
import requests 
import json


x = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')


requisicao_dic =  json.loads(x.text)

print(type(requisicao_dic))
print(requisicao_dic)
