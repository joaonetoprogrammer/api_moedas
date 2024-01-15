import requests 
import json
import matplotlib.pyplot as plt

cot_bitcoin = requests.get("https://economia.awesomeapi.com.br/json/daily/BTC-BRL/200?start_date=20231201&end_date=20240114")
cot_bitcoin_dict = cot_bitcoin.json()

list_bt = [float(i['bid']) for i in cot_bitcoin_dict]
list_bt.reverse()

plt.figure(figsize=(15,5))
plt.plot(list_bt)
plt.show()