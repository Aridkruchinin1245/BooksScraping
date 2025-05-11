import requests
import lxml
from bs4 import BeautifulSoup

def get_price(currency_symbol) -> bool:
    '''
    returns prices, if currency_symbol = True return it with extra symbol
    '''
    page=0
    result = []
    while True:
        page+=1
        url=f'https://books.toscrape.com/catalogue/page-{page}.html'
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'lxml')
        cards = soup.find_all('article', class_='product_pod')
        if cards==[]:
            print('pages are finish')
            break
        for card in cards:
            price = card.find('p', class_='price_color').text
            if currency_symbol == True:
                #print(price[1:]) #price with currency symbol
                result.append(price[1:])
            else:
                #print(float(price[2:])) #price without extra symbols
                result.append(float(price[2:]))     
        print('working')    
    return result
def get_data():
    result = []
    a = -1
    page=49
    hrefs = []
    while True:
        page+=1
        url=f'https://books.toscrape.com/catalogue/page-{page}.html'
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'lxml')
        cards = soup.find_all('div', class_="image_container")
        for card in cards:
            hrefs.append('https://books.toscrape.com/catalogue/'+card.find('a')['href'])
        if cards==[]:
            print('pages are finish')
            break
        for href in hrefs:
            a +=1
            result.append([])
            response = requests.get(href).text
            card_data = BeautifulSoup(response, 'lxml')
            name = card_data.find('h1').text
            imgsrc = card_data.find('img')['src']
            img = 'https://books.toscrape.com/'+imgsrc[5:]
            price = float(card_data.find('p', class_='price_color').text[2:])
            description = card_data.find('p', class_='')
            result[a].extend([name,img,price,description])
    return result
get_data()
