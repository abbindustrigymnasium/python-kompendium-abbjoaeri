import random # importerar random
import requests # importera requests

url = "https://opentdb.com/api.php?amount=10&category=21" # url där frågesportens frågor och svar finns

r = requests.get(url) # requestar url
API = r.json() 
svar = API 
antalrätt = 0 # variabel för antal rätt svar hos användaren
frågenummer = 0 # variabel för antalet frågor användaren har fått
antalfrågorkvar = 8 # variabel för hur många frågor som återstår så programmet och användaren vet det

frågor = [] # skapar arrays med frågor och svar. 
rättsvar = []
felsvar = []

for i in API['results']: # Går in i api:n och results
    frågor.append(i['question']) # skapar array med frågor
    rättsvar.append(i['correct_answer']) # skapar array med rätt svar
    felsvar.append(i['incorrect_answers']) # skapar array med fel svar

print(" ------ SPORT FRÅGESPORT ------") # skriver ut information och hur spelet går till. 
print("Välkommen till sportfrågesporten. Det finns åtta frågor med fyra svars alternativ på varje.")
print("Skriv in det alternativ du tror är det rätta i svarsfältet.")
print("Lycka till och ha kul!")
print("")

while frågenummer < 11:
    tal = random.randint(1, antalfrågorkvar) # randomiserar tal mellan 1 och antalfrågorkvar för att hämta random fråga och inte samma varje gång, dessutom gör det så att det kommer nya frågor hela tiden och samma fråga inte kan komma flera gånger. 
    allalternativ = felsvar[tal] # skapar en array med felsvar (lägger till rätt svar på nästa rad) för att de ska kunna randomiseras och inte komma i samma ordning hela tiden. 
    allalternativ.append(rättsvar[tal])
    random.shuffle(allalternativ) # randomiserar ordningen på svarsalternativen
    frågenummer += 1
    print(" - Fråga nummer: " + str(frågenummer))
    print(frågor[tal]) # skriver ut fråga för det tal som randomiseras. 
    print(allalternativ) # skriver ut rättsvar för det tal som randomiseras. 
    användarenssvar = input("Skriv ditt svar här: ")
    if (användarenssvar.lower().title() == rättsvar[tal]): # title
        antalrätt += 1 # adderar 1 till antalrätt varje gång användaren svarar rätt
        print(str(användarenssvar.lower().title()) + " är rätt svar, bra jobbat!" ) # skriver ut om det är rätt svar
    else:
        print(str(användarenssvar.lower().title()) + " är tyvärr fel svar. Rätt svar är " + str(rättsvar[tal]) + ". du sätter nästa!") # skriver ut användarens felaktiga svar och det rätta svaret
    antalfrågorkvar -= 1  # tar bort hur många frågor som återstår efter varje fråga. För att både användaren och programmet ska veta när spelet är slut. 
    if frågenummer < 8: # Kollar så att spelet inte är slut. 
        print("")
        print("Du har nu " + str(antalrätt) + " rätt av " + str(frågenummer) + " möjliga. Det innebär att det återstår " + str(antalfrågorkvar) + " frågor. Lycka till!") # skriver ut nuvarande resultat och eventuella frågor som återstår
        print("")
    else: # om frågenummer är 8 och spelet är slut så skrivs det ut att spelet är slut. 
        print("Spelet är nu avslutat, du fick " + str(antalrätt) + " rätt av " + str(frågenummer) + " möjliga. Bra jobbat! Spela gärna igen!") # skriver ut resultat
        print("")
        break # bryter hela loopen (och avslutar spelet) om användaren har svarat på alla frågor
    frågor.remove(frågor[tal]) # tar bort den fråga som precis har vari,t med hjälp av variabeln tal som vi skapade i början av loopen.
    rättsvar.remove(rättsvar[tal]) # tar bort det svar som precis har varit, med hjälp av variabeln tal som vi skapade i början av loopen.
    felsvar.remove(felsvar[tal]) # tar bort de fel svar som precis har varit, med hjälp av variabeln tal som vi skapade i början av loopen.
