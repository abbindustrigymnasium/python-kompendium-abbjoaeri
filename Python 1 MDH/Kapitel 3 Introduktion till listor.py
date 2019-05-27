#3.2 Övningsuppgifter

#3.1 
male = ["Erik", "Lars", "Karl", "Anders", "Johan"]
female = ["Maria", "Anna", "Margareta", "Elisabeth", "Eva"]

print(male[0]) # skriver ut första namnet i listan med male
print(female[2]) # skriver ut andra namnet i listan med female 
print(female[4])
print(male[1])

#3.2
del male[1]
del male[2]
del female[0]

print(male)
print(female)

#3.3
male.append("Jocke") # Lägger till Jocke i male listan
print(male)
print(female)

#3.4
male.sort()
female.sort()
print(male)
print(female)

#3.5
namn = input("Skriv ditt namn:") # skriver in sitt namn i terminalen
if namn in male: # checkar om namnet finns i listan med män
    male.remove(namn) # raderar namnet om det finns i listan
if namn in female: # checkar om namnet finns i listan med kvinnor
    female.remove(namn) # raderar namnet om det finns i listan
print(male) # skriver ut listorna
print(female)