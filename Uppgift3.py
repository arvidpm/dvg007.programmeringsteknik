# Programmeringsteknik webbkurs KTH inlämningsuppgift 3.
# Arvid Persson
# 2015-03-XX
#
# Detta är ett program som skapar en dikt av en inläst text.
# Programmet läser in fyra meningar och skriver sedan ut texten
# uppdelad på följande rader:

import random, sys


class Visitor:
    # Konstruktor
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name, self.height

class Attraction:

    # Konstruktor
    def __init__(self, name, minheight, passengers, dangerlevel):
        self.name = name
        self.height = minheight
        self.passengers = passengers
        self.dangerlevel = dangerlevel

    def __str__(self):
        return self.name, self.height, self.passengers, self.dangerlevel

    def start(self):
        print()
        if random.randrange(0,2) == 0:
            self.broken()
            self.stop()


    def stop(self):
        print(self.sto)


    def broken(self):
        print(random.randrange(0,2))


    def dangerlevel(self):
        if self.dangerlevel <= 4:
            print("Den här attraktionen är coollugn!")
        elif self.dangerlevel >4<=7 :
            print("Den här attraktionen är lite farlig..")
        elif self.dangerlevel >7:
            print("Säker på att du ska åka denna? Den är dödligt farlig!")




# Huvudprogrammet
def main():

    # Inmatning av gästens data
    name = input("Välkommen! Vad heter du?: ")
    height = input("Din längd (i cm): ")

    # Skapar besöksobjekt, inparametrar (namn, ålder, längd)
    visitor = Visitor(name, height)
    print('\nVälkommen ' + visitor.name + '! ' + visitor.height + ' cm är nog för inträde.')

    # Skapar attraktionsobjekt, inparametrar (namn, minlängd, passagerarantal, farlighetsnivå)
    attractions = [Attraction('Mountain Ride', 140, 20, 9),
                   Attraction('Fun House', 90, 40, 4),
                   Attraction('Radio Cars', 120, 30, 7)]

    attractionbroken = [("Attraktionen gick sönder och behöver oljas, försök igen eller åk en annan!"),
                        ("De anställda gästarbetarna är slut och behöver en rast, "
                         "försök igen senare eller åk en annan!"),
                        ("Den här är helt paj och behöver fixas, försök igen eller åk en annan!")]

    attractionscream = [("---------------------Attraktionen startar---------------------\n"
                         "---------------------WOOOHOOOOO!---------------------"),
                        ("---------------------Attraktionen startar---------------------\n""
                        "---------------------NU KÖÖÖÖR VIIII!!!---------------------")]

    # Huvudmenyn
    while True:
        if choice[0] == "1":
            visitor.mountainRide()
        elif choice[0] == "2":
            visitor.funhouseRide()
        elif choice[0] == "3":
            visitor.radiocarsRide()
        elif choice[0] == "4":
            guest.aircastleRide()
        elif choice[0] == "7":
            print("Du heter" + visitor.name + "och du är" + visitor.height + "cm lång.")
        elif choice[0] == "8":
            height = input("Ange ny längd (i cm): ")
            visitor = Visitor(visitor.name, height)
        elif choice[0] == "9":
            print("Hejdå,", visitor.name, "! Hoppas att du haft en rolig dag!")
            sys.exit(9)
        else:
            print("\nNågot blev fel!\n")

        print()
        choice = input("Vilken attraktion vill du prova åka? Välj bland:\n1. Berg-och-dalbana\n2. Lustiga huset"
                   "\n3. Radiobilarna\n\n7. Visa din information\n8. Ändra längd"
                   "\n9. Orkar inte mer, jag vill gå hem!\n\nGör ditt val: ")

main()