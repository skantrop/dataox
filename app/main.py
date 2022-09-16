from datetime import datetime
import requests
from bs4 import BeautifulSoup
from db_config import psql_db
from db.models import Ads

MAIN_URL = 'https://www.kijiji.ca'

def get_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'lxml')

def get_next_page(url):
    soup = get_page(url)
    if soup.find('a', {'title':'Next'}):
        return soup.find('a', {'title':'Next'}).get("href")

def get_data_from_ads(soup:BeautifulSoup):
    ads = soup.find_all('div', {'class':'search-item'})
    for ad in ads:
        try:
            image = ad.find('picture').find('img').get("data-src")
        except:
            image = ''
        title = ad.find('a', {'class':'title'}).text.strip()
        desc = ' '.join(ad.find('div', {'class':'description'}).text.split())
        location = ad.find('div', {'class':'location'}).find('span').text.strip()
        try:
            beds = int(ad.find('span', {'class':'bedrooms'}).text.replace(' + Den', '').split(':')[-1])
        except:
            beds = 1
        date = ad.find('span', {'class':'date-posted'}).text
        if 'Yesterday' in date:
            curr = datetime.now()
            date = datetime( curr.year, curr.month, curr.day-1)
        elif 'ago' in date:
            date = datetime.now()
        else:
            dd, mm, yyyy = date.split('/')
            date = datetime(int(yyyy), int(mm), int(dd))
        try:
            price = float(ad.find('div', {'class':'price'}).text.replace('\n', '').strip().replace(',', '').replace('$', ''))
        except:
            price = 0.0
        Ads.create(image=image, title=title, desc=desc, location=location, beds=beds, date=date, price=price)


def main():
    psql_db.create_tables([Ads])
    url = MAIN_URL + '/b-apartments-condos/city-of-toronto/c37l1700273'
    soup = get_page(url)
    next_page = get_next_page(url)
    while next_page:
        get_data_from_ads(soup)
        url = MAIN_URL + next_page
        next_page = get_next_page(url)
        print(url)
        soup = get_page(url)
    get_data_from_ads(soup)
    psql_db.close()

if __name__ == '__main__':
    main()
