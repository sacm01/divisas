import requests
from bs4 import BeautifulSoup as b

def dl():
    url="https://www.xe.com/es/currencyconverter/convert/?Amount=1&From=COP&To=USD"
    html=requests.get(url)
    content=html.content
    soup=b(content,"lxml")
    precio_dolar= soup.find("p",{"class":"result__BigRate-sc-1bsijpp-1 iGrAod"})  
    print(precio_dolar.text)


def eu():
    url="https://www.xe.com/es/currencyconverter/convert/?Amount=1&From=COP&To=EUR"
    html=requests.get(url)
    content=html.content
    soup=b(content,"lxml")
    precio_euro= soup.find("p",{"class":"result__BigRate-sc-1bsijpp-1 iGrAod"})  
    print(precio_euro.text)
    

def GBP():
    url="https://www.xe.com/es/currencyconverter/convert/?Amount=1&From=COP&To=GBP"
    html=requests.get(url)
    content=html.content
    soup=b(content,"lxml")
    precio_libra= soup.find("p",{"class":"result__BigRate-sc-1bsijpp-1 iGrAod"})  
    print(precio_libra.text)


dl()
eu()
GBP()