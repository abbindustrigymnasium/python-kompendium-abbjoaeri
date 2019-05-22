#övningsuppgifter 8.2

# #8.1

# distanskm = input("Ange distans (i km): ") # variabeln distanskm som en text input

# def km_to_miles(distanskm): # funktionen som omvandlar
#     return str(int(distanskm) * 1.609344) +  # multiplierar med 1 mile för att genomföra det
# print( "Din distans motsvarar " + str(miles_to_km(distanskm)) + " miles") # skriver ut vad distansen motsvarar i miles.

# distansmiles = input("Ange distans (i miles): ")

# def miles_to_km(distansmiles):
#     return str(int(distansmiles) * 0.62) 
# print( "Din distans motsvarar " + str(km_to_miles(distansmiles)) + " km")


#8.2

url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/stockholm'
r = requests.get(url)
response_dictionary = r.json()

def get(url):
    