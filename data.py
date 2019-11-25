

import requests
from bs4 import BeautifulSoup

req = requests.get('http://bewakoof.com/desi-collection/')


soup  = BeautifulSoup(req.content, 'html.parser')


fp = open('file_name.csv', 'w')
fp.write('t-shirt name , price , image\n')

    
for product in soup.find_all('div' , {'class' : 'productCardBox'} ):
    # print(product details)
    for detail in product.find_all('div', {'class' : 'productCardDetail'}):
        
        fp.write(str(detail.find_all('h3')[0].text))
        fp.write(',')
        fp.write(str(detail.find_all('b')[1].text))
        fp.write(',')
    for img in product.find_all('div', {'class' : 'productCardImg'}):
        div = next(iter(img.children))
        for img in div.find_all('img'):
             fp.write(img['src'])

    fp.write('\n')
   