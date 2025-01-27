import requests
from textblob import TextBlob
import tkinter as tk
from tkinter import messagebox

# Facebook Graph API credentials
access_token = 'EAAJY2gT2yyoBOy5ZBbSIv2PLQTCXAFRuWHTTX8KXfghQeN1ddPU9oJOAX3OiKLO5bAZCbkZBY0mthEPFwoYl2whOrFQO3XJ7tfgdtkqSMQNyFiroHb0JtwfGdHtnjZCZBojiRskQzQspFkv3kv3xG54DhZCp4ZBEtWmszFlqxlJjVOHbLdN3QwqiSznQET0yV9VZBGjqH50ZCDAUbv1OedcFoxMYZBYSX1gYyPETkGvubLcxsSh5YBv5CXULlgPRgnRQZDZD'
user_id = "1768298886926918"

# Fetch user's posts using Facebook Graph API
def get_user_posts(user_id, access_token):
    url = f'https://graph.facebook.com/v13.0/{user_id}/posts'
    params = {'access_token': access_token}
    response = requests.get(url, params=params)
    data = response.json()
    return data.get('data', [])

# Analyze sentiment of each post
def analyze_sentiment(posts):
    results = []
    for post in posts:
        message = post.get('message', '')
        if message:
            sentiment = TextBlob(message).sentiment.polarity
            sentiment_label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
            emoji = "😊" if sentiment > 0 else "😞" if sentiment < 0 else "😐"
            results.append((message, sentiment_label, emoji))
    return results

# Display results in a separate window
def display_results():
    # Create the root Tkinter window
    root = tk.Tk()
    root.title("Sentiment Analysis Results")
    root.geometry("800x600")  # Window size

    # Get user posts and analyze sentiment
    user_posts = get_user_posts(user_id, access_token)
    results = analyze_sentiment(user_posts)

    # Create a scrollbar
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a Text widget for displaying results
    text_widget = tk.Text(root, wrap=tk.WORD, height=20, width=80, yscrollcommand=scrollbar.set, font=("Helvetica", 16))
    text_widget.pack()

    # Display each post and its sentiment in the Text widget with colors and big fonts
    for post, sentiment, emoji in results:
        if sentiment == "Positive":
            color = "green"
        elif sentiment == "Negative":
            color = "red"
        else:
            color = "gray"

        # Insert the post message in large font and sentiment with color
        text_widget.insert(tk.END, f"Post: {post}\n", "post")
        text_widget.insert(tk.END, f"Sentiment: {sentiment} {emoji}\n\n", sentiment)

        # Tag the text with appropriate styles
        text_widget.tag_configure("post", font=("Helvetica", 18, "bold"), foreground="black")  # Post text style
        text_widget.tag_configure(sentiment, font=("Helvetica", 16, "italic"), foreground=color)  # Sentiment style

    scrollbar.config(command=text_widget.yview)

    # Start the Tkinter event loop
    root.mainloop()

# Call the display function
display_results()
