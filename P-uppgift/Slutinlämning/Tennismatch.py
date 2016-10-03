# # Programmeringsteknik webbkurs KTH inlämningsuppgift P-uppgift
# Delmoment 3 - Slutinlämning

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


# ---------- Klass Player som skapar spelarobjekt -----------
class Player:
    # Skapar en ny spelare
    def __init__(self, name, serveavg, m_won, m_played, average_won):
        self.name = name
        self.serveavg = serveavg
        self.won = m_won
        self.played = m_played
        self.averagewon = average_won

    # Returnerar spelaren med attribut, samt formaterar för resultatlista
    def __str__(self):
        return '    {:15} {:>1} {:>8}   {}'.format(self.name, self.won, self.played, self.averagewon)


# ---------- Funktioner för filkontroll, skapande av spelare, matcher, resultatuppdatering ------------

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
def createplayers(FILENAME, FIRSTLINES):
    # Kontrollerar antalet rader i FILENAME
    num_lines = file_len(FILENAME)

    # Skapar array med all data från spelarna
    v = []

    with open(FILENAME, encoding="utf-8") as file:
        # Loopar igenom data från rad 5 till slutet
        for line in islice(file, FIRSTLINES, num_lines):
            line = line.replace('\n', '')
            v.append(line)

        p1avg = round((int(v[2]) / int(v[3])), 3)
        p2avg = round((int(v[6]) / int(v[7])), 3)
        p3avg = round((int(v[10]) / int(v[11])), 3)
        p4avg = round((int(v[14]) / int(v[15])), 3)

        player = [Player(v[0], v[1], v[2], v[3], p1avg),
                  Player(v[4], v[5], v[6], v[7], p2avg),
                  Player(v[8], v[9], v[10], v[11], p3avg),
                  Player(v[12], v[13], v[14], v[15], p4avg)]

        return player


# En funktion som sköter matchförberedelser
def playmatch(player1, player2, FILENAME, FIRSTLINES, player):
    player1.played = int(player1.played) + 1
    player2.played = int(player2.played) + 1

    result = randint(0, 1)

    if result == 0:
        player1.won = int(player1.won) + 1
        print(player1.name, "won!")
    else:
        player2.won = int(player2.won) + 1
        print(player2.name, "won!")

    player1.averagewon = int(player1.won) / int(player1.played)
    player2.averagewon = int(player2.won) / int(player2.played)

    print("--------------------------------------------\n")

    save(FILENAME, FIRSTLINES, player)


# En funktion som sparar ny data till Spelarlista.txt
def save(FILENAME, FIRSTLINES, player):
    # Kontrollerar antalet rader i FILENAME
    num_lines = file_len(FILENAME)

    # Raderar befintlig data, lämnar filen öppen
    oldlines = open(FILENAME).readlines()
    open(FILENAME, 'w').writelines(oldlines[:-(num_lines - FIRSTLINES)])

    # Skriver ny data

    for i in player:
        with open(FILENAME, "a", encoding='utf-8') as file:
            file.write(str(i.name) + '\n')
            file.write(str(i.serveavg) + '\n')
            file.write(str(i.won) + '\n')
            file.write(str(i.played) + '\n')


def testfunction(FILENAME, FIRSTLINES):
    # Kontrollerar antalet rader i FILENAME
    num_lines = file_len(FILENAME)

    # Antal spelare
    count = (num_lines - FIRSTLINES) / 4

    # Skapar array med all data från spelarna
    v = [count]

    with open(FILENAME, encoding="utf-8") as file:
        # Loopar igenom data från rad 5 till slutet
        for line in islice(file, FIRSTLINES, num_lines):
            line = line.replace('\n', '')
            v.append(line)

        p1avg = round((int(v[2]) / int(v[3])), 3)
        p2avg = round((int(v[6]) / int(v[7])), 3)
        p3avg = round((int(v[10]) / int(v[11])), 3)
        p4avg = round((int(v[14]) / int(v[15])), 3)

        player = [Player(v[0], v[1], v[2], v[3], p1avg),
                  Player(v[4], v[5], v[6], v[7], p2avg),
                  Player(v[8], v[9], v[10], v[11], p3avg),
                  Player(v[12], v[13], v[14], v[15], p4avg)]

        return player


# --------- Funktioner för gränssnitt -------------


def print_resultlist(player):
    player.sort(key=lambda player: player.averagewon, reverse=True)

    plac = 1
    print("\n----------------------------------------")
    print("Plac. Namn        Vunna  Spelade  %vunna")

    for i in player:
        print(plac, i)
        plac += 1
    print("----------------------------------------\n")


def print_playerlist(player):
    plac = 0
    print("\n----------------------------------------")
    print("Nr. Namn")

    for i in player:
        print(plac, " ", i.name)
        plac += 1


# Huvudprogram
def main():
    # Refererar textfil till konstant
    FILENAME = '../resources/Spelarlista.txt'

    # Kontrollerar om filen finns
    checkfile(FILENAME)

    # Konstant för första raderna i textfilen
    FIRSTLINES = 5

    # Skapar spelarobjekt
    player = createplayers(FILENAME, FIRSTLINES)

    # Sparar ny data till textfilen
    # save(FILENAME, FIRSTLINES, player)

    # playmatch(player[0], player[1])

    # Huvudmenyn
    choice = input("\nVälkommen!\n\n1. Spela match\n2. Visa spelare\n3. Visa resultat\n\nGör ditt val: ")

    while choice:

        if choice[0] == "1":
            print_playerlist(player)
            print("\n")

            a = int(input("Välj spelare nr 1: "))
            b = int(input("Välj spelare nr 2: "))
            if a == b:
                print("En spelare kan inte spela mot sig själv!")
            else:
                print("\n" + player[a].name, "vs", player[b].name, "!\n")
                print("--------------------------------------------\n")
                playmatch(player[a], player[b], FILENAME, FIRSTLINES, player)

        elif choice[0] == "2":
            print_playerlist(player)

        elif choice[0] == "3":
            print_resultlist(player)

        elif choice[0] == "5":
            print("Hejdå!")
            sys.exit()

        else:
            print("\nNågot blev fel!\n")

        print()

        choice = input("\n1. Spela match\n2. Visa spelare\n3. Visa resultat\n\nGör ditt val: ")


# Meny för val av händelser
# choice = '';
# while choice != 'S':
#       Välj två spelare som ska gå en match
#

main()
