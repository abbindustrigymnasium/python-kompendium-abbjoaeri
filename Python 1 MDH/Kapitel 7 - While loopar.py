# #övningsuppgifter 7.2

# #7.1

# tal = int(input("Ange en multiplikationstabell: "))

# num = 0
# kolla = 0

# while True:
#     print(tal * num)
#     num += 1
#     kolla += 1
#     if kolla == 3:
#         jaellernej = input("Vill du fortsätta? ")
#         if jaellernej == "ja":
#             kolla = 0
#             continue
#         else:
#             break
            

#7.2
import random # importerar random eftersom det ska randomiseras
tal = random.randint(1,100) # vilket spann vi randomiserar inom.

print( "   ---- Högre eller lägre spel ----" )
print("Jag randomiserar ett tal mellan 0 och 100. Din uppgift är att lista ut vilekt talet är på så få försök som möjligt.")
print("Det enda jag säger är om talet är högre eller lägre än talet du angett.")

gissning = int(input("Skriv din gissning här: "))
antalgissningar = 0

while True:
    if tal > gissning: # if sats som används om spelaren gissat ett för lågt tal.
        print("Högre")
        gissning = int(input("Skriv din gissning här: "))
        antalgissningar += 1 # håller koll på antalet gissningar personen gjort så det kan skrivas ut i slutet
        continue
    if tal < gissning: # if sats som används om spelaren gissat ett för högt tal.
        print("Lägre")
        gissning = int(input("Skriv din gissning här: "))
        continue # körs om eftersom det inte är rätt svar
        antalgissningar += 1
    if tal == gissning:
        print(str(tal) + " är rätt!")
        antalgissningar += 1
        print("Det tog dig " + str(antalgissningar)+ " försök! Bra jobbat!") #  skriver ut hur många gissningar det tog
        break # bryter, eftersom spelaren gissat rätt
