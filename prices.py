import requests


def get_prices_gdax():
    '''
    Gets the top 50 open orders for the specified product.
    '''
    url = 'https://api.gdax.com/products/BTC-GBP/book?level=2'
    response = requests.get(url).json()
    return response
