clientAge: int = 0
clientDLicense: int = 0
clientSeniority: int = 0
clientAccident: int = 0
clientTarif: str = ""
clientAccepted: bool = True

clientAge = int(input("Quel est votre âge : "))
clientDLicense = int(input("Nombre d'années de votre permi : "))
clientAccident = int(input("Nombre d'accidents : "))
clientSeniority = int(input("Depuis combien de temps êtes-vous chez nous : "))

if clientAge <= 25:
    if clientDLicense <=2:
        clientTarif = "rouge"
    elif clientDLicense > 2:
        if clientAccident == 0:
            clientTarif = "orange"
        elif clientAccident == 1:
            clientTarif = "rouge"
        else:
            print("On veut pas de vous ici, désolé !")
            clientAccepted = False
    else:
        print("On veut pas de vous ici, désolé !")
        clientAccepted = False
elif clientAge > 25:
    if clientDLicense <= 2:
        if clientAccident == 0:
            clientTarif = "orange"
        elif clientAccident == 1:
            clientTarif = "rouge"
        else:
            print("On veut pas de vous ici, désolé !")
            clientAccepted = False
    else:
        if clientAccident == 0:
            clientTarif = "vert"
        elif clientAccident == 1:
            clientTarif = "orange"
        elif clientAccident == 2:
            clientTarif = "rouge"
        else:
            print("On veut pas de vous ici, désolé !")
            clientAccepted = False
else:
    print("On veut pas de vous ici, désolé !")
    clientAccepted = False


if clientSeniority > 5:
    if clientTarif == "rouge":
        clientTarif = "orange"
        print("Votre tarif est : "+clientTarif)
    elif clientTarif == "orange":
        clientTarif = "vert"
        print("Votre tarif est : "+clientTarif)
    else:
        clientTarif = "bleu"
        print("Votre tarif est : "+clientTarif)

if clientAccepted:
    print("Votre tarif prévu est : "+clientTarif)
