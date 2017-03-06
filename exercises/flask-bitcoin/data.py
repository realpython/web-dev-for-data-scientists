import sqlite3
import requests


def get_rates():
    results = {}
    btc = requests.get('https://btc-e.com/api/3/ticker/btc_usd')
    results['btc'] = btc.json()['btc_usd']['buy']
    kraken = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
    results['kraken'] = float(kraken.json()['result']['XXBTZUSD']['b'][0])
    bittrex = requests.get(
        'https://bittrex.com/api/v1.1/public/getticker?market=usdt-btc')
    results['bittrex'] = bittrex.json()['result']['Bid']
    return results


def get_lowest_rate(rates):
    min_value = float('inf')
    new_rates = []
    for key, value in rates.items():
        new = {'currency': key, 'price': value, 'lowest': False}
        if value <= min_value:
            min_value = value
            new['lowest'] = True
        new_rates.append(new)
    return new_rates


def add_data(data):
    print(data)
    with sqlite3.connect('bitcoin.db') as connection:
        c = connection.cursor()
        for key, value in data.items():
            values = [key, value]
            c.execute('INSERT INTO rates (currency, price) VALUES(?, ?)',
                      values)
