import requests 
import json

#site com api para buscar moedas
cot = requests.get("https://economia.awesomeapi.com.br/json/all")

# transformando json em um dicionario python
cot_dict = cot.json()

print(cot_dict)