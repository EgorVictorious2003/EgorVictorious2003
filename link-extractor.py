from bs4 import BeautifulSoup
from os import system
import requests
import sys

system('cls')

try:
   # задаем URL сайта
   url = input('Введите URL: ')

   # получаем HTML-код страницы
   page = requests.get(url).text

   # создаем объект BeautifulSoup для парсинга HTML-кода
   soup = BeautifulSoup(page, 'html.parser')

   # извлекаем все теги <a> со ссылками
   links = soup.find_all('a')

   # проходим по каждой ссылке и выводим ее адрес
   for link in links:
       print(link.get('href'))

except KeyboardInterrupt:
   print()
   print('Ошибка: Операция прервана пользователем!')
   sys.exit(1)
