# # Programmeringsteknik webbkurs KTH inlämningsuppgift P-uppgift
# Delmoment 1 - Kodskelett

# Arvid Persson Moosavi
# 2016-09-25
#
# Detta är deluppgiften kodskelett huvuduppgiften Tennismatch
#
# Programmet fungerar i grova drag så att den läser indata från textfilen Spelarlista.txt
# Existerar inte filen, eller om data från färra än två spelare finns, så kommer programmet avsluta
# Sedan skapas spelarobjekt utifrån datan m.h.a. klassen Player och dess konstruktor.
#
# Spelardatan laddas i main och skickas sedan som inparametrar till klassen Player
# Klassen Match simulerar en match mellan två spelare, och innehåller en funktion för att uppdatera resultatlistan
#

import sys, os.path
from itertools import islice
from random import randint

class Player:
    # Skapar en ny spelare
    def __init__(self, name, serveavg, m_won, m_played):
        self.name = name
        self.serveavg = serveavg
        self.won = m_won
        self.played = m_played

    # Returnerar spelaren med attribut
    def __str__(self):
        return self.name, self.serveavg, self.won, self.played



# Klassen Match simulerar matcher som spelas och uppdaterar även resultatlistan samt Spelarlista.txt
class Match:

    # En funktion som sköter matchförberedelser
    def playmatch(self, player1, player2):

        p1, p2, i = 0, 0, 0

        while i < 3:
            if randint(0,1) == 0:
                p1 =+1
            else:
                p2 =+1

            i =+1

        print(p1, p2)


    # En funktion som uppdaterar resultatlistan
    def resultlist(self, player1, player2):
        return

    # En funktion som sparar ny data till Spelarlista.txt
    def save(self, player1, player2, FILENAME):
        return



# Huvudprogram
def main():

    # Kontrollerar filens existens
    def checkfile(FILENAME):

        if os.path.isfile(FILENAME):
            return
        else:
            sys.exit("Spelarlista.txt kunde inte hämtas")

    # Funktion som kontrollerar antalet rader i textfilen
    def file_len(FILENAME):
        with open(FILENAME) as f:
            for i, l in enumerate(f):
                pass
        return i + 1


    # En funktion som läser indata från FILENAME och sedan skapar objekt av Player
    def playerdata(FILENAME):

        # Kollar antalet rader i filen
        num_lines = file_len(FILENAME)

        # Skapar array med all data från spelarna
        data = []

        with open(FILENAME) as fin:
            for line in islice(fin, 5, num_lines):

                data.append(line[:-1])

            fin.close()
            return data

    def createplayers(playerdata, FILENAME):

        num_lines = file_len(FILENAME)
        playercount = num_lines / 4


    FILENAME = 'Spelarlista.txt'


    checkfile(FILENAME)
    playerdata = playerdata(FILENAME)
    print(playerdata)









# Match.preparematch(player1, player2)
# match = Match(FILENAME)

# Meny för val av händelser
# choice = '';
# while choice != 'S':
#       Välj två spelare som ska gå en match
#

main()