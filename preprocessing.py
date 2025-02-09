import re
import emoji
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize


import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


# Initializing Lemmatizer and Stemmer
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Function for emoji handling (this converts emojis into text descriptions)
def handle_emojis(text):
    return emoji.demojize(text)

# Function for spelling correction
def correct_spelling(r):
    return str(TextBlob(r).correct())


def lemmatize_and_stem(r):
    words = word_tokenize(r)
    
    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]
    
    # Lemmatize and Stem
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    stemmed_words = [stemmer.stem(word) for word in lemmatized_words] 
    
    result = ' '.join(stemmed_words)

    return result

def preprocess_text(r):
    r = str(r).lower().strip()

    # Replacements for currency and percentages
    r = r.replace('%', ' percent')
    r = r.replace('$', ' dollar ')
    r = r.replace('₹', ' rupee ')
    r = r.replace('€', ' euro ')
    r = r.replace('@', ' at ')

    # Number abbreviations (e.g., 1,000,000 becomes 1m)
    r = r.replace(',000,000,000 ', 'b ')
    r = r.replace(',000,000 ', 'm ')
    r = r.replace(',000 ', 'k ')
    r = re.sub(r'([0-9]+)000000000', r'\1b', r)
    r = re.sub(r'([0-9]+)000000', r'\1m', r)
    r = re.sub(r'([0-9]+)000', r'\1k', r)

    # Contractions dictionary for replacement
    contractions = {
        "ain't": "am not", "aren't": "are not", "can't": "can not", "can't've": "can not have", "cause": "because",
        "could've": "could have", "couldn't": "could not", "couldn't've": "could not have", "didn't": "did not",
        "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hadn't've": "had not have", "hasn't": "has not",
        "haven't": "have not", "he'd": "he would", "he'd've": "he would have", "he'll": "he will", "he'll've": "he will have",
        "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",
        "i'd": "i would", "i'd've": "i would have", "i'll": "i will", "i'll've": "i will have", "i'm": "i am", "i've": "i have",
        "isn't": "is not", "it'd": "it would", "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have",
        "it's": "it is", "let's": "let us", "ma'am": "madam", "mayn't": "may not", "might've": "might have",
        "mightn't": "might not", "mightn't've": "might not have", "must've": "must have", "mustn't": "must not",
        "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have", "o'clock": "of the clock",
        "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not",
        "shan't've": "shall not have", "she'd": "she would", "she'd've": "she would have", "she'll": "she will",
        "she'll've": "she will have", "she's": "she is", "should've": "should have", "shouldn't": "should not",
        "shouldn't've": "should not have", "so've": "so have", "so's": "so as", "that'd": "that would",
        "that'd've": "that would have", "that's": "that is", "there'd": "there would", "there'd've": "there would have",
        "there's": "there is", "they'd": "they would", "they'd've": "they would have", "they'll": "they will",
        "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have",
        "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have",
        "we're": "we are", "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have",
        "what're": "what are", "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have",
        "where'd": "where did", "where's": "where is", "where've": "where have", "who'll": "who will", "who'll've": "who will have",
        "who's": "who is", "who've": "who have", "why's": "why is", "why've": "why have", "will've": "will have",
        "won't": "will not", "won't've": "will not have", "would've": "would have", "wouldn't": "would not",
        "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would", "y'all'd've": "you all would have",
        "y'all're": "you all are", "y'all've": "you all have", "you'd": "you would", "you'd've": "you would have",
        "you'll": "you will", "you'll've": "you will have", "you're": "you are", "you've": "you have", "'ve": " have",
        "n't": " not", "'re": " are", "'ll": " will"
    }

    # Replacing contractions
    r_decontracted = [contractions.get(word, word) for word in r.split()]
    r = ' '.join(r_decontracted)

    # Removing HTML tags using regex
    r = re.sub(r'<.*?>', '', r)

    # Correcting spelling
    r = correct_spelling(r)

    # Handling emojis (convert to text)
    r = handle_emojis(r)

    # Lemmatization and Stemming with Stopwords removal
    r = lemmatize_and_stem(r)

    return r
