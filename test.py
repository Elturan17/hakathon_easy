import requests 
from bs4 import BeautifulSoup
import csv



def write_to_csv(data):
    with open('nout.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price'], data['image']])  

def get_html(url):
    '''возвращать html код страницы'''
    response = requests.get(url) 
    return response.text

def get_total_pages(html):
    soup = BeautifulSoup(html,'lxml')
    pages = int(soup.find('span', class_ = 'vm-page-counter').text.split()[-1])
    return pages

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    product_list = soup.find_all('div', class_='row')

    for product in product_list:
        title = product.find('span', class_='prouct_name').text
        price = product.find('span', class_='price').text
        image = 'https://enter.kg/' + product.find('img').get('src')
        image = 'https://enter.kg/' + product.find('img').get('src')


        dict_ = {'title':title, 'price':price, 'image':image}
        write_to_csv(dict_) 


def main():
    notebooks_url = 'https://enter.kg/computers/noutbuki_bishkek'
    pages = '?page='
    html = get_html(notebooks_url)
    number = get_total_pages(html) 
    for i in range(1,number+1):
        print(i)
        if i == 1:
            url = 'https://enter.kg/computers/noutbuki_bishkek'
        else:
            url = 'https://enter.kg/computers/noutbuki_bishkek' +f'/results,{(i-1)*100+1}-{(i-1)*100}'
        get_html(url)       

        get_data(html) 

with open('nout.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'price', 'image']) 



main()


