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
mas = []
for price in get_price(currency_symbol=False):
    if price < 30:
        mas.append(price)
print(mas)
