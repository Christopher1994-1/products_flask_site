import os 
import requests


# api_key = os.environ.get('twelvedata_secretkey')

# print(api_key)


ticker = "NLY"
api_key = os.environ.get('twelvedata_secretkey')
# # get stock price
# def get_stock_price(ticker, api):
#     url = f"https://api.twelvedata.com/price?symbol={ticker}&apikey={api}&source=docs"
#     response = requests.get(url).json()
#     return response



# stock_price = get_stock_price(ticker, api_key)['price'][:-3]

print(api_key)