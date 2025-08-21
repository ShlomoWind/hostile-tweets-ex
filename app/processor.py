import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Process:
    def __init__(self,text):
        self.text = text

# Finding the rarest word in any text
    def rarest_word(self):
        words = self.text.split()
        word_count = {}
        for word in words:
            word = word.lower()
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
        rarest = min(word_count, key=word_count.get)
        return rarest

# Finding the sentiment of the text - positive, negative, or neutral.
    def sentiment_type(self):
        nltk.download('vader_lexicon')
        score = SentimentIntensityAnalyzer().polarity_scores(self.text)
        if score['compound'] >= 0.05:
            return 'positive'
        elif score['compound'] <= -0.05:
            return 'negative'
        else:
            return 'neutral'

# Finding names of weapons according to a blacklist.
    def weapon_blacklist(self):
        weapons = "data/weapon_list.txt"
        found_weapons = [weapon for weapon in weapons if weapon in self.text.lower()]
        return found_weapons[0] if found_weapons else None