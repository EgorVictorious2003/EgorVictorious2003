import requests
from pyfiglet import Figlet

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url = f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Провайдер]': response.get('isp'),
            '[Организация]': response.get('org'),
            '[Страна]': response.get('country'),
            '[Регион]': response.get('regionName'),
            '[Город]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Широта]': response.get('lat'),
            '[Долгота]': response.get('lon'),
        }
       
        for k, v in data.items():
            print(f' {k}, : {v}')

    except requests.exceptions.ConnectionError:
        print('[!]Пожалуйста проверьте подключение!')

def main():
    print('<<-[ IP_Поиск ]->>')
    ip = input('Пожалуйста введите целевой сайт или IP: ')
    get_info_by_ip(ip = ip)

if __name__ == '__main__':
    main()