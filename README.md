# Scion Bot 📊
### An entry to CodePlay 2020 by Asseco.

### [Webpage 🖥](https://www.3ify.io/codeplay)

---

2020, the year of pandemic and uncertainity, saw unprecedented levels of volatility on the stock market. VIX, CBOE Volatility Index, sometimes reffered to as "fear index", hit its all-time high on 16 March 💸 [1]. This, along with major societal changes caused by COVID-19 [2] and significant media coverage of financial markets, caused the raise of retail investors 📈 [3][4]. The individual investors 💻 (non-professional market participants) account for over 20% of traded equity [5][6], and the knowledge of their movements became an object of great interest for big investors [7].

```
10 highest VIX closes

Mon 16 Mar 2020 = 82.69
Thu 20 Nov 2008 = 80.86
Mon 27 Oct 2008 = 80.06
Fri 24 Oct 2008 = 79.13
Wed 18 Mar 2020 = 76.45
Tue 17 Mar 2020 = 75.91
Thu 12 Mar 2020 = 75.47
Wed 19 Nov 2008 = 74.26
Fri 21 Nov 2008 = 72.67
Thu 19 Mar 2020 = 72.00
```
Table 1: All-Time Highest VIX Closes [8].

Some attempts have been made at quantizing the retail investors' sentiment. Mjysong's [Momentum Trading off Sentiment from r/wallstreetbets](https://medium.com/@mjysong/momentum-trading-off-sentiment-from-r-wallstreetbets-149c19c7538d) article on Medium describes one such inquiry. The author attempts to evaluate post on [r/wallstreetbets](https://www.reddit.com/r/wallstreetbets/) 💵, 1.6 million strong financial community on social media site Reddit, by whether they represent bullish 📈 or bearish 📉 sentiment. He creates a dictionary of 200 words of subreddit's subculture, which he uses to calculate Bull/Bear ratio from 25 most-commented threads.

Our implementation includes several substantial improvements. First off, instead of evaluating one subreddits sentiment as a whole, our bot monitors 17 financial subreddits with focus on investing, with total number of members just over 20M. The list is: [r/algotrading](https://www.reddit.com/r/algotrading/), [r/dividends](https://www.reddit.com/r/dividends/), [r/Etoro](https://www.reddit.com/r/Etoro/), [r/finance](https://www.reddit.com/r/finance/), [r/Forex](https://www.reddit.com/r/Forex/), [r/investing](https://www.reddit.com/r/investing/), [r/Options](https://www.reddit.com/r/options/), [r/OptionsExclusive](https://www.reddit.com/r/OptionsExclusive/), [r/PersonalFinance](https://www.reddit.com/r/personalfinance/), [r/RobinHood](https://www.reddit.com/r/RobinHood/), [r/SecurityAnalysis](https://www.reddit.com/r/SecurityAnalysis/), [r/StockMarket](https://www.reddit.com/r/StockMarket/), [r/stocks](https://www.reddit.com/r/stocks/), [r/tdameritrade](https://www.reddit.com/r/tdameritrade/), [r/trading212](https://www.reddit.com/r/tdameritrade/), [r/wallstreetbets](https://www.reddit.com/r/wallstreetbets/) and [r/Webull](https://www.reddit.com/r/Webull/). Furthermore, the bot can (but doesn't have to) look for chatter about specific companies 🔎. All the user has to do is pass it the ticker of company they're interested in, and the program will generate keywords on its own, with the use of yfinance python library.

The gathered data is analyzed two-folds: first, with use of manually written dictionary of bullish 🐂 and bearish 🐻 keywords. The outcome is series of bullishness metric datapoints and their dates (one for each relevant comment), a set of those for every subreddit. The other analysis we implemented is [MonkeyLearn 🐒 Sentiment Analysis Classifier](https://app.monkeylearn.com/main/classifiers/cl_pi3C7JiL/tab/api/).

![Amazon mentions plot](/results/mentions_over_time.png)

Figure 1: Example of mentions of Amazon over the week. Note the Amazon Prime Day (2nd day on the graph which was the 13th of October, red line stands for negative comments, gray for neutral and green for positive)

---

[1]: [What Does the Volatility Index (VIX) Indicate?](https://www.investopedia.com/news/what-does-volatility-index-vix-indicate/), James Chen, 13 March 2020.

[2]: [How ‘Animal Crossing’ Is Preparing Players to Trade Stocks](https://www.bloomberg.com/news/articles/2020-10-07/stock-market-how-nintendo-game-animal-crossing-prepares-players-to-trade), Berber Jin, 7 October 2020.

[3]: [Investor Intelligence: The Rise of Retail](https://www.nasdaq.com/articles/investor-intelligence%3A-the-rise-of-retail-2020-08-26), MarketInsite, 26 August 2020.

[4]: [The Rise of the Retail Investor](https://medium.com/@ryantanby1/the-rise-of-the-retail-investor-d4bd93e52bf2), Ryan Tan, 2 June 2020.

[5]: [Retail Investor](https://www.investopedia.com/terms/r/retailinvestor.asp), Adam Hayes, 31 March 2020.

[6]: Retail Investors Now the Second-Largest Segment, Larry Tabb.

[7]: [Reddit's Stock Threads Become a Must-Read on Wall Street](https://www.bloomberg.com/news/articles/2020-09-15/big-investors-are-dying-to-know-what-the-little-guys-are-doing), Sarah Ponczek, 15 September 2020.

[8]: [All-Time Highest VIX Closes](https://www.macroption.com/vix-all-time-high/), Macroption.
