# 1. Importing packages
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords, wordnet
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
lemmatize = WordNetLemmatizer()
import warnings
warnings.filterwarnings(action='ignore')

# text data visualization
import matplotlib.pyplot as plt
#%matplotlib inline
#from wordcloud import WordCloud
import seaborn as sns

# 2. Loading dataset
tweets_df = pd.read_csv('TSLA_tweets.csv').drop(['Unnamed: 0'], axis=1)
tweets_df.head()
tweets_df.date = pd.to_datetime(tweets_df.date)

# 3. Cleaning the tweets
def clean(df):
    df['cleaned_tweet'] = df.tweet.map(lambda x: x + ' ')
    df.cleaned_tweet = df.cleaned_tweet.map(lambda x: re.sub(r'http.*', '', x))
    df.cleaned_tweet = df.cleaned_tweet.map(lambda x: re.sub(r'[^a-zA-Z#]', ' ', x))
    df.cleaned_tweet = df.cleaned_tweet.map(lambda x: x.lower())
    stopword_list = stopwords.words('english')
    for i in range(len(df.cleaned_tweet)):
        tokens = word_tokenize(df.cleaned_tweet[i])
        clean_tokens = [w for w in tokens if w not in stopword_list]
        df.cleaned_tweet[i] = clean_tokens

clean(tweets_df)
tweets_df.head()
                                                