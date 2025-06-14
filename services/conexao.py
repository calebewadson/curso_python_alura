import requests
import json
import os

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

pasta_destino = 'data'
os.makedirs(pasta_destino, exist_ok=True)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            'Item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
else:
    print(f'O erro foi {response.status_code}')


for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    caminho = os.path.join(pasta_destino, nome_do_arquivo)
    with open(caminho, 'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent=4)