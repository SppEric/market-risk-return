# Risk, Return, and Market Anomalies: An Analysis of S&P 500 Companies

![abstract poster](./Data%20Science%20PDF%20Poster.png)

## Final Project Video
[![Watch the video](https://img.youtube.com/vi/YQn5Gf2jQ8s/default.jpg)](https://www.youtube.com/watch?v=YQn5Gf2jQ8s)


## Structure of repo

The directory [stock_data] contains the stock data on the S&P 500 companies.
The directory [me_output] contains the data obtained from using the IEX API to perform major events analysis.

#### Data files:
[stock_data]:
The data in this file were collected using webscraping techniques from Wikipedia and the IEX Fianance API, which is one of the top global sources of financial data and news for stocks. We navigated the Wikipedia webste and collected data about company names and stock ticker symbols that was nested within different HTML and react tags, which made the collection process difficult. We specifically scraped the list of S&P500 Stocks on Wikipedia, and we removed those stocks that did not have active data. This sample is comparably small when taking into account the number of total US stocks, but it is more likely to be representative of the stocks that most investors would choose to invest in. After obtaining the list of stock names and symbols, we used the IEX Finance API to obtain more detailed financial information, such as price history and detailed returns.

Each datapoint has the following keys and values:

```
'company name': the name of the company
'stock symbol': the stock ticker symbol for the company
'price': the current price per share of the company stock
'mean_return': the average daily return of the stock over the given time period
'annualized_mean_return': the average daily return of the stock over the given time period, annualized
'annualized_risk': the annualized standard deviation of daily returns
'beta': the beta of the stock
```

[me_output]:
The data in this file is related to the price changes of stocks surrounding the certain date of a major event, which we chose to be 2020-11-03. This was the day of the US election and we believe this major event could have impacted stock prices in a significant manner. 

Each datapoint has the following keys and values:

```
"date": the date of the data, which is sequential from the date of the major event,
"expected_return": the expected return of the stock on that day
"abnormal_return": the percentage of returns that were abnormal
```
#### Data format:
The data is stored in a JSON format, with each line representing a single company's data. The data is structured as follows:
```
{
    "company name": string,
    "stock symbol": string,
    "price": float,
    "mean_return": float,
    "annualized_mean_return": float,
    "annualized_risk": float,
    "beta": float
}
```
```
{
    "date": string,
    "expected_return": float
    "abnormal_return": float
}
```

For string-based values, the default value is NULL and for float-based values, the default value id 0. 
## Data Quality

The data is sourced from webscraping, so there may be occasional missing or inaccurate data points. It is also important to note that the data may not be up-to-date and may not reflect the current state of the stock market. We checked for cleanliness by running through cell values and seeing if there are any blank data values for each stock, since not all stocks will have financial data on the dates that we looked at. In the data we scraped, there were no missing values, but as mentioned above, since some stocks did not have active data, we simply removed them from the database for compatibility. For the time being, we haven’t seen any issues with our scraper since we are able to capture the data properly. 

## License

The data in these files is for personal and educational use only. Redistribution or commercial use of the data is strictly prohibited.

## Questions

##### 1. How many data points are there in total? How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)? Aim for a resource of reasonable size. At least 500 records after cleaning and duplicate removal. Account that part of your data should be used for validation of your results only. Do you think this is enough data to perform your analysis later on?

There are a total of 502 data points after cleaning and duplicate removal for [stock_data] and there are 43 data points for each stock in our analysis list in [me_output] because we analyze 43 days around the major event. The data is divided into individual records for each stock, with each record containing multiple data points for various financial metrics. We did not divide the data into positive/negative examples or any other groups, as our analysis focuses on understanding the relationships between different financial metrics and how they relate to a stock's overall performance. We believe that 502 data points is a reasonable size for our analysis, given the scope of our project, since we are additionally analyzing the price history of each stock within a range of dates and adding additonal data points. 

##### 2. What are the identifying attributes?
The identifying attributes in our dataset include the name of each stock, the date of the financial metric, and the values for various financial metrics such as the opening price, closing price, and volume.

##### 3. Where is the data from?
The data was collected by scraping the Investing.com website and joining the data with more data points from the IEX Cloud API. Both of these sources are reputable and widely recognized as reliable sources for financial data.

##### 4. How did you collect your data?
We collected the data by using web scraping techniques to gather data from the Investing.com website and then joined that data with more data points from the IEX Cloud API.

##### 5. Is the source reputable?
Both Investing.com and IEX Cloud API are widely recognized as reputable sources for financial data. Investing.com is one of the top global sources of financial data and news for stocks, and IEX Cloud API provides high-quality financial data to some of the largest financial institutions in the world.

##### 6. How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?
We generated the sample by taking all of the stocks that had data from our webscraping results from scraping the list of 50 most active stocks on Investing.com. Some stocks did not have active data and we removed them from our dataset. This sample is comparably small when taking into account the number of total US stocks, but it is more likely to be representative of the stocks that most investors would choose to invest in. 

##### 7. Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)
One consideration we took into account when collecting our data was the need to scrape data from the website that was nested within different HTML and react tags, which made the collection process difficult. We looked into using Selenium to help us with this process.

##### 8. How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? (Each team will have to go about answering this question differently but use the following questions as a guide. Graphs and tables are highly encouraged if they allow you to answer these questions more succinctly.)How did you check for the cleanliness of your data? What was your threshold reference?
We checked for cleanliness by running through cell values and seeing if there were any blank data values for each stock, since not all stocks will have financial data in the dates that we looked at. We removed non-active stocks from the dataset. Overall, the data is relatively clean and contains the necessary information to complete our project. However, we may need to do some additional cleaning and pre-processing before conducting our analysis, such as removing outliers and normalizing the data.

##### 9. Did you implement any mechanism to clean your data? If so, what did you do?
We implemented a mechanism to clean our data by removing non-active stocks from the dataset and running through cell values to remove any blank data values.

##### 10. Are there missing values? Do these occur in fields that are important for your project's goals?
There were no missing values in the data that we scraped, but some stocks did not have active data. Therefore, we simply removed them from the dataset for compatibility.

##### 11. Are there duplicates? Do these occur in fields that are important for your project's goals?
There were no duplicates in the dataset since the list of most active stocks only contains unique stocks.

