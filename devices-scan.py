import scapy.all as scapy
import argparse

import time
from colorama import *
from tqdm import tqdm

print('''
-t --target Целевой IP / IP диапазон (devices-scan -t 192.168.1.1/24")
''')

print('Devices-scan 1.3')
try:
    def get_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--target", dest="target", help="Целевой IP/ IP Диапазон")
        options = parser.parse_args()
        return options

    def scan(ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                  11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                  21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
                  31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
        for i in tqdm(mylist):
            time.sleep(1)


        clients_list= []
        for element in answered_list:
            client_dict ={"ip": element[1].psrc, "mac": element[1].hwsrc}
            clients_list.append(client_dict)

        return clients_list


    def print_result(results_list):
        print('-----------------------------------------------------------------')
        print(Fore.GREEN, "IP Адрес\t\t\tMAC Адрес\n-------------------------------------------------------")
        for client in results_list:
            print(Fore.CYAN, client["ip"] + "\t\t" + client["mac"])



    options = get_arguments()
    scan_result = scan(options.target)
    print_result(scan_result)

except KeyboardInterrupt:
    print('GoodBye')
    exit()