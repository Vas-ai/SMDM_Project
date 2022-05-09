import flask
from flask import Flask,jsonify, request, render_template
from twitter_tweet_Extraction import getTweets
from getSentiment import getSentiment
from getRealStock import *
import pandas as pd
import json
import matplotlib.pyplot as plt
import os

# data = {'date', 'text_blob', 'vader_sentiment','Adj Close'}

def getting_dataframe(stock):
    dataframe = getSentiment(stock)
    dataframe.rename(columns = {'Adj Close':'Real_time Stock'}, inplace = True)
    plotting(dataframe,stock)

def plotting(dataframe,stock):
    analysis = ["text_blob", "vader_sentiment", "Real_time Stock"]
    dataframe.plot(x='date', y=analysis, kind = 'line')
    plt.grid(axis = 'y', color = 'green', linestyle = '-')
    plt.grid(axis = 'x', color = 'red', linestyle = '-')
    plt.title(stock)
    plt.show()

if __name__ == "__main__":
    print("Getting the stock dataframe and printing it: \n")
    print("Choose from the following sample list of stock tickers or enter your stock ticker\n")
    sample_stocks = ['For Nvidia = NVDA', 'For Tesla = TSLA', 'For Apple = AAPL', 'For ROBLOX = RBLX']
    for i in range(len(sample_stocks)):
        print((i+1),sample_stocks[i])
    stock = input("Enter stock ticker: \n")
    result_data = getting_dataframe(stock)
    print("Exited")
