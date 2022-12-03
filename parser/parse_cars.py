import requests
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup as bs

URL = 'https://turbo.kg/'

HEADERS = { 
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
}

@csrf_exempt
def get_html(url,params=''):
    req = requests.get(url,headers=HEADERS)
    return req

@csrf_exempt
def get_data(html):
    soup = bs(html,'html.parser')
    items = soup.find_all('div', class_ = 'car')
    cars = []

    for item in items:
        cars.append(
            {
            'year': item.find('p', class_ = "mb-1").find('b',class_=None).get_text(),
            'price': item.find('p', class_ = "mb-1").find('b',class_="float-right").get_text(),
            'car_model': item.find('a',class_="card-body").find('h3',class_="mb-1").get_text(),
            'image': item.find('a',class_="d-block").find('img').get('src')
            }
        )
    return cars

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        html = get_html(URL)
        # with open('parse.html','w',encoding="UTF-8") as file:
        #     file.write(html.text)
        cars.extend(get_data(html.text))
        return cars
    else:
        raise Exception('Error in parser')