import sqlite3
import requests


def get_rates():
    results = {}
    try:
        bitstamp = requests.get(
            'https://www.bitstamp.net/api/v2/ticker/btcusd/')
        results['bitstamp'] = float(bitstamp.json()['bid'])
        kraken = requests.get(
            'https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        results['kraken'] = float(kraken.json()['result']['XXBTZUSD']['a'][0])
        bittrex = requests.get(
            'https://bittrex.com/api/v1.1/public/getticker?market=usdt-btc')
        results['bittrex'] = bittrex.json()['result']['Bid']
        return results
    except:
        return False


def get_lowest_rate(rates):
    lowest = min(rates, key=rates.get)
    new_rates = []
    for key, value in rates.items():
        new = {'currency': key, 'price': value, 'lowest': False}
        if key == lowest:
            new['lowest'] = True
        new_rates.append(new)
    return new_rates


def add_data(data):
    with sqlite3.connect('bitcoin.db') as connection:
        c = connection.cursor()
        for key, value in data.items():
            values = [key, value]
            c.execute('INSERT INTO rates (currency, price) VALUES(?, ?)',
                      values)
