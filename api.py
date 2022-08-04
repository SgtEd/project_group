import requests
import math
from decimal import Decimal

def getData():
    print("Getting exchange rate..")

    # declare url link
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=8S58BDY13J9J9NK1'

    # get the data
    r = requests.get(url)

    # open data
    data = r.json()


    # print(data)

    # access the Exchange Rate from the data
    exchange_rate = Decimal(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    roundedOffExchangeRate = round(exchange_rate, 8)

    return roundedOffExchangeRate

