import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Process:
    def __init__(self,data_frame):
        self.df = data_frame
        self.df["rarest_word"] = self.df["Text"].apply(self.rarest_word)
        self.df["sentiment"] = self.df["Text"].apply(self.sentiment_type)
        self.df["weapon_detected"] = self.df["Text"].apply(self.weapon_blacklist)
        nltk.download('vader_lexicon')

# Finding the rarest word in any text
    def rarest_word(self,text):
        all_words = text.split()
        words_count = {word: all_words.count(word) for word in all_words}
        rarest = min(words_count, key=words_count.get)
        return rarest

# Finding the sentiment of the text - positive, negative, or neutral.
    def sentiment_type(self,text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        if score['compound'] >= 0.05:
            return 'positive'
        elif score['compound'] <= -0.05:
            return 'negative'
        else:
            return 'neutral'

# Finding names of weapons according to a blacklist.
    def weapon_blacklist(self, text):
        with open("data/weapon_list.txt", "r") as f:
            weapons = [line.strip().lower() for line in f.readlines()]
        found_weapons = [weapon for weapon in weapons if weapon in text.lower()]
        return found_weapons[0] if found_weapons else None

# Returning the processed data frame
    def get_processed_data(self):
        return self.df