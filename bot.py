import pyodbc
from var_dump import var_dump
from geopy.geocoders import Yandex
# from geopy.geocoders import Nominatim
import time
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0'
# source_address = 'Московская обл, г. Химки, ул Кирова д.3,стр.3'
# source_address = 'Московская обл, Шатурский р-н, с. Дмитровский Погост, ул Рабочая, д. 2Б'
# source_address = 'Московская обл, Орехово-Зуевский р-н, п. Авсюнино, ул Ленина'
source_address = 'пос. Коммунарка, ул Липовый парк, д.11'

geo = Yandex(lang='ru_RU', user_agent=user_agent)
# geo = Nominatim(user_agent=user_agent)
loc = geo.geocode(source_address, exactly_one=True)._raw
print(loc['Point'])
# print(loc['metaDataProperty']['GeocoderMetaData']['text'])
# loc.append({
#     'kind': 'pos',
#     'name': loc['Point']['pos']
# })
loc['metaDataProperty']['GeocoderMetaData']['Address']['Components'].append(loc['Point'])
var_dump(loc['metaDataProperty']['GeocoderMetaData']['Address']['Components'])


# conn = pyodbc.connect('Driver={SQL Server Native Client 10.0};Server=GT\\SQL2008;Database=ASCNDB;UID=sa;PWD=Qwe1@#rty')

# print(y[0].address)
# print(y[0].latitude)
# var_dump(y[0].raw)
# print(f'Исходный адрес  = {source_address}')
# print(f'Адрес = {y[0].address}, Широта = {y[0].latitude}, Долгота = {y[0].longitude}')
# print('Read')

# cursor = conn.cursor()
# rows = list(cursor.execute('select top 1 a.Adress_ID, a.Adres from dbo.ascn_adresses a order by a.Adress_ID desc'))
# for line in rows:
#     time.sleep(2)
#     print(line.Adres)
# loc = geolocator.geocode(line.Adres, exactly_one=False, timeout=2)[0].raw
# loc_one = geolocator.geocode(line.Adres, exactly_one=True, timeout=2)
# loc_nom = geolocator.geocode(line.Adres)
# address = loc_one.address
# longitude = loc_one.longitude
# latitude = loc_one.latitude
# print(loc_nom)
# print(f'address = {address}')
# print(f'longitude = {longitude}')
# print(f'latitude = {latitude}')
# meta_data = loc['metaDataProperty']['GeocoderMetaData']
# if meta_data['precision'] == 'exact' and meta_data['kind'] == 'house':
#     print('All right')
# else:
#     print('Fail')

# address_detail = loc['metaDataProperty']['GeocoderMetaData']['AddressDetails']
# AddressLine = address_detail['Country']['AddressLine']
# CountryName = address_detail['Country']['CountryName']
# AdministrativeArea = address_detail['Country']['AdministrativeArea']['AdministrativeAreaName']
# Administrative = address_detail['Country']['AdministrativeArea']
# SubAdministrativeAreaName = Administrative['SubAdministrativeArea']['SubAdministrativeAreaName']
# Locality = Administrative['SubAdministrativeArea']['Locality']['LocalityName']
# street_area = Administrative['SubAdministrativeArea']['Locality']
# street = street_area['Thoroughfare']['ThoroughfareName']
# try:
#     house = street_area['Thoroughfare']['Premise']['PremiseNumber']
# except:
#     house = None
# try:
#     postal_code = street_area['Thoroughfare']['Premise']['PostalCode']['PostalCodeNumber']
# except:
#     postal_code = None

# print(f'Адрес = {AddressLine}')
# print(f'Страна = {CountryName}')
# print(f'Административная единица = {AdministrativeArea}')
# print(f'Субадминистративная единица = {SubAdministrativeAreaName}')
# print(f'Населенный пункт = {Locality}')
# print(f'Улица = {street}')
# print(f'Дом = {house}')
# print(f'Индекс = {postal_code}')
# print('-' * 100)

# var_dump(loc['metaDataProperty'])

# conn.close
