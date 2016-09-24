# -*- coding: iso8859-1 -*-

# Titel: Teatrar
# Författare: Daniel Skarehag
# Datum: 2014-09-13
#
# Det här är ett program för att strukturera vinster och beläggning för teatrar.
# Programmet läser teatrar från en fil med namnet "teatrar.txt"

# En klass som beskriver en teater:
#    name - namnet på teatern
#    adult_price - priset för en vuxen
#    elderly_price - priset för en pensionär
#    child_price - priset för ett barn
#    seats - antal platser i teatern
#
#    income - hur mycket teatern har tjänat in
#    occupancy - hur många platser i teatern som är bokade
#    adult_tickets - hur många sålda vuxenbiljetter
#    elderly_tickets - hur många sålda pensionärsbiljetter
#    child_tickets - hur många sålda barnbiljetter
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

    # För utskrift med print
    def __str__(self):
        return self.name

    # Uppdatera beläggning och intäkter. Kommer göras för varje typ av biljett.
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

    # Returnera intäkter
    def GetIncome(self):
        return self.income

    # Returnera beläggningsgrad i procent
    def GetOccupancy(self):
        return (self.occupancy/self.seats)*100

def LoadTheatres(filename):
    # Öppna fil och ladda in teatrar i en lista
    Theatres = []
    
    with open(filename,'r') as f:
        for line in f:
            line = line.split('/')
            Theatres.append(Theatre(line[0], int(line[1]), int(line[2]), int(line[3]), int(line[4])))
     
    return Theatres

def main():
    # Användarinterface
    FILENAME = 'teatrar.txt'

    listTheatres = []
    listTheatres = LoadTheatres(FILENAME)

    # För varje teater, fråga hur många biljetter som såldes i varje kategori
    # Uppdatera sedan genom SetData    
    for t in listTheatres:
        print('Hur många biljetter såldes i ' + t.name + '?')
        
        adult = input('Vuxenbiljetter: ')
        elderly = input('Pensionärsbiljetter: ')
        child = input('Barnbiljetter: ')
        
        t.SetData(int(adult), 1)
        t.SetData(int(elderly), 2)
        t.SetData(int(child), 3)

    # Sortera efter output från metoden GetOccupancy
    listTheatres = sorted(listTheatres, key=lambda theatre: theatre.GetOccupancy(), reverse=True)

    # Printa ut beläggning för varje teater, samt addera ihop intäkter
    total_income = 0
    for t in listTheatres:
        print(t.name + ':\n* Beläggning: ' + str(t.GetOccupancy()) + '%\n* Intäkter: ' + str(t.income) + '\n')
        total_income += t.income
    
    print('--------------------------------')
    print('Totala intäkter: ' + str(total_income))

    return
main()
