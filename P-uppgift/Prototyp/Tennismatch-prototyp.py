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

#---------- Klass Player som skapar spelarobjekt -----------
class Player:
    # Skapar en ny spelare
    def __init__(self, name, serveavg, m_won, m_played, average_won):
        self.name = name
        self.serveavg = serveavg
        self.won = m_won
        self.played = m_played
        self.averagewon = average_won

    # Returnerar spelaren med attribut
    def __str__(self):
        return self.name



#---------- Funktioner för filkontroll, skapande av spelare, matcher, resultatuppdatering ------------

# Funktion som kontrollerar antalet rader i textfilen
def file_len(FILENAME):
    with open(FILENAME) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# En funktion som läser indata från FILENAME och sedan skapar objekt av Player
def createplayers(FILENAME):

    # Kontrollerar antalet rader i FILENAME
    num_lines = file_len(FILENAME)

    # Skapar array med all data från spelarna
    v = []

    with open(FILENAME) as file:

        # Loopar igenom data från rad 5 till slutet
        for line in islice(file, 5, num_lines):

            v.append(line[:-1])

        file.close()

        p1avg = round(( int(v[2]) / int(v[3]) ), 3)
        p2avg = round(( int(v[6]) / int(v[7]) ), 3)
        p3avg = round(( int(v[10]) / int(v[11]) ), 3)
        p4avg = round(( int(v[14]) / int(v[15]) ), 3)

        player= [ Player(v[0], v[1], v[2], v[3], p1avg),
                Player(v[4], v[5], v[6], v[7], p2avg),
                Player(v[8], v[9], v[10], v[11], p3avg),
                Player(v[12], v[13], v[14], v[15], p4avg) ]

        return player

# En funktion som sköter matchförberedelser
def playmatch(player1, player2):

    print(player1.won)
    print(player2.won)

    result = randint(0, 1)

    if result == 0:
        player1.won += 1
    else:
        player2.won += 1

    return player1, player2


# En funktion som sparar ny data till Spelarlista.txt
def save(self, player1, player2, FILENAME):
    return



# --------- Funktioner för gränssnitt -------------

def skrivlistan(player):
    for i in player:
        print(i, end=" ")
    print("\n")


def print_resultlist(player):

    player.sort(key=lambda player: player.averagewon)

    skrivlistan(player)


    #print('Plac.    Namn    Vunna   Spelade    %vunna')
    #print('1', player1.name, player1.won, player1.played, (player1.won/player1.played))


# Skriver ut valmenyn. Lånade denna från exemplet då den var snyggare än min
def print_menu():
    print ('1  söka på Titel.')
    print ('2  söka på Författare.')
    print ('3  Låna bok.')
    print ('4  Återlämna bok.')
    print ('6  Sluta.')

# Huvudprogram
def main():

    # Refererar textfil till konstant
    FILENAME = 'Spelarlista.txt'

    # Skapar spelarobjekt
    player = createplayers(FILENAME)

    print_resultlist(player)







    # player[0], player[1] = playmatch(player[0], player[1])



# Match.preparematch(player1, player2)
# match = Match(FILENAME)

# Meny för val av händelser
# choice = '';
# while choice != 'S':
#       Välj två spelare som ska gå en match
#

main()