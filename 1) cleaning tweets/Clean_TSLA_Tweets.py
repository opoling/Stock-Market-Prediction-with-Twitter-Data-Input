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
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

def lemmatize(tweets):
    for i in range(len(tweets)):
        for w in [tweets[i]]:
            pos_tag_list = nltk.pos_tag(w)
        wordnet_tags = []
        for j in pos_tag_list:
            if j[1].startswith('J'):
                wordnet_tags.append(wordnet.ADJ)
            elif j[1].startswith('N'):
                wordnet_tags.append(wordnet.NOUN)
            elif j[1].startswith('R'):
                wordnet_tags.append(wordnet.ADV)
            elif j[1].startswith('V'):
                wordnet_tags.append(wordnet.VERB)
            else:
                wordnet_tags.append(wordnet.NOUN)
        lem_words = []
        for k in range(len(tweets[i])):
            lem_words.append(lemmatizer.lemmatize(tweets[i][k], pos=wordnet_tags[k]))
        lem_tweet = ' '.join(lem_words)
        tweets[i] = lem_tweet

# tagging words with their pos
#nltk.download('averaged_perceptron_tagger')   
lemmatize(tweets_df.cleaned_tweet)
tweets_df.head()


# Removing 'tesla', 'q', '#'
def remove_clean(df):
    df.cleaned_tweet = df.cleaned_tweet.map(lambda x: x.replace('tesla', ''))
    df.cleaned_tweet = df.cleaned_tweet.map(lambda x: x.replace('tsla', ''))
    df.cleaned_tweet = df.cleaned_tweet.map(lambda x: x.replace('q', ''))
    df.cleaned_tweet = df.cleaned_tweet.map(lambda x: x.replace('#', ''))
remove_clean(tweets_df)
tweets_df.cleaned_tweet[500]

# Combine tweets together into single str
all_words_str = ' '.join([tweet for tweet in tweets_df.cleaned_tweet])

# making list of all words
all_words_list = all_words_str.split()

# 5. Fequency analysis figures

# line graph:
# top 50 most used words:
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html 

plt.figure(figsize=(12,5))
plt.xticks(fontsize=8, rotation=90)
word_freq = nltk.FreqDist(all_words_list)
word_freq.plot(50, cumulative=False)

# Word cloud with the word frequenciesL
# https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html

word_cloud = WordCloud(
    width=900,
    height=500,
    max_words=500,
    max_font_size=100,
    relative_scaling=0.5,
    colormap='Oranges',
    background_color='Black',
    normalize_plurals=True).generate_from_frequencies(word_freq)
plt.figure(figsize=(16,9))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
plt.show()
    
# Table of the frequency of each word
word_freq_df = pd.DataFrame({'Word': list(word_freq.keys()), 
                             'Count': list(word_freq.values())}).sort_values(by=['Count'], 
                              ascending=False)
word_freq_df.head(25)

# Box plot
word_freq_df = word_freq_df.nlargest(columns='Count', n=20)
plt.figure(figsize=(12,5))
ax = sns.barplot(data=word_freq_df, x='Word', y='Count')
ax.set_title('Top 20 Frequent Words', fontsize=12)
plt.show()

# Saving cleaned tweets
tweets_df.to_csv('cleaned_tsla_tweets.csv', index=False)