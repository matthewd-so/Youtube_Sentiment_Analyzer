**Youtube Sentiment Analysis**

This project is a web application that performs sentiment analysis on YouTube video comments and displays the results in a tabular format. It uses the YouTube API to retrieve comments from a specified video and AWS Comprehend for sentiment analysis. The results are then displayed on a web page using Flask and HTML.

**Prerequisites**

Before running this application, you will need to have the following:

- A Google developer key
- An AWS access key ID and secret access key
- Python 3 installed on your system
- Flask and boto3 Python packages installed on your system

**Getting Started**

To get started with this application, follow the steps below:

1. Clone the repository to your local machine
2. Install the required Python packages using the following command:
```pip install -r requirements.txt```
3. Open the app.py file and insert your developer key and AWS access key ID and secret access key in the appropriate places
Run the application using the following command:
```python app.py```
4. Open a web browser and go to http://localhost:5500
5. Enter the ID of the YouTube video for which you want to perform sentiment analysis and click on the "Submit" button
The comments, sentiments, and scores will be displayed in a tabular format on the web page.

**License**
This project is licensed under the MIT License. See the LICENSE file for details.
