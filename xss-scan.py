import requests
import re
from colorama import Fore

# Prompt user for target URL and custom payloads
url = input("Введите целевой URL: ")
custom_payloads = input("Введите пользовательские полезные нагрузки (через запятую): ").split(",")

# Define regex pattern to match potential XSS vulnerabilities in response body
xss_pattern = re.compile(r"<script>.*?</script>")

# Send GET request to target URL and search response body for potential XSS vulnerabilities
try:
    response = requests.get(url)
    matches = re.findall(xss_pattern, response.text)
except requests.exceptions.RequestException as e:
    print("Ошибка: Возможно защищено!", e)
    exit()

# Check for potential XSS vulnerabilities in response body
if len(matches) > 0:
    print("Обнаружены потенциальные XSS-уязвимости:")
for match in matches:
    print(match)
else:
    print("Потенциальные XSS-уязвимости не обнаружены.")

# Check for potential XSS vulnerabilities using custom payloads
if len(custom_payloads) > 0:
    print("Поиск потенциальных XSS-уязвимостей с использованием пользовательских полезных нагрузок...")
for payload in custom_payloads:
    # Replace placeholder with custom payload and send GET request to target URL
    test_url = url.replace("INJECT_HERE", payload)
    try:
        test_response = requests.get(test_url)
        test_matches = re.findall(xss_pattern, test_response.text)
    except requests.exceptions.RequestException as e:
        print("Ошибка: ", e)
        continue
# Check for potential XSS vulnerabilities in response body
if len(test_matches) > 0:
    print("Обнаружена потенциальная XSS-уязвимость с использованием полезной нагрузки:", payload)
for match in test_matches:
    print(match)
else:
    print("Потенциальные уязвимости XSS с использованием полезной нагрузки не обнаружены:", payload)