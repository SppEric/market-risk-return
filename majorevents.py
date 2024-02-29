import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

def get_stock_data(symbol: str, start_date: str, end_date: str):
    api_token = 'pk_a37a60c3938f4dc89f3eb95ca16e6e53'
    base_url = 'https://cloud.iexapis.com/stable'
    endpoint = f'/stock/{symbol}/chart/5y?token={api_token}'


    response = requests.get(base_url + endpoint)
    data = json.loads(response.text)

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    mask = (df['date'] >= start_date) & (df['date'] <= end_date)
    filtered_data = df.loc[mask]

    return filtered_data


def get_risk_free_rate():
    return 0.02

# def create_presets():
# #Preset parameters for search
#     date_str = '2020-11-03'
#     event_date = pd.to_datetime(date_str) #US Presidential Election
#     window_size = 30
#     market_symbol ='SPY'
#     start_date = (event_date - pd.DateOffset(days=window_size)).strftime('%Y-%m-%d')
#     end_date = (event_date + pd.DateOffset(days=window_size)).strftime('%Y-%m-%d')
#     market_df = get_stock_data(market_symbol)
#     market_df = df.loc[mask]
#     if market_df.empty:
#         print(f"No data available for {symbol} in the given date range")
#         return None
#     df = pd.DataFrame(market_df)
#     df['date'] = pd.to_datetime(df['date'])
#     mask = (df['date'] >= start_date) & (df['date'] <= end_date)
#     market_df = df.loc[mask]


def event_study(stock_symbol: str, market_symbol: str, event_date: str, window_size: int):
    event_date = pd.to_datetime(event_date)
    start_date = (event_date - pd.DateOffset(days=window_size)).strftime('%Y-%m-%d')
    end_date = (event_date + pd.DateOffset(days=window_size)).strftime('%Y-%m-%d')

    stock_df = get_stock_data(stock_symbol, start_date, end_date)
    market_df = get_stock_data(market_symbol, start_date, end_date)

    stock_df.set_index('date', inplace=True)
    market_df.set_index('date', inplace=True)

    stock_df['stock_return'] = stock_df['close'].pct_change()
    market_df['market_return'] = market_df['close'].pct_change()

    risk_free_rate = get_risk_free_rate() / 252

    stock_df['excess_return'] = stock_df['stock_return'] - risk_free_rate
    market_df['excess_return'] = market_df['market_return'] - risk_free_rate

    X = market_df['excess_return'].iloc[1:]
    y = stock_df['excess_return'].iloc[1:]
    beta = stats.linregress(X, y).slope

    stock_df['expected_return'] = risk_free_rate + beta * market_df['excess_return']
    stock_df['abnormal_return'] = stock_df['excess_return'] - stock_df['expected_return']

    # plt.figure(figsize=(10, 6))
    # plt.plot(stock_df['abnormal_return'], label='Abnormal Return', marker='o')
    # plt.axhline(0, color='gray', linestyle='--')
    # plt.axvline(event_date, color='red', linestyle='--', label='Event Date')
    # plt.legend()
    # plt.title('Abnormal Returns')
    # plt.xlabel('Date')
    # plt.ylabel('Abnormal Return')
    # plt.xticks(rotation=45)
    # plt.grid()
    # plt.show()

    # extract abnormal return and expected return for event date
    data = []
    for i in range(len(stock_df)):
        data.append({
            'date': str(stock_df.index[i]),
            'expected_return': float(stock_df['expected_return'][i]),
            'abnormal_return': float(stock_df['abnormal_return'][i])
        })

    return {
        'symbol': stock_symbol,
        'data': data
    }


response = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df2 = pd.read_html(response.text)[0]
symbols = list(df2['Symbol'])
#print(symbols)


result = event_study('AAPL', 'SPY', '2020-11-03', 30)


with open('me_output.json', 'w') as f:
    json.dump(result, f, indent=4)

print('Data written to me_output.json')