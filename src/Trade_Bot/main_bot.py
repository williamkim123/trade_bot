'''
Trade Bot:
Using API to get the data: 1) https://twelvedata.com/
2) Yahoo data
1) Going through Batch request.
'''

import requests
import time



ticker = "TRP"
# interval ='1day'



def get_stock_price(ticker_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&country=Canada&apikey={api}"

    #get a request from this url
    response = requests.get(url).json()

    # Accessing through python
    price = response['price'][:-3]

    return price

    print(price)

def get_stock_quote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&country=Canada&apikey={api}"
    response = requests.get(url).json()
    return response

stock_data = get_stock_quote(ticker, api_key)
stock_price = get_stock_price(ticker, api_key)

# exchange = stock_data['exchange']
# currency = stock_data['currency']
# open = stock_data['open']
# high_price = stock_data['high']
# low_price = stock_price['low']
# close_price = stock_price['close']
# volume = stock_price['volume']
# name = stock_price['name']


print(stock_data, stock_price)