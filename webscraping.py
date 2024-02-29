import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import seaborn as sns

MIN_TRADING_DAYS = 252

def get_stock_data(symbol):
    api_key = 'pk_a37a60c3938f4dc89f3eb95ca16e6e53'
    url = f'https://cloud.iexapis.com/stable/stock/{symbol}/chart/max?token={api_key}&chartLast=253'
    response = requests.get(url)
    while response.status_code == 429:  # Too Many Requests error
        print(f"Too many requests for {symbol}. Waiting for 0.3 seconds...")
        time.sleep(0.3)
        response = requests.get(url)
    if response.status_code != 200:
        print(f"Error retrieving data for {symbol}: {response.status_code}")
        return None
    return response.json()

market_data = get_stock_data('SPY')

def analyze_stock_data(data: list):
    if len(data) < 253:
        return None
    
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])

    df['daily_return'] = df['close'].pct_change()

    mean_return = df['daily_return'].mean()
    std_dev = df['daily_return'].std()

    annualized_mean_return = ((1 + mean_return) ** 252) - 1
    annualized_risk = std_dev * np.sqrt(252)

    market_df = pd.DataFrame(market_data)
    market_df['date'] = pd.to_datetime(market_df['date'])
    market_df['daily_return'] = market_df['close'].pct_change()

    covariance_matrix = np.cov(df['daily_return'][1:], market_df['daily_return'][1:])
    beta = covariance_matrix[0, 1] / covariance_matrix[1, 1]

    return mean_return, annualized_mean_return, annualized_risk, beta

def plot_stock_data(data: list):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    plt.figure(figsize=(10, 6))
    plt.plot(df['close'])
    plt.title('Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid()
    plt.show()

response = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = pd.read_html(response.text)[0]
symbols = list(df['Symbol'])
names = list(df['Security'])


data = {} # Dictionary to store results for each stock

for symbol in symbols:
    stock_data = get_stock_data(symbol)
    result = analyze_stock_data(stock_data)
    if not isinstance(result, tuple):
        continue
    mean_return, annualized_mean_return, annualized_risk, beta = result
    price = stock_data[-1]['close']

    data[symbol] = {
    'company name': names[symbols.index(symbol)],
    'stock symbol': symbol,
    'price': price,
    'mean_return': mean_return,
    'annualized_mean_return': annualized_mean_return,
    'annualized_risk': annualized_risk,
    'beta': beta
}

with open('stock_data.json', 'w') as f:
    json.dump(data, f)

print('Data written to stock_data.json')
