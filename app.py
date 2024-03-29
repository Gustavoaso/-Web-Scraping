import pandas as pd
import numpy as np
import requests 
from bs4 import BeautifulSoup
import json 
from difflib import SequenceMatcher
from selenium import webdriver 
import time
from datetime import date
import re
from datetime import datetime


listaJson = []

def buscarDadosOlx(pages = 62, regiao = "MG"):
    regiaoBuscar = {"MG": "belo-horizonte-e-regiao" }
    prefix  = {"MG":"estado-mg"}
    for x in range(pages):
        print("LOOP NUMERO:" + str(x))

     
        url = "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/" + prefix[regiao] + "/" +regiaoBuscar[regiao] + "/grande-belo-horizonte/betim" 
        if x == 0:
            print("somente a primeira pagina")
        else:
            url = "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/" + prefix[regiao] + "/" +regiaoBuscar[regiao]+ "/grande-belo-horizonte/betim" + "?o="+str(x)+""
            
        print(url)

        PARAMS = { 

                    "authority":"www.olx.com.br",
                    "method": "get",
                    "path": "/autos-e-pecas/carros-vans-e-utilitarios/estado-mg/belo-horizonte-e-regiao",
                    "scheme":"https" ,
                    "referer": "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios",
                    "sec-fecth-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fecth-user":"?1",
                    "upgrade-insecure-request":"1",
                    "user-agent": 'Mozilla/5.0(Windoes NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.394 Safari/537.36',

                 }
        
        page = requests.get(url = url, headers = PARAMS)
        print(page)
        soup = BeautifulSoup(page.content,'lxml')
        results = soup.find_all('h2', class_= "olx-text olx-text--title-small olx-text--block olx-ad-card__title olx-ad-card__title--vertical")
        prices = soup.find_all("h3",class_= "olx-text olx-text--body-large olx-text--block olx-text--semibold olx-ad-card__price")
        links = soup.find_all( "a", class_ = "olx-ad-card__title-link")
        locais = soup.find_all('p', class_= "olx-text olx-text--caption olx-text--block olx-text--regular")
        
        
       
       
        for result,price,link,local in zip(results,prices,links,locais): 

            pageCar = requests.get(url = link['href'], headers = PARAMS)
            soupCar = BeautifulSoup(pageCar.content,'lxml')
            car = soupCar.find_all('div',  class_ = 'olx-d-flex olx-ml-2 olx-ai-baseline olx-fd-column')
          
            json = { "nomeVeiculo" : result.text,
                     "preçoVeiculo": price.text,
                     "linkAnuncio" : link['href'],
                     "LocalVeiculo" : local.text,         
                    }
            

             
            for div in car:
                
             spans = div.find_all('span', {'data-ds-component': 'DS-Text'})

             
             if spans[0].text == "Quilometragem":
                    json.update({"Quilometragem": spans[1].text})

             elif spans[0].text == "Ano":
                      ano = div.find('a',{'data-ds-component':"DS-Link"})
                      json.update({"Ano": ano.text})

             elif spans[0].text == "Cor":
                     json.update({"Cor": spans[1].text})

            listaJson.append(json)


buscarDadosOlx()
time = datetime.now().strftime("%Y%m%d_%H%M%S")
nome = f"veiculos_{time}.xlsx"
df  = pd.DataFrame(listaJson)
df.to_excel(fr'C:\Users\gtvan\OneDrive\Área de Trabalho\Veiculos\{nome}',nome, engine = 'xlsxwriter' )