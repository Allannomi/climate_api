import requests
import json
import os
#função que le o .env
from dotenv import load_dotenv 
 
#carrega as variaveis do .env
load_dotenv() 

#api key pega no site
url = "https://api.openweathermap.org/data/2.5/weather"

#pega a variavel do .env
API_KEY = os.getenv("key_api")

#"q" cidade
#"appid" api key 
# "units": metric é apra definir para celsios

#parametros para ir pra url e buscar esseas informações
parametros = {
    "q": "sao paulo",
    "appid": API_KEY,
    "units": "metric",
    "lang": "pt-br"
}
#colcoar os parametros direto no get, invez de colocar na url, mais limpo
response = requests.get(url, params=parametros)

#se da certo
if response.status_code == 200:
    #transforma o json em dicionario
    dados = response.json()
    # ??
    resultado = {
        "cidade": dados["name"],
        "temperatura": dados["main"]["temp"],
         "descrição": dados["weather"][0]["description"]
    }
    #adicionar em um arquivo json
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(resultado, arquivo, indent=4, ensure_ascii=False)
    print("dados salvo em json")
else:
     # response.status mostra como está o status
    print("Status:", response.status_code)
    # mostra oq tem de erro
    print("Raw body:", response.text[:200])

    print("ocorreu um erro")