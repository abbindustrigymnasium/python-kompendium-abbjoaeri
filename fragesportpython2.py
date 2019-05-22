import random # importerar random
import requests # importera requests

url = "https://opentdb.com/api.php?amount=10&category=21" # url där frågesportens frågor och svar finns

r = requests.get(url) # requestar url
API = r.json() 

antalrätt = 0 # variabel för antal rätt svar hos användaren
frågenummer = 0 # variabel för antalet frågor användaren har fått
antalfrågorkvar = 0

svar = API

frågor = []
rättsvar = []
felsvar = []

# for i in svar["results"]: # loop som hämtar i [results]
#     print(i['question']) # hämtar frågor
#     print(i['correct_answer']) # hämtar rätt svar
#     print(i['incorrect_answers']) # hämtar fel svar

for i in API['results']: # Går in i api:n och results
    frågor.append(i['question']) # skapar array med frågor
    rättsvar.append(i['correct_answer']) # skapar array med rätt svar
    felsvar.append(i['incorrect_answers']) # skapar array med fel svar


print(" ------ SPORT FRÅGESPORT ------")
print("Välkommen till sportfrågesporten. Det finns tio frågor med 4 svars alternativ på varje.")
print("Skriv in A, B, C eller D i svarsfältet beroende på vilket svar du tror är det rätta.")
print("Lycka till och ha kul!")


while frågenummer < 11:
    tal = random.randint(1,10) # randomiserar tal mellan 1 och 10 för att hämta random fråga och inte samma varje gång
    print(frågor[tal])
    print(rättsvar[tal])
    print(felsvar[tal])
    frågor.remove(frågor[tal])
    rättsvar.remove(rättsvar[tal])
    felsvar.remove(felsvar[tal])
    användarenssvar = input("Skriv ditt svar här: ")
    if (användarenssvar == rättsvar[tal]):
        antalrätt += 1 # adderar 1 till antalrätt varje gång användaren svarar rätt
        print( användarenssvar + " är rätt svar, bra jobbat!" )
    else:
        print( användarenssvar + " är tyvärr fel svar, du sätter nästa!")
    frågenummer += 1
    antalfrågorkvar = 10 - int(frågenummer)
    print("Du har nu " + antalrätt + " rätt av " + frågenummer " möjliga. Det innebär att det återstår " + antalfrågorkvar + ". Lycka till!")

