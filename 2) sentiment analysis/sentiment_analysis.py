# import packages
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# what is %matplotlib inline: https://stackoverflow.com/questions/43027980/purpose-of-matplotlib-inline
%matplotlib inline
import seaborn as sns


#Load dataset
tweets_df = pd.read_csv('cleaned_tsla_tweets.csv')
tweets_df = tweets_df.iloc[:, [0,1,4]]
tweets_df.head()

tweets_df.info()

#Change date column into datetime type
tweets_df.date=pd.to_datetime(tweets_df.date)
tweets_df.info()

# check for null values
# https://www.miamioh.edu/cads/students/coding-tutorials/python/data-cleaning/index.html
tweets_df.isnull().sum()

# delete the null values
tweets_df = tweets_df.dropna()

# Calculating sentiment scores
# use TextBlob for sentiment scores:
tweets_df['sentiment_score'] = tweets_df.apply(lambda row: TextBlob(row.cleaned_tweet).sentiment[0], axis=1)
tweets_df.head()

# 4. Previewing sentiment scores of tweets
tweets_df.cleaned_tweet[174]
tweets_df.sentiment_score[174]

# https://pandas.pydata.org/docs/user_guide/options.html
pd.options.display.max_colwidth = 250
random_subset = tweets_df.sample(n=15)
# remove columns
random_subset = random_subset.drop(columns=['id','date'])
random_subset = random_subset.rename(columns={'tweet': 'Original Tweet', 
                                              'cleaned_tweet': 'Cleaned Tweet', 
                                              'sentiment_score':'Sentiment Score'})

random_subset.head(5)

# 5. Frequency analysis of sentiment scores