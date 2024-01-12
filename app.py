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

def buscarDadosOlx(pages = 1, regiao = "MG"):
    regiaoBuscar = {"MG": "belo-horizonte-e-regiao"}
    prefix  = {"MG":"estado-mg"}
    for x in range(0,pages):
        print("LOOP NUMERO:" + str(x))

     
        url = "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/" + prefix[regiao] + "/" +regiaoBuscar[regiao]
        if x == 0:
            print("somente a primeira pagina")
        else:
            url = "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/" + prefix[regiao] + "/" +regiaoBuscar[regiao]+"?o="+str(x)+""
            
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
       
        num = 1
        for result,price,link in zip(results,prices,links): 
            print(f"{num} {result.text} {price.text} {link['href']} ")
            num +=1
            
   

buscarDadosOlx()
    