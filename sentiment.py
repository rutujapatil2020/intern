from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Classify the polarity of the text
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Example usage
text_to_analyze = "I love programming. It's so much fun!"
sentiment_result = analyze_sentiment(text_to_analyze)
print(f"Sentiment: {sentiment_result}")

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    # Get the polarity score
    compound_score = analyzer.polarity_scores(text)['compound']
    # Classify the sentiment based on the compound score
    if compound_score >= 0.05:
        return 'Positive'
    elif -0.05 < compound_score < 0.05:
        return 'Neutral'
    else:
        return 'Negative'

# Example usage with VADER
text_to_analyze = "I love programming. It's so much fun!"
sentiment_result_vader = analyze_sentiment_vader(text_to_analyze)
print(f"Sentiment (VADER): {sentiment_result_vader}")
