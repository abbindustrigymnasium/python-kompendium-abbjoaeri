# #test 4.1
deltagare = ["lina", "gunilla", "erik"]
for person in deltagare:
    print('Välkommen ' + person.capitalize() + '!')

# # test 4.2
mängd = range(100000000000)
for nummer in mängd:
    print(nummer)

# test 4.3
namn = ["Joakim", "Lindrit", "Linus", "Lena", "Maria", "Matilda"] # gör en lista med namn
#Delar nu upp namn i 2 delar med hjälp av slicing
mansnamn = namn[0:3] # vilka av platserna har mansnamn
kvinnonamn = namn[3:6]

print('kvinnonamn:')
for namn in kvinnonamn: # for loop som hittar kvinnonamn
    print("\t" + namn)

print('mansnamn:')
for namn in mansnamn: # for loop som hittar mansnamn
    print("\t" + namn)

#4.4 övningsuppgifter

# #4.1
allatal = 0
for i in range(500):
    allatal += i
print(allatal/2)

#4.1
summa = 0 
for i in range(500): # for loop som räknar ut summan av alla udda heltal från 0 till 500
    if i%2 == 1: # %2 kollar om talet är ojämnt
        summa += i

print(summa)



