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

# Testing the Data:
tweets_df.tweet[500]  
tweets_df.cleaned_tweet[500]

# 4. Lemmatizing the cleaned tweets
lemmatizer = WordNetLemmatizer()

def lemmatize(tweets):
    for i in range(len(tweets)):
        for w in [tweets[i]]:
            pos_tag_list = nltk.pos_tag(w)
        wordnet_tags = []
        for j in pos_tag_list:
            # adjective
            if j[1].startswith('J'):
                wordnet_tags.append(wordnet.ADJ)
            # noun
            elif j[1].startswith('N'):
                wordnet_tags.append(wordnet.NOUN)
            # adverb
            elif j[1].startswith('R'):
                wordnet_tags.append(wordnet.ADV)
            # verb
            elif j[1].startswith('V'):
                wordnet_tags.append(wordnet.VERB)
            # default to noun
            else:
                wordnet_tags.append(wordnet.NOUN)
        lem_words = []
        for k in range(len(tweets[i])):
            lem_words.append(lemmatizer.lemmatize(tweets[i][k], pos=wordnet_tags[k]))
        lem_tweet = ' '.join(lem_words)
        tweets[i] = lem_tweet