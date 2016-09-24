# Programmeringsteknik webbkurs KTH inlämningsuppgift 3.
# Arvid Persson Moosavi
# 2016-09-24
#
# Detta är inlämningsuppgiften Nöjesfält
#
# Programmet tar indata namn, längd vid start och använder dessa
# för att kontrollera så användaren inte är för kort för attraktionen
#
# Klassen Visitor har en konstruktor för besökaren, denna används även om besökaren vill ändra sin längd
# Klassen Attraction har konstruktor för attraktionerna, samt metoder för att starta/stoppa attraktionen
#

import sys, time
from random import randint


class Visitor:

    # Konstruktor
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name, self.height

class Attraction:

    # Konstruktor
    def __init__(self, name, minheight, passengers, dangerlevel, broken, scream, commercial):
        self.name = name
        self.height = minheight
        self.passengers = passengers
        self.dangerlevel = dangerlevel
        self.broken = broken
        self.scream = scream
        self.commercial = commercial

    def __str__(self):
        return self.name, self.height, self.passengers, self.dangerlevel, self.broken, self.scream, self.commercial

    def start(self):
        print()

        # Slumpar haveri
        if randint(0,2) == 0:
            print(self.name,":", self.broken)
            self.stop()
            time.sleep(3)
        else:
            # Skriver ut farlighetsnivå
            if self.dangerlevel < 5:
                print("Den här attraktionen är coollugn!")
            elif self.dangerlevel < 8:
                print("Den här attraktionen är lite farlig..")
            else:
                print("Säker på att du ska åka denna? Den är dödligt farlig!")
            time.sleep(3)
            print()
            print(self.scream)
            print()
            self.stop()
            time.sleep(3)

    # Metod som stoppar attraktionen
    def stop(self):
        print(self.name,": Attraktionen stannar...")

# Huvudprogrammet
def main():

    # Inmatning av gästens data
    name = input("Välkommen! Vad heter du?: ")
    height = input("Din längd (i cm): ")

    # Skapar besöksobjekt, inparametrar (namn, ålder, längd)
    visitor = Visitor(name, height)
    print('\nVälkommen', visitor.name, '!', visitor.height, 'cm är nog för inträde.\n')


    # Attraktionsdata, här går det att lägga till mer data att slumpa från
    attr_broken = ["Attraktionen gick sönder och behöver oljas, försök igen eller åk en annan!",
                        "De anställda gästarbetarna är slut och behöver en rast, "
                         "försök igen senare eller åk en annan!",
                        "Den här är helt paj och behöver fixas, försök igen eller åk en annan!"]

    attr_scream = ["---------------------Attraktionen startar---------------------\n"
                    "---------------------WOOOHOOOOO!---------------------",
                    "---------------------Attraktionen gnisslar igång--------------\n"
                     "---------------------NU KÖÖÖÖR VIIII!!!---------------------"]

    attr_commerical = ["Kom och åk mig, du kommer ha det superkul!",
                       "Åk med mig så bjuder jag på en godis efteråt!",
                       "Jag är den bästa attraktionen, jag svär på min grav!"]


    # Skapar attraktionsobjekt, inparametrar (namn, minlängd, passagerarantal, farlighetsnivå, söndermeddelande, skrikmeddelande, reklammeddelande)
    attractions = [ Attraction('Mountain Ride', 140, 20, 9, attr_broken[randint(0,2)], attr_scream[randint(0,1)], attr_commerical[randint(0,2)]),
                    Attraction('Fun House', 90, 40, 4, attr_broken[randint(0,2)], attr_scream[randint(0,1)], attr_commerical[randint(0,2)]),
                    Attraction('Radio Cars', 120, 30, 7, attr_broken[randint(0,2)], attr_scream[randint(0,1)], attr_commerical[randint(0,2)])]

    # Gör reklam för vald attraktion och startar denna om användaren skriver "ja"
    def rideprep(ride):

        if int(visitor.height) < attractions[ride].height:
            print("Du är för kort för attraktionen",attractions[ride].name,visitor.name)
            print("Minsta längd är:",attractions[ride].height)
            time.sleep(3)
        else:
            print(attractions[ride].name,"tar",attractions[ride].passengers,"passagerare")
            print(attractions[ride].name,":",attractions[ride].commercial)
            sure = input("Starta? ja/nej: ")
            if sure == "ja":
                attractions[ride].start()


    # Huvudmenyn
    choice = input("Vilken attraktion vill du prova åka? Välj bland:\n\n1. Berg-och-dalbanan\n2. Lustiga huset"
                   "\n3. Radiobilarna\n\n7. Visa din information\n8. Ändra längd"
                   "\n9. Orkar inte mer, jag vill gå hem!\n\nGör ditt val: ")

    while choice:

        if choice[0] == "1":
            ride = 0
            rideprep(ride)

        elif choice[0] == "2":
            ride = int(1)
            rideprep(ride)

        elif choice[0] == "3":
            ride = int(2)
            rideprep(ride)

        elif choice[0] == "7":
            print("Du heter", visitor.name, "och du är", visitor.height, "cm lång :D")
            time.sleep(1)

        elif choice[0] == "8":
            height = input("Ange ny längd (i cm): ")
            visitor = Visitor(visitor.name, height)
            print("Din längd ändrades till cm:", visitor.height)
            time.sleep(1)

        elif choice[0] == "9":
            print("Hejdå", visitor.name, "! Hoppas att du haft en rolig dag!")
            sys.exit()

        else:
            print("\nNågot blev fel!\n")

        print()

        choice = input("Vilken attraktion vill du prova åka? Välj bland:\n\n1. Berg-och-dalbanan\n2. Lustiga huset"
                        "\n3. Radiobilarna\n\n7. Visa din information\n8. Ändra längd"
                        "\n9. Orkar inte mer, jag vill gå hem!\n\nGör ditt val: ")

# Initierar huvudprogrammet
main()