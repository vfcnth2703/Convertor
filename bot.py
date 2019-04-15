import pyodbc
from var_dump import var_dump
from geopy.geocoders import Yandex
from pprint import pprint

source_address = 'Московская обл, г. Химки, ул Кирова д.3,стр.3'
geolocator = Yandex(lang='ru_RU', user_agent='Telegram_bot')

yan = Yandex()
y = yan.geocode(source_address, exactly_one=False, timeout=1)

conn = pyodbc.connect('Driver={SQL Server Native Client 10.0};Server=GT\\SQL2008;Database=ASCNDB;UID=sa;PWD=Qwe1@#rty')

print(f'Исходный адрес  = {source_address}')
print(f'Адрес = {y[0].address}, Широта = {y[0].latitude}, Долгота = {y[0].longitude}')
print('Read')
# print(y[0].address)
# print(y[0].latitude)
var_dump(y[0].raw)

cursor = conn.cursor()
rows = cursor.execute('select top 10 a.Adress_ID, a.OfficialAdress from dbo.ascn_adresses a order by a.Adress_ID desc')
# for row in rows:
# print(row.Adress_ID, row.OfficialAdress)


conn.close
