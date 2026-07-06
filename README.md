# 🚗 Projeto de Web Scraping da OLX 🚗
## 🧠 Visão Geral do Projeto
O Projeto de Web Scraping é um script desenvolvido em Python para extrair dados do site da OLX. O script tem como objetivo coletar dados sobre carros, vans e veículos utilitários à venda na região de Belo Horizonte, Brasil. A finalidade deste script é reunir dados para possíveis análises, monitoramento ou outras aplicações de inteligência de negócios. O projeto utiliza bibliotecas populares como `BeautifulSoup` e `requests` para web scraping e requisições HTTP, respectivamente.

## 🚀 Principais Funcionalidades
* Extrai dados do site da OLX, incluindo títulos dos anúncios, preços, links para as páginas individuais dos veículos e localizações
* Itera sobre um número especificado de páginas para coletar dados
* Armazena os dados extraídos em formato JSON para facilitar a análise ou a integração com outras ferramentas
* Utiliza as bibliotecas `BeautifulSoup` e `requests` para web scraping e requisições HTTP
* Possibilidade de integração com ferramentas de armazenamento, processamento ou visualização de dados

## 🛠️ Stack Tecnológica
* Biblioteca `BeautifulSoup` para análise de conteúdo HTML e extração de dados
* Biblioteca `requests` para realizar requisições HTTP
* Biblioteca `pandas` para manipulação e análise de dados
* Biblioteca `numpy` para cálculos numéricos
* Biblioteca `selenium` para tarefas de web scraping mais complexas
* Biblioteca `json` para manipulação de dados JSON
* Biblioteca `difflib` para calcular semelhanças entre strings
* Biblioteca `re` para correspondência de padrões com expressões regulares

## 📦 Instalação
Para começar a usar o projeto, siga estes passos:
### Pré-requisitos
* Python instalado no seu sistema
* Bibliotecas necessárias instaladas (`BeautifulSoup`, `requests`, `pandas`, `numpy`, `selenium`, `json`, `difflib`, `re`)
### Instalação
* Clone o repositório usando `git clone`
### Execução local
* Execute o script usando `python app.py`

## 💻 Uso
Para utilizar o script, basta executar `python app.py` no seu terminal. O script percorrerá o número especificado de páginas (padrão: 62) e extrairá dados do site da OLX. Os dados extraídos serão armazenados no formato JSON.

## 📂 Estrutura do Projeto
```markdown
.
├── app.py
├── README.md
└── data
    ├── json
    └── csv
```
