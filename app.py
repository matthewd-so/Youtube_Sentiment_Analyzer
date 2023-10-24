import os
import json
import google.auth
from googleapiclient.discovery import build
import boto3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Set up the Google API client
    DEVELOPER_KEY = '' # <-- Insert your developer key here
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Set up the AWS Comprehend client
    aws_access_key_id = '' # <-- Insert your AWS access key id here
    aws_secret_access_key = '' # <-- Insert your AWS secret access key here
    region_name = 'us-east-2'
    comprehend = boto3.client('comprehend', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    # Scrape the comments from the YouTube video
    video_id = '' # <-- Insert the id of youtube video here (Sample URL: https://www.youtube.com/watch?v=WAFtQjgaVDE, Sample ID: WAFtQjgaVDE)
    comments = []
    results = youtube.commentThreads().list(part="snippet", videoId=video_id, textFormat="plainText", maxResults=50).execute()
    for item in results["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    # Perform sentiment analysis on the comments using AWS Comprehend
    coms = []
    sents = []
    scores = []

    for comment in comments:
        response = comprehend.detect_sentiment(Text=comment, LanguageCode='en')
        sentiment = response['Sentiment']
        score = response['SentimentScore'][sentiment.title()]
        print(f"Comment: {comment}")
        print(f"Sentiment: {sentiment} (Score: {score:.2f})")
        coms.append(comment)
        sents.append(sentiment)
        scores.append("{:.2f}".format(score))
    
    # Convert everything to a string
    string_comments = [str(i) for i in coms]
    string_sentiments = [str(i) for i in sents]
    string_scores = ['  ' + str(i) for i in scores]

    # Display on web page
    html = """
            <html>
                <head>
                    <title>Youtube Sentiment Analysis</title>
                </head>
                <body>
                    <table>
                        <thead>
                            <tr>
                                <th>Comments</th>
                                <th>Sentiments</th>
                                <th>Scores</th>
                            </tr>
                        </thead>
                        <tbody>
                            {}
                        </tbody>
                    </table>
                </body>
            </html>
        """
    rows = ""
    for i in range(len(string_comments)):
        rows += "<tr><td style='padding: 30px'>{}</td><td style='padding: 30px'>{}</td><td style='padding: 30px'>{}</td></tr>".format(string_comments[i], string_sentiments[i], string_scores[i])
    return html.format(rows)

if __name__ == '__main__':
    app.run(port=5500)
