# python currency_calculator.py USD 2023.06.24


import requests
import sys 
import dateutil.parser
from datetime import timedelta, datetime


print('Kalkulator Walutowy')


#   Waluta USD EUR....
try:
    currency = sys.argv[1]
except IndexError:
    print('Prosze wpisać skrót waluty USD, EUR, GBP, itd...')
    currency = input('Proszę podaj walutę: ')
currency = currency.upper()


#   Data
try:
    str_date = sys.argv[2]
except IndexError:
    str_date = input('Proszę podać datę:(yyyy.mm.dd) ')


#   Modyfikacja daty na stringa
try:
    date = dateutil.parser.parse(str_date)
except ValueError:
    print('Invalid date')
    sys.exit(1)

url_date = date.strftime('%Y-%m-%d')


#   URL API
URL = f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{url_date}/?format=json'



#   błąd 404
total = 0
day = timedelta(days=1)
response = requests.get(URL)
while response.status_code == 404:
    print(url_date, 'No date')
    url_date = datetime.strptime(url_date, '%Y-%m-%d') - day
    url_date = url_date.strftime('%Y-%m-%d')
    URL = f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{url_date}/?format=json'
    response = requests.get(URL)
    if total == 20:
        sys.exit(2)
    total += 1
if not response.ok:
    print('Unexpected server response')
    sys.exit(3)


#   Dostajemy się do kursu waluty którą podaliśmy
json = response.json()
try:
    rate = json['rates'][0]['mid']
except (ValueError, KeyError):
    print('Invalid server response')
    sys.exit(4)


print(f'1 {currency} = {rate} PLN w dniu {url_date[8:10]}/{url_date[5:7]}/{url_date[:4]}')




