import nltk
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Function to analyze sentiment
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

# List of CSV files to analyze
csv_files = [
    'Product_reviews.csv',
    'Movie_reviews.csv',
    'SocialMedia_posts.csv',
    'News_headlines.csv',
    'CustomerService_Feedback.csv'
]

for file in csv_files:
    # Load data from the CSV file
    df = pd.read_csv(file)

    # Ensure the text column exists
    if 'text' not in df.columns:
        raise ValueError(f"The CSV file {file} must contain a 'text' column.")

    # Analyze sentiment for each text
    sentiments = df['text'].apply(analyze_sentiment)
    df = pd.concat([df, sentiments.apply(pd.Series)], axis=1)

    # Display the DataFrame with sentiment scores
    print(f"Results for {file}:")
    print(df)

    # Visualize the results
    df['compound'].hist(bins=20)
    plt.title(f'Sentiment Analysis Results for {file}')
    plt.xlabel('Compound Score')
    plt.ylabel('Frequency')
    plt.show()
