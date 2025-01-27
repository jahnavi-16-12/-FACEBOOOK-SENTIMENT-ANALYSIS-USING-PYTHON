# Facebook Sentiment Analysis Using Python

This project analyzes the sentiment of Facebook posts using the Facebook Graph API and Python. The primary goal is to determine whether the sentiment of each post is **positive**, **negative**, or **neutral**. The project leverages **Natural Language Processing (NLP)** techniques for text analysis and sentiment classification. It uses the **TextBlob** library for sentiment analysis and fetches posts from Facebook using the Facebook Graph API.

## Features
- **Fetch Facebook Posts:** Get posts from a user's Facebook account using the Facebook Graph API.
- **Sentiment Classification:** Classifies the sentiment of each post as positive, negative, or neutral using the TextBlob library.
- **Visual Representation:** Displays the sentiment distribution (positive, negative, neutral)

## Screenshots
Here are some images showing the project in action:

- **Access Token Generation**
  ![Access Token Generation](images/access_token_generation.png)

- **Output FB_Sentiment Analysis**
  ![Sentiment Analysis Output](images/output.png)

- **Website Screenshot**
  ![Website Screenshot](images/website_screenshot.png)

## Prerequisites
Before running the project, make sure you have the following installed:
- Python 3.x
- A Facebook account to generate an access token

## How to Set Up and Run the Project:

### 1. Clone the Repository:
Clone the repository to your local machine:
```bash
git clone https://github.com/jahnavi-16-12/-FACEBOOOK-SENTIMENT-ANALYSIS-USING-PYTHON.git
```
### 2. Navigate to the Project Directory:
Open a terminal and navigate to the project directory:

```bash
cd path/to/-FACEBOOOK-SENTIMENT-ANALYSIS-USING-PYTHON
```
### 3. Install the Dependencies:
Use the following command to install the required libraries:
```bash
pip install -r requirements.txt
```
### 4. Run the Project:
Once the dependencies are installed, run the Python script:
```bash
python fb_sentiment_analysis.py
```
### 5. Get Your Facebook Access Token:
To fetch posts from Facebook, you need an access token:
Go to the Facebook Developer Portal.
Use the Graph API Explorer to generate your token with the required permissions (like user_posts).
Replace the token in the script with your generated token.
### License:
This project is licensed under the MIT License - see the LICENSE file for details.
### Contributions:
Feel free to fork the repository and make pull requests. If you encounter any issues or have suggestions for improvements, don't hesitate to open an issue or submit a PR.

### Breakdown:
1. **Images Section**: I've added a "Screenshots" section to display the images of the project, including access token generation, output, and website screenshots.
2. **Markdown for Images**: Each image is inserted using `![Alt text](image_path)`
   - ![Sentiment Analysis Output](images/output.png)
   - ![Website Screenshot](images/website_screenshot.png)
   -  ![Access Token Generation](images/access_token_generation.png)
6. **Image Paths**: Make sure that the `images/` folder and the images inside it (like `access_token_generation.png`, `output.png`, etc.) exist in your repository.

You can add or modify image paths as per your actual directory structure. Just ensure the images are in the right


