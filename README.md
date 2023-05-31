# Stock Market Prediction with Twitter Data Input

***FYI:** This personal project was first proposed to my college as a summer research opportunity with my professor advisor. I was very excited for the opportunity to have this as a college research and learn more about the algorithms used for this research, the machine learning concepts, and also using real life factor of stock prediction like Twitter. I was very dissapointed when I learned my propsal was rejected only because I proposed using one stock ($TSLA) for this research. This did not stop me from pursuing my interest, I had made the decision in doing this research by myself---I will not recieve any funds. 

## My College Summer Research Proposal: Machine Learning Approach for Stock Market Prediction with Twitter Data Input

### Abstract
Prediction of stocks for financial advisors is challenging because of how volatile they can be due to external factors like the social media platform Twitter. This research will understand how machine learning algorithms can use Twitter to predict how it will affect stock values. The tweets that contain the keywords of stock “$TSLA” are used as our main data. We process them through sentiment analysis. The resulting data, along with the conventional financial data, will be fed to a Recurrent Neural Network and Long Short-Term Memory to find the most accurate stock prediction.

### Budget Summary
- $210 payment to Vicinitas to be able to download historical Twitter data for my research

### Goal
Stock market prediction is traditionally a very challenging task. The stock market consists of a vast amount of stocks that are impacted differently by various factors and have different growth trends and values. One way stocks are impacted is by tweets from the social media platform Twitter. The purpose of this research is to investigate the impacts of tweets on the stock trends (e.g., Tesla stock ($TSLA) value) and how the Twitter data can be incorporated into machine learning algorithms to make predictions of the stock market value. This research will help us understand the complexity of the stock market and if it is computationally predictable. We expect a reasonable stock market prediction accuracy from this research which can greatly help people make wise stock trading decisions using our method.

### Introduction
Many people and companies rely on predicting the price movement and direction of the stock market because of how vital the market is to the country’s economy. Stock traders have to predict the trends in the market to determine when to buy or sell stocks to gain profits. The prediction of the stock market is an area of research that has been done for a long time.  The Efficient Market Hypothesis states that the stock market values are significantly driven by new information, making it follow a random walk pattern [1]. Investors pay attention to a company’s performance through the news or social media websites.
 One platform is Twitter due to the many finance and stock market updates shared. There, users express opinions, feelings, decisions, and predictions that can cause rippling effects but investors can not assess all of these tweets by themself. That is when a computational analysis is needed for investors for it will evaluate stock trends using Twitter data to make predictions of the stocks. In this research, we will test how information like tweets, about a stock like $TSLA, will affect the stock price and how to implement predictive algorithms on future stock moments. 
This research will come across the problem of how to generate predictions for the stock market. A Neural Network is a sequence of cascading layers with a great number of trainable parameters. The parameters are trained and determined by processing the known training dataset that clearly specifies the input to and output from the network. The trained network is then applied to the unknown dataset, which consists of input only, to predict the best outcome based on a loss function.  There exists a variety of different neural networks that suit different applications.  The Neural Network that our research will be using is Recurrent Neural Network (RNN) [2] which is designed to work on time series data like the stock market data. The structure of RNN is slightly different from regular Neural Networks: there are feedback loops inside of RNN called recurrent units. These recurrent units process the data information for a set amount of time repeatedly. There are a couple of problems that RNN has when it comes to predicting: loss of information through time and a large amount of error accumulating [2]. To avoid the problems, this research will involve a variant of RNN called Long Short-Term Memory Networks (LSTMs) since it is able to model long-range dependencies information and temporal sequences more accurately [3]. LSTM is capable of learning sequence prediction problems as it remembers data from drawn-out stretches of time [4]. In the research, we want to see how efficient and accurate the LSTM is over the RNN based on how fast the predictions are made on the stock. We will compare the results with the LSTM prediction time to better understand how an accurate prediction takes on time. 

