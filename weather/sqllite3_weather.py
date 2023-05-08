from requests import get
import sqlite3
from sys import argv
# python dane_pogodowe.db setup  -  create file dane_pogodowe.db


def setup():
    with sqlite3.connect('DoKodu/M07_M08/dane_pogodowe.db') as db:
        sql = '''CREATE TABLE weather(
        weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_pomiaru TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        nazwa_stacji TEXT NOT NULL,
        temperatura REAL NOT NULL,
        ciśnienie REAL NOT NULL
        )'''
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()


if len(argv) == 2 and argv[1] == 'setup':
    setup()


url = 'https://danepubliczne.imgw.pl/api/data/synop'
response = get(url)
data = response.json()


weather_station = input('Podaj stację pogodową, która ciebie interesuje: ')
check = True
for rate in data:
    if rate['stacja'] == weather_station:
        with sqlite3.connect('DoKodu/M07_M08/dane_pogodowe.db') as db:
            sql = '''INSERT INTO weather(data_pomiaru, nazwa_stacji, temperatura, ciśnienie) VALUES(?,?,?,?)'''
            cursor = db.cursor()
            cursor.execute(sql, (rate['data_pomiaru'], rate['stacja'], rate['temperatura'], rate['cisnienie']))
            db.commit()
            check = False
if check:
    print('Brak stacji o którą pytasz')


with sqlite3.connect('DoKodu/M07_M08/dane_pogodowe.db') as db:
    cursor = db.cursor()
    print('ID | DATA POMIARU | NAZWA STACJI | TEMPERATURA | CIŚNIENIE')
    for data in cursor.execute('SELECT * FROM weather'):
        print(f'{data[0]}. | {data[1]:12} | {data[2]:12} | {data[3]:9}{chr(176)}C | {data[4]} ')

