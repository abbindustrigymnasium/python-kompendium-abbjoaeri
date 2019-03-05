# Minsiffra = 10
# Ennysiffra = Minsiffra + 5
# print(Ennysiffra)
### En enkel addition

# a = 5
# b = 5
# c = a + b
# print(c)
### Se skillnad mellan a = "2" och a = 2

# strängar = "En datatyp som består av till exempel en sån här textrad."
# print(strängar)
### En sträng skrivs med citattecken runt medans en int skrivs utan.

# Jocke = 1337
# Mittnamn = Jocke
#print(Mittnamn) # Här skrivs 1337 eftersom att det är den som Mittnamn till sist går till. Se nästa rad för hur man ska skriva för att få ut Jocke. 
# Mittnamn = "Jocke"
# print(Mittnamn)
### Det krävs alltså kaninöron för att Jocke ska skrivas ut.



#ÖVNINGSUPPGIFTER KAPITEL 2.2

#2.1

# citat = "datatyper har inbyggda metoder"
# citat2 = citat.upper()
# print(citat2)


#2.2

# print("Mata in valfritt decimaltal!")
# tal1 = float(input())
# tal2 = int(tal1)
# print(tal2)

#2.3

# print("Hej!")
# print("Vad är ditt förnamn?")
# förnamn = input()
# print("Vad är ditt efternamn?")
# efternamn = input()
# print("Trevligt att träffas " + förnamn + " " + efternamn + "! :)")

#2.4

# print()
# ålder = input("Hur gammal är du?")
# ålder1 = int(ålder)
# årtillmyndig = 18 - ålder1
# print("Du är myndig inom " + str(årtillmyndig) + " år!")

#2.5

a = input("Hur många elever vill ha 2 vanliga korvar?")
b = input("Hur många elever vill ha 3 vanliga korvar?")
c = input("Hur många elever vill ha 2 vegetariska korvar?")
d = input("Hur många elever vill ha 3 vegetariska korvar?")

vanliga2 = int(a) * 2
vanliga3 = int(b) * 3
vegan2 = int(c) * 2
vegan3 = int(d) * 3

förpackningvanlig = (vanliga2 + vanliga3)/8
förpackningvegetarisk = (vegan2 + vegan3)/8
drickor = int(int(a)+int(b)+int(c)+int(d))
pris = förpackningvanlig * 20.95 + förpackningvegetarisk * 34.95 + drickor * 13.95



print("Antal förpackningar vanliga korvar: " + str(förpackningvanlig))
print("Antal förpackningar vegetariska korvar: " + str(förpackningvegetarisk))
print("Det behövs " + str(drickor) + " drickor till skolutflykten.")
print("Kostnaden blir: " + str(pris) + " SEK.")