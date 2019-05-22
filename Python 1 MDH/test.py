import requests
stad = str(input("Skriv in valfri stad av Stockholm Göteborg Malmö Uppsala Västerås för väderinformation: "))

url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/' + stad

r = requests.get(url)
platser = r.json()


print(platser)