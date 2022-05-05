import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

response_redirect = response.history
count_response_redirect = len(response_redirect)
print(f"Количесвто редиректов: {count_response_redirect}")
print(f"Итоговый URL: {response.url}")