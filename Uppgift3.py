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
    def __init__(self, visitorname, visitorlength):
        self.name = visitorname
        self.length = visitorlength

    def __str__(self):
        return self.name, self.length

class Attraction:

    # Konstruktor
    def __init__(self, name, minheight, passengers, dangerlevel):
        self.name = name
        self.height = minheight
        self.passengers = passengers
        self.dangerlevel = dangerlevel

    def __str__(self):
        return self.name, self.height, self.passengers, self.dangerlevel


print('Dear Amusement park visitor! Please...\n')
visitorname = input('Enter your name: ')
visitorlength = input('Enter your height (in cm): ')

# Skapar besöksobjekt, inparametrar (namn, längd)
visitor = Visitor(visitorname, visitorlength)
print('\nWelcome ' +visitor.name + '! ' + visitor.length + ' cm is enough for entering :)')

# Skapar attraktionsobjekt, inparametrar (namn, minlängd, passagerarantal, farlighetsnivå)
attractions = [Attraction('Mountain Ride', 140, 20, 9),
               Attraction('Fun House', 90, 40, 4),
               Attraction('Radio Cars', 120, 30, 7),
               Attraction('Air Castle', 9999, 1, 10)]



print(attractions[1].name)

