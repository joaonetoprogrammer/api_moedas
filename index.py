import requests 
import json

#site com api para buscar moedas
cot = requests.get("https://economia.awesomeapi.com.br/json/all")

# transformando json em um dicionario python
cot_dict = cot.json()
# dicionario inteiro 
print(cot_dict)

# exibindo moedas especificas
dolar = cot_dict['USD']['bid']
euro = cot_dict['EUR']['bid']
print("Dolar: {}" .format(dolar))
print("Euro: {}" .format(euro))

# ultimos 30 dias de valores
dolar_ultimos_30 = requests.get("https://economia.awesomeapi.com.br/json/daily/USD-BRL/30")
cot_d_30_dict = dolar_ultimos_30.json()

list_dolar = [float(i['bid']) for i in cot_d_30_dict]
print(list_dolar)
