# -*- coding: iso8859-1 -*-

# Titel: Teatrar
# F�rfattare: Daniel Skarehag
# Datum: 2014-09-13
#
# Det h�r �r ett program f�r att strukturera vinster och bel�ggning f�r teatrar.
# Programmet l�ser teatrar fr�n en fil med namnet "teatrar.txt"

# En klass som beskriver en teater:
#    name - namnet p� teatern
#    adult_price - priset f�r en vuxen
#    elderly_price - priset f�r en pension�r
#    child_price - priset f�r ett barn
#    seats - antal platser i teatern
#
#    income - hur mycket teatern har tj�nat in
#    occupancy - hur m�nga platser i teatern som �r bokade
#    adult_tickets - hur m�nga s�lda vuxenbiljetter
#    elderly_tickets - hur m�nga s�lda pension�rsbiljetter
#    child_tickets - hur m�nga s�lda barnbiljetter
class Theatre:
    # Konstruktor
    def __init__(self, name, seats, adult_price, elderly_price, child_price):
        self.name = name
        self.adult_price = adult_price
        self.elderly_price = elderly_price
        self.child_price = child_price
        self.seats = seats
        
        self.income = 0
        self.occupancy = 0
        self.adult_tickets = 0
        self.elderly_tickets = 0
        self.child_tickets = 0

    # F�r utskrift med print
    def __str__(self):
        return self.name

    # Uppdatera bel�ggning och int�kter. Kommer g�ras f�r varje typ av biljett.
    def SetData(self, SoldTickets, Type):
        if(Type == 1):
            self.income += SoldTickets*self.adult_price
            self.adult_tickets += SoldTickets
            self.occupancy += SoldTickets
        elif(Type == 2):
            self.income += SoldTickets*self.elderly_price
            self.elderly_tickets += SoldTickets
            self.occupancy += SoldTickets
        elif(Type == 3):
            self.income += int(SoldTickets)*self.child_price
            self.child_tickets += SoldTickets
            self.occupancy += SoldTickets
        return

    # Returnera int�kter
    def GetIncome(self):
        return self.income

    # Returnera bel�ggningsgrad i procent
    def GetOccupancy(self):
        return (self.occupancy/self.seats)*100

def LoadTheatres(filename):
    # �ppna fil och ladda in teatrar i en lista
    Theatres = []
    
    with open(filename,'r') as f:
        for line in f:
            line = line.split('/')
            Theatres.append(Theatre(line[0], int(line[1]), int(line[2]), int(line[3]), int(line[4])))
     
    return Theatres

def main():
    # Anv�ndarinterface
    FILENAME = 'teatrar.txt'

    listTheatres = []
    listTheatres = LoadTheatres(FILENAME)

    # F�r varje teater, fr�ga hur m�nga biljetter som s�ldes i varje kategori
    # Uppdatera sedan genom SetData    
    for t in listTheatres:
        print('Hur m�nga biljetter s�ldes i ' + t.name + '?')
        
        adult = input('Vuxenbiljetter: ')
        elderly = input('Pension�rsbiljetter: ')
        child = input('Barnbiljetter: ')
        
        t.SetData(int(adult), 1)
        t.SetData(int(elderly), 2)
        t.SetData(int(child), 3)

    # Sortera efter output fr�n metoden GetOccupancy
    listTheatres = sorted(listTheatres, key=lambda theatre: theatre.GetOccupancy(), reverse=True)

    # Printa ut bel�ggning f�r varje teater, samt addera ihop int�kter
    total_income = 0
    for t in listTheatres:
        print(t.name + ':\n* Bel�ggning: ' + str(t.GetOccupancy()) + '%\n* Int�kter: ' + str(t.income) + '\n')
        total_income += t.income
    
    print('--------------------------------')
    print('Totala int�kter: ' + str(total_income))

    return
main()
