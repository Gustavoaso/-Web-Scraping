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

def buscarDadosOlx(pages = 2, regiao = "PG"):
    regiaoBuscar = {"PG": "regiao-de-ponta-grossa-e-guarapuava", "CTBA":"regiao-de-curitiba-e-paranagua","SP": "sao-paulo-e-regiao"}
    prefix  = {"PG":"pr","CTBA":"pr","SP":"sp"}
    for x in range(0,pages):
        print("LOOP NUMERO:" + str(x))
        url = "https://" + prefix[regiao]+".olx.com.br/" + regiaoBuscar[regiao]+"/autos-e-pecas/carros-vans-e-utilitarios"
        if x == 0 :
            print("somente a primeira pagina")
        else:
            url = "https://" + prefix[regiao]+".olx.com.br/" + regiaoBuscar[regiao]+"/autos-e-pecas/carros-vans-e-utilitarios?o="+str(x)+""
            
        print(url)

        PARAMS = { 

                    "authority":"pr.olx.com.br",
                    "method": "get",
                    "path": "/regiao-de-ponta-grossa-e-guarapuava/autos-e-pecas/carros-vans-e-utilitarios",
                    "scheme":"https" ,
                    "referer": "https://pr.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios",
                    "sec-fecth-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fecth-user":"?1",
                    "upgrade-insecure-request":"1",
                    "user-agent": 'Mozilla/5.0(Windoes NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.394 Safari/537.36',

                 }
        
        page = requests.get(url = url, headers = PARAMS)
        print(page)
        soup = BeautifulSoup(page.content,'lxml')
        results = soup.find_all("li",{"class":"sc-lfcmfeb-2 ggOGT3"})
        print(results   )

buscarDadosOlx()
    