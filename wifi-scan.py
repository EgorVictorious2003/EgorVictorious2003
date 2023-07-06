import pywifi
import time

try:
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2.0)
    results = iface.scan_results()
    
    for i in results:
        print("WiFi--Scanner")
        print()
        bssid = i.bssid
        ssid = i.ssid
        key = i.key
        auth = i.auth
        cipher = i.cipher
        print(f"BSSID: {bssid}| SSID: {ssid}| Key: {key}| Аутентификация: {auth}| Шифрование: {cipher}")
        input('Для выхода нажмите Ctrl + C ')

except KeyboardInterrupt:
    print("GoodBye")
