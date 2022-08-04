import requests
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=8S58BDY13J9J9NK1'
r = requests.get(url)
data = r.json()
print(data)
exchange_rate=data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
