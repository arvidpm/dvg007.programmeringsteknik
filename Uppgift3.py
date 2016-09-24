# Programmeringsteknik webbkurs KTH inlämningsuppgift 3.
# Arvid Persson Moosavi
# 2016-09-24
#
# Detta är ett program som skapar en dikt av en inläst text.
# Programmet läser in fyra meningar och skriver sedan ut texten
# uppdelad på följande rader:

import random, sys, time


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
        if random.randrange(0,2) == 0:
            print(self.name,":", self.broken)
            self.stop()
        else:
            self.dangerlevel()
            print(self.scream)
            self.stop()



    def stop(self):
        print(self.name+": Attraktionen stannar...")


    def dangerlevel(self):
        if self.dangerlevel <= 4:
            print("Den här attraktionen är coollugn!")
        elif self.dangerlevel >4<=7 :
            print("Den här attraktionen är lite farlig..")
        elif self.dangerlevel >7:
            print("Säker på att du ska åka denna? Den är dödligt farlig!")
        time.sleep(3)




# Huvudprogrammet
def main():

    # Inmatning av gästens data
    name = input("Välkommen! Vad heter du?: ")
    height = input("Din längd (i cm): ")

    # Skapar besöksobjekt, inparametrar (namn, ålder, längd)
    visitor = Visitor(name, height)
    print('\nVälkommen', visitor.name, '!', visitor.height, 'cm är nog för inträde.\n')


    # Attraktionsdata, här går det att lägga till mer data att slumpa från
    attr_broken = [("Attraktionen gick sönder och behöver oljas, försök igen eller åk en annan!"),
                        ("De anställda gästarbetarna är slut och behöver en rast, "
                         "försök igen senare eller åk en annan!"),
                        ("Den här är helt paj och behöver fixas, försök igen eller åk en annan!")]

    attr_scream = ["---------------------Attraktionen startar---------------------\n"
                    "---------------------WOOOHOOOOO!---------------------",
                    "---------------------Attraktionen gnisslar igång--------------\n"
                     "---------------------NU KÖÖÖÖR VIIII!!!---------------------"]

    attr_commerical = ["Kom och åk mig, du kommer ha det superkul!",
                       "Åk med mig så bjuder jag på en godis efteråt!",
                       "Jag är den bästa attraktionen, jag svär på min grav!"]


    # Skapar attraktionsobjekt, inparametrar (namn, minlängd, passagerarantal, farlighetsnivå, söndermeddelande, skrikmeddelande, reklammeddelande)
    attractions = [ Attraction('Mountain Ride', 140, 20, 9, attr_broken[random.randrange(0,2)], attr_scream[random.randrange(0,1)], attr_commerical[random.randrange(0,2)]),
                    Attraction('Fun House', 90, 40, 4, attr_broken[random.randrange(0,2)], attr_scream[random.randrange(0,1)], attr_commerical[random.randrange(0,2)]),
                    Attraction('Radio Cars', 120, 30, 7, attr_broken[random.randrange(0,2)], attr_scream[random.randrange(0,1)], attr_commerical[random.randrange(0,2)])]

    def rideprep(ride):
        print(attractions[ride].commercial)
        choice = input("Starta? ja/nej: ")
        if choice == "ja":
            attractions[ride].start()


    # Huvudmenyn
    choice = input("Vilken attraktion vill du prova åka? Välj bland:\n\n1. Berg-och-dalbanan\n2. Lustiga huset"
                   "\n3. Radiobilarna\n\n7. Visa din information\n8. Ändra längd"
                   "\n9. Orkar inte mer, jag vill gå hem!\n\nGör ditt val: ")

    while choice:
        if choice[0] == "1":
            rideprep(0)

        elif choice[0] == "2":
            rideprep(1)

        elif choice[0] == "3":
            rideprep(2)

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


main()