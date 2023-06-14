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