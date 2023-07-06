from scapy.all import sniff #основная библиотека программы
import time # время работы программы
from colorama import Fore #Изменение цвета текста

print('DNS-Sniffer __version 0.2__')
print('''
В этой версии изменен цвет текста
''')
start = time.time() # точка отсчёта программы

print()
print(Fore.GREEN + '----[ DNS--Sniffer ]----')
print()

try:
    def packet_sniff(packet):
        qname = packet['DNS Question Record'].qname.decode()
        print(Fore.CYAN + f'Запрос: {qname[0:-1]}')

    def main():
        sniff(filter='dst port 53', count=0, store=False, prn=packet_sniff)

    if __name__ == "__main__":
        main()

except:
    KeyboardInterrupt()
    end = time.time()
    print('Время работы программы', end)
exit()
