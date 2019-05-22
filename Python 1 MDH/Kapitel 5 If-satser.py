#uppgifter:

# 5.1

# kön = input("Ange ditt kön: ")
# hårfärg = input("Ange din hårfärg: ")
# ögonfärg = input("Ange din ögonfärg: ")

# Daniel_Radcliffe = ['man', 'brun', 'brun', 'Daniel Radcliffe']
# Rupert_Grint = ['man', 'röd', 'blå', 'Rupert Grint']
# Emma_Watson = ['kvinna', 'brun', 'brun', 'Emma Watson']
# Selena_Gomez = ['kvinna', 'brun', 'brun', 'Selena Gomez']

# kändis = [Daniel_Radcliffe, Rupert_Grint, Emma_Watson, Selena_Gomez]

# for personer in kändis:
#     if kön == personer[0] and hårfärg == personer[1] and ögonfärg == personer[2]:
#         print( "Du är lik " + personer[3])

#     else: print("Du liknar ingen kändis.")

#5.2
# global a
# a = 0

# namn = str(input("Ange ditt namn här: "))
# ålder = str(input("Ange din ålder här: "))
# ålder = int(ålder)

# if ålder == 1:
#    # global a
#     a = 14
# elif ålder == 2:
#   #  global a
#     a = 13
# elif ålder == 3:
#   #  global a
#     a = 12
# elif ålder == 4:
#  #   global a
#     a = 11.5
# elif ålder == 5:
#   #  global a
#     a = 11
# elif ålder == 6:
#  #   global a
#     a = 11
# elif ålder == 7:
#  #   global a
#     a = 10.5
# elif ålder == 8:
#   #  global a
#     a = 10
# elif ålder == 9:
#  #   global a
#     a = 10
# elif ålder == 10:
#   #  global a
#     a = 10
# elif ålder == 11:
#   #  global a
#     a = 9.5
# elif ålder == 12:
#   #  global a
#     a = 9
# elif ålder == 13:
#   #  global a
#     a = 9
# elif ålder == 14:
#   #  global a
#     a = 9
# elif ålder == 15:
#    # global a
#     a = 9
# elif ålder == 16:
#    # global a
#     a = 8.5
# elif ålder == 17:
#   #  global a
#     a = 8
# else: 
#    # global a
#     a = 8
# a = str(a)
# ålder = str(ålder)
    
# print("Hallå " + namn + " enligt vårdguidens rekommendationer behöver individer i din ålder (" + ålder + " år) sova minst " + a + " timmar per natt.")

#5.2 alternativt lösningssätt

# namn = str(input("Ange ditt namn här: "))
# ålder = str(input("Ange din ålder här: "))

# a = [14, 13, 12, 11.5, 11, 11, 10.5, 10, 10, 10, 9.5, 9, 9, 9, 9, 8.5, 8]
# if ålder < 17:
#     t = a[ålder - 1]
# else: 
#     t = 8

# print("Hallå " + namn + " enligt vårdguidens rekommendationer behöver individer i din ålder (" + ålder + " år) sova minst " + t + " timmar per natt.")

#5.3

land = input("Skriv in ditt land: ")
land = land.capitalize()
norden = ['Danmark', 'Finland', 'Island', 'Norge', 'Sverige']
storbritannien = ['England', 'Nordirland', 'Skottland', 'Wales']

if land in norden:
    print("Ditt land " + land + " ligger i Norden.")
elif land in storbritannien:
    print("Ditt land " + land + " ligger i Storbritannien.")
else:
    print("Ditt land " + land + " ligger varken i Storbritannien eller Norden.")