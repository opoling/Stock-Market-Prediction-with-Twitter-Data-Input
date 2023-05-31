# Importing packages
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

tweets_df = pd.read_csv('TSLA_tweets.csv').drop(['Unnamed: 0'], axis=1)
tweets_df.head()