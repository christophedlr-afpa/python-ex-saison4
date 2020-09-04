dateDay:        int = 0
dateMonth:      int = 0
dateYear:       int = 0
dateLeapYear:   bool = False

dateDay = int(input("Donner un numéro de jour : "))
dateMonth = int(input("Donner un numéro de mois : "))
dateYear = int(input("Donner une année : "))

# Algorithme
if dateDay < 1 or dateDay > 31:
    print("Date non valide")

if dateMonth < 1 or dateMonth > 12:
    print("Date non valide")

if dateYear%4 == 0 and dateYear%100 != 0:
    dateLeapYear = True
elif dateYear%400 == 0:
    dateLeapYear = True
else:
    dateLeapYear = False

if dateMonth == 1 or dateMonth == 3 or dateMonth == 5 or dateMonth == 7 or dateMonth == 8 or dateMonth == 10 or dateMonth == 12:
    if dateDay <= 31:
        print("Date valide")
elif dateMonth == 4 or dateMonth == 6 or dateMonth == 9 or dateMonth == 11:
    if dateDay == 31:
        print("Date non valide")
elif dateMonth == 2:
    if dateLeapYear:
        if dateDay <= 29:
            print("Date valide")
        else:
            print("Date non valide")
    elif dateDay > 28:
        print("Date non valide")
    else:
        print("Date valide")
else:
    print("Date non valide")