### Method
The basis of this research will go through three stages: data collecting and cleaning, sentiment analysis, and prediction programming. The first stage will be using software called Vicinitas to download historical tweets on the hashtag/keywords of TSLA [5]. Once downloaded as a file, we will use the programming language Python to clean the tweets and remove unnecessary words, characters, special characters, and HTTP links. The cleaned tweets will be then counted based on their frequency.
	The next stage is to computationally determine whether a text conveys a positive, negative, or neutral emotion from the user of the tweet. This is done by sentiment analysis. Sentimental is used for various analyses: market field to develop strategies on understanding customers' sentiments towards products, political field to analyze the political views better and understand reactions of the government’s perspectives, and social phenomena for spotting the public's mood to news articles online [6]. For this research purpose, sentiment analysis will be implemented on users’ views on $TSLA stock to program machine learning predictions. We will then program the algorithms of RNN and LSTM. By loading the sentimental analysis dataset and building the RNN and  LSTM model, we will be able to compare the two’s running times as they compute predictions. 

### Outcomes
Having no prior experience in machine learning as a student, we are excited to learn the concepts and algorithms involved in this research to successfully do further projects with machine learning. We hope to predict the future movement of the stock market based on analyzing the sentiment of Twitter tweets related to the stock market and utilizing machine learning algorithms. The research will provide valuable insight into the inner workings of machine learning on predictions, and we would be more than willing to present at the Elkin R. Isaac Research Symposium. We understand the challenges in this research and we are excited for the opportunity to overcome them to be able to have results in predicting the trend of stock prices in finance. 

### Timeframe of Project
- Start Date: May 15th
- The daily task will be assigned by Dr. Zhang every morning
- Week 1:
  - We will collect information and data from Yahoo and Vicinitas to acquire $GOOGL Stock data and keywords of $GOOGL Twitter data. We will begin to clean the Twitter data by coding with Python to obtain the most frequent valuable words related to the stock.
- Week 2-3:
  - We will continue to clean the Twitter data and then start sentiment analysis on the data to appoint emotions to each text. It will be appointed into one of three categories (positive, negative, or neutral).
- Week 4-7:
  - These weeks will consist of time-consuming trials of the machine learning algorithms RNN and LSTM coding and incorporating the sentiment analysis data into this program with Python.
- Week 8:
  - We will be wrapping up our research and program by coding the data graphs and visualizations to see the machine learning $GOOGL stock prediction with Twitter data involved. 
We will be comparing the running time of the two algorithms to draw conclusions about our research and results.
- End Date: July 17th

### Reference
- Malkiel, B. G. (2003, Winter). The Efficient Market Hypothesis and Its Critics. Journal of Economic Perspectives, 17(0046-9777), 1. https://doi.org/10.1257/089533003321164958
- Bissau, A. (2022). Recurrent Neural Network (RNN) Tutorial: Types, Examples, LSTM and More. - - Simplilearn. https://www.simplilearn.com/tutorials/deep-learning-tutorial/rnn
- Thormann, M., Farchmin, J., Weisser, C., Kruse, R., Sa ̈fken, B., Silbersdorff, A.(2021). Stock Price Predictions with LSTM Neural Networks and Twitter Sentiment. International Academic Press, 9(268-287), 2310-5070.
- Geeks for Geeks. (2021, Septemnber 29). Deep Learning | Introduction to Long Short Term Memory. Geeks for Geeks. https://www.geeksforgeeks.org/deep-learning-introduction-to-long-short-term-memory/
- Vicinitas. (n.d.). Download User Tweets for Free. https://www.vicinitas.io/free-tools/download-user-tweets
- Pimprikar, R., Ramachandran, S., & Senthilkumar, K. (2017). Use of Machine Learning Algorithms and Twitter Sentiment Analysis for Stock Market Prediction. International Journal of Pure and Applied Mathematics, 115(1314-3395), 2.


