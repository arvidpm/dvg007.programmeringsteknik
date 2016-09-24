# Programmeringsteknik webbkurs KTH inlämningsuppgift 3.
# Arvid Persson Moosavi
# 2015-12-27
#
# Detta är en enkel nöjespark med fyra attraktioner varav tre fungerande.
# Gästen har möjlighet att ändra ålder och längd under programmets körning.

# Importerar random (maskinfel) samt sys för korrekt avslut i metoden leave()
from random import *
import sys

class AmusementPark:

    # Konstruktorn. Genererar namn, ålder och längd till objektet genom user input name, age, height.
    def __init__(self, name, age, height):
        self.age = age
        self.name = name
        self.height = height

    # Printar ut välkomnande, namn, ålder och längd.
    def showVisitor(self):       
        print("\nVälkommen", self.name,"!", "\nDu är", self.age, "år gammal och din längd är", self.height,"cm!")

    # mountainRide() är en berg-och-dalbana för de äldre och längre besökarna. Felfrekvens 30%.
    def mountainRide(self):
        minHeight = 140
        minAge = 13
        coinFlip = self.coinFlip(0,100)

        print()
        if int(self.height) < minHeight:
            print("Tyvärr, du måste växa på dig lite innan du får åka denna attraktion!"
                  "\nMinimilängd är",minHeight,"cm.")
        elif int(self.age) < minAge:
            print("Tyvärr, lägsta ålder för denna attraktion är",minAge,"år!")
        elif coinFlip <= 30:
            print("Attraktionen gick sönder och behöver oljas, försök igen eller åk en annan!")
        else:
            print("---------------------Attraktionen startar---------------------")
            print("---------------------Nu kör vi!!!---------------------")
            print("---------------------WOOOHOOOOO!---------------------")
            print("")

    # funhouseRide(), eller Lustiga Huset, välkomnar stora som små besökare. Felfrekvens 20%.
    def funhouseRide(self):
        minHeight = 90
        minAge = 9
        coinFlip = self.coinFlip(0,100)

        print()
        if int(self.height) < minHeight:
            print("Tyvärr, du måste växa på dig lite innan du får åka denna attraktion!"
                  "\nMinimilängd är",minHeight,"cm.")
        elif int(self.age) < minAge:
            print("Tyvärr, lägsta ålder för denna attraktion är",minAge,"år!")
        elif coinFlip <= 20:
            print("De anställda gästarbetarna är slut och behöver en rast, "
                  "försök igen senare eller åk en annan!")
        else:
            print("---------------------Attraktionen startar---------------------")
            print("---------------------ÅÅÅÅÅÅH VAD LUSTIGA HUSET ÄR ROLIGT!----------")
            print("---------------------WOOOHOOOOO!---------------------")

    # Radiobilarna kräver att du är 120 cm lång och 11 år.
    # Attraktionen är väldigt gammal och felar hälften av gångerna.
    def radiocarsRide(self):
        minHeight = 120
        minAge = 11
        coinFlip = self.coinFlip(0,100)

        print()
        if int(self.height) < minHeight:
            print("Tyvärr, du måste växa på dig lite innan du får åka denna attraktion!"
                  "\nMinimilängd är",minHeight,"cm.")
        elif int(self.age) < minAge:
            print("Tyvärr, lägsta ålder för denna attraktion är",minAge,"år!")
        elif coinFlip <= 50:
            print("Din bil gick sönder och behöver oljas, försök igen eller åk en annan!")
        else:
            print("---------------------Attraktionen startar---------------------")
            print("---------------------BRUM BRUM BRUM---------------------")
            print("---------------------WOOOHOOOOO!---------------------")

    # Denna attraktion är fiktiv och körs aldrig.
    def aircastleRide(self):
        coinFlip = True

        print()
        if coinFlip == True:
            print("Det kan vara så att denna attraktion inte existerar...")
        else:
            print("This should never run..")

    # Genererar ett slumptal i intervallet min,max.
    def coinFlip(self,min,max):
        randomnr = randrange(min,max)
        return randomnr

    # Denna metod ändrar attributen i self, mest för testsyfte.
    def changeSelf(self):
        self.age = input("Ändra ålder till: ")
        self.height = input("Ändra längd till: ")

    # Skriver ut avsked till gäst, avslutar programmet.
    def leave(self):
        print()
        print("Hejdå,", self.name,"! Hoppas att du haft en rolig dag!")
        sys.exit()

# Huvudprogrammet
def main():

    # Inmatning av gästens data
    name = input("Välkommen! Vad heter du?: ")
    age = input("Hur gammal är du? ")
    height = input("Vi behöver även veta din längd (i cm): ")

    # Skapar ett gästobjekt
    guest = AmusementPark(name,age,height)
    guest.showVisitor()
    print()

    # Huvudmenyn
    choice = input("Vilken attraktion vill du prova åka? Välj bland:\n1. Berg-och-dalbana\n2. Lustiga huset"
                   "\n3. Radiobilarna\n4. Luftslottet\n\n7. Visa besökarens information\n8. Ändra längd/ålder"
                   "\n9. Orkar inte mer, jag vill gå hem!\n\nGör ditt val: ")
    while choice:
        if choice[0] == "1":
            guest.mountainRide()
        elif choice[0] == "2":
            guest.funhouseRide()
        elif choice[0] == "3":
            guest.radiocarsRide()
        elif choice[0] == "4":
            guest.aircastleRide()
        elif choice[0] == "7":
            guest.showVisitor()
        elif choice[0] == "8":
            guest.changeSelf()
        elif choice[0] == "9":
            guest.leave()
        else:
            print("\nNågot blev fel!\n")

        print()
        choice = input("Vilken attraktion vill du prova åka? Välj bland:\n1. Berg-och-dalbana\n2. Lustiga huset"
                   "\n3. Radiobilarna\n4. Luftslottet\n\n7. Visa besökarens information\n8. Ändra längd/ålder"
                   "\n9. Orkar inte mer, jag vill gå hem!\n\nGör ditt val: ")

main()