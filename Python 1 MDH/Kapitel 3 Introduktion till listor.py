#3.2 Övningsuppgifter

#3.1 
male = ["Erik", "Lars", "Karl", "Anders", "Johan"]
female = ["Maria", "Anna", "Margareta", "Elisabeth", "Eva"]

# print(male[0])
# print(female[2])
# print(female[4])
# print(male[1])
#3.2
# del male[1]
# del male[2]
# del female[0]

# print(male)
# print(female)

#3.3
# male.append("Jocke")
# print(male)
# print(female)

#3.4
# male.sort()
# female.sort()
# print(male)
# print(female)

#3.5
namn = input("Skriv ditt namn:")
if namn in male:
    male.remove(namn)
if namn in female:
    female.remove(namn)
print(male)
print(female)