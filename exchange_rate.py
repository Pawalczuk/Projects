# python exchange_rate.py USD 2022.08.18


import requests
import sys 
import dateutil.parser


print('Kalkulator Walutowy')


try:
    currency = sys.argv[1]
except IndexError:
    print('Prosze wpisać skrót waluty USD, EUR, GBP, itd...')
    currency = input('Proszę podaj walutę: ')
currency = currency.upper()


try:
    str_date = sys.argv[2]
except IndexError:
    str_date = input('Proszę podać datę:(yyyy.mm.dd) ')


try:
    date = dateutil.parser.parse(str_date)
except ValueError:
    print('Invalid date')
    sys.exit(1)


url_date = date.strftime('%Y-%m-%d')
URL = f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{url_date}/?format=json'


response = requests.get(URL)
if response.status_code == 404:
    print('No date')
    sys.exit(2)
if not response.ok:
    print('Unexpected server response')
    sys.exit(3)


json = response.json()
try:
    rate = json['rates'][0]['mid']
except (ValueError, KeyError):
    print('Invalid server response')
    sys.exit(4)


print(f'1 {currency} = {rate} PLN w dniu {date.day}/{date.month}/{date.year}')

















