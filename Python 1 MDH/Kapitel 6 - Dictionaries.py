# import requests
# stad = input("Skriv in valfri stad av Stockholm Göteborg Malmö Uppsala Västerås för väderinformation: ")

# url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/' + stad

# r = requests.get(url)
# platser = r.json()

# print(platser)

# 
#6.2#test av api i python 6.1.2
# import requests
# url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/stockholm'
# r = requests.get(url)
# response_dictionary = r.json()
# print(response_dictionary)


#övningsuppgifter:

#6.1

# import requests 
# url = 'http://77.238.56.27/examples/numinfo/?integer='+ str(nummer)
# r = requests.get(url)
# faktorer = r.json()
# nummer = str(input("Ange ett positivt heltal: ")
# if nummer %2== 0:
#     print(nummer + " är ett jämt nummer, talet är alltså inte ett primtal ." + "Numrets faktorer är " + faktorer)
# else:
#     print("Talet är inte ett jämt positivt heltal.")

#6.2

# import requests
# stad = str(input("Skriv in valfri stad av Stockholm Göteborg Malmö Uppsala Västerås för väderinformation: "))

# url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/' + stad

# r = requests.get(url)
# platser = r.json()


# print(platser)

# 6.3

import requests #importerar requests
url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/cd822d767d6816e8a720234bc26043a39baf6d4cd' #url som ska användas

r = requests.get(url) # definerar variabeln r
response_dictionary = r.json() # definerar response_dictionary
print(response_dictionary) # skriver ut det vi tidigare definerade

print("  -----ARTISTER-----  ") # skriver ut artister