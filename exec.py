from getSentiment import getSentiment
import matplotlib.pyplot as plt

def plotting(dataframe,stock):
    analysis = ["text_blob", "vader_sentiment", "Real_time Stock"]
    dataframe.plot(x='date', y=analysis, kind = 'line',title=stock).get_figure().savefig(stock)
    plt.grid(which="major",alpha=0.6)
    plt.grid(which="minor",alpha=0.3)
    plt.show()

if __name__ == "__main__":
    print("CIS-600 Social Media Data Mining Final Project:\nPerforming sentiment analysis on stock tickers using mined data from Twitter\n")
    print("Choose from the following sample list of stock tickers or enter your stock ticker\n Tickers for:\n")
    sample_stocks = ['Nvidia is NVDA', 'Microsoft is MSFT', 'Apple.Inc is AAPL', 'Roblox.Inc is RBLX']
    for i in range(len(sample_stocks)):
        print((i+1),".", sample_stocks[i])
    stock = input("Enter stock ticker: \n")
    dataframe = getSentiment(stock)
    dataframe.rename(columns = {'Adj Close':'Real_time Stock'}, inplace = True)
    plotting(dataframe,stock)
    print("Exited")
    
