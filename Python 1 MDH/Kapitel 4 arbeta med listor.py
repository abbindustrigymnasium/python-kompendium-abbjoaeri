# #test 4.1
# deltagare = ["lina", "gunilla", "erik"]
# for person in deltagare:
#     print('Välkommen ' + person.capitalize() + '!')

# # test 4.2
# mängd = range(100000000000)
# for nummer in mängd:
#     print(nummer)

# # test 4.3
# namn = ["Joakim", "Lindrit", "Linus", "Lena", "Maria", "Matilda"]
# #Delar nu upp namn i 2 delar med hjälp av slicing
# mansnamn = namn[0:3]
# kvinnonamn = namn[3:6]

# print('Kvinnonamn:')
# for namn in kvinnonamn:
#     print("\t" + namn)

# print('Mansnamn:')
# for namn in mansnamn:
#     print("\t" + namn)

#4.4 övningsuppgifter

# #4.1
# allatal = 0
# for i in range(500):
#     allatal += i
# print(allatal/2)

#4.2
# summa = 0
# for i in range(500):
#     if i%2 == 1:
#         summa += i

# print(summa)

# #4.3
# registrerade = ["Anna", "Eva", "Erik", "Lars", "Karl"]
# avanmälningar = ["Anna", "Erik", "Karl"]

# for namn in avanmälningar: # definerar alla platser i avanmälningar som namn
#     del registrerade[(registrerade.index(namn))] # raderar alla platser i registrerarde som har ett namn i avanmälningar. 

# print(registrerade)

#4.4

# förnamn = ["Maria", "Erik", "Karl"]
# efternamn = ["Svensson", "Karlsson", "Andersson"]

# for namn in förnamn: # Varje förnamn
#     for name in efternamn: #Varje efternamn
#         print(namn + " " + name) # Skriver ut varje förnamn mellanslag varje efternamn

#
