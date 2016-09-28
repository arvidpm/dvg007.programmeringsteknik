# # Programmeringsteknik webbkurs KTH inlämningsuppgift P-uppgift
# Delmoment 2 - Prototyp
#
# Arvid Persson Moosavi
# 2016-09-27
#
# Detta är deluppgiften prototyp från huvuduppgiften Tennismatch
#
# Programmet fungerar i grova drag så att den läser indata från textfilen Spelarlista.txt
# I prototypuppgiften kollas inte filen, varken dess existens eller rimlig data.
# Ingen felkontroll görs utöver att en spelare inte kan spela en match mot sig själv.
#
# Programflöde:
# 1. main anropar createplayers med datafilen Spelarlista.txt.
# 2. Data läses och spelarobjekt skapas utifrån antalet rader i Spelarlista.txt, 4 rader per spelare.
# 3. Huvudmeny presenteras. Användaren väljer mellan att visa resultatlista/tillgängliga spelare, eller spela en match.
# 4. Spelas en match väljer användaren två kombatanter, dessa får inte vara densamma.
# 5. Matchen spelas, objekten uppdateras och ny data sparas till Spelarlista.txt
# 6. Laddas resultatlistan på nytt finns ny data tillgänglig sedan förra matchen.
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

    # Returnerar spelaren med attribut, samt formaterar för resultatlista
    def __str__(self):
        return '    {:15} {:>1} {:>8}   {}'.format(self.name, self.won, self.played, self.averagewon)



#---------- Funktioner för filkontroll, skapande av spelare, matcher, resultatuppdatering ------------


# Kontrollerar filens existens
def checkfile(FILENAME):

    if os.path.isfile(FILENAME):
        print(FILENAME, "laddad!")
    else:
        sys.exit("Spelarlista.txt kunde inte hämtas")


# Funktion som kontrollerar antalet rader i textfilen
def file_len(FILENAME):
    with open(FILENAME) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# En funktion som läser indata från FILENAME och sedan skapar objekt av Player
def createplayers(FILENAME, IGNORELINES):

    # Kontrollerar antalet rader i FILENAME
    num_lines = file_len(FILENAME)

    player_count = int( (num_lines-IGNORELINES) / 4)

    p = 0
    s = 0

    # Skapar arrays för data. v1 för att hålla objekten och v2 för att hålla attributen
    v1 = [None] * player_count
    v2 = [None] * 4


    with open(FILENAME, encoding="utf-8") as file:

        # Loopar igenom data från rad 5 till slutet av textfilen
        for line in islice(file, IGNORELINES, num_lines):

            # Tar bort radbyte
            line = line.replace('\n', '')

            if p < 3:

                # Varje rad sparas till element i v2
                v2[p] = line
                p += 1

            elif p == 3:

                # Sista spelarraden sparas till elementet i v2
                v2[p] = line

                # Beräknar snitt vunna matcher
                avg = round(( int(v2[2]) / int(v2[3]) ), 3)

                # Spelarobjekt skapas från datan till v1
                v1[s] = Player(v2[0], v2[1], v2[2], v2[3], avg)

                # Nollställer p, ökar s för nästa objekt
                p = 0
                s += 1

        # Returnerar lista med spelarobjekt
        return v1


# En funktion som simulerar en match mellan två valda spelare
def playmatch(player1, player2, FILENAME, IGNORELINES, player):

    player1.played = int(player1.played)+1
    player2.played = int(player2.played)+1

    result = randint(0, 1)

    if result == 0:
        player1.won = int(player1.won)+1
        print(player1.name, "won!")
    else:
        player2.won = int(player2.won)+1
        print(player2.name, "won!")

    player1.averagewon = round( (int(player1.won) / int(player1.played)), 3)
    player2.averagewon = round( (int(player2.won) / int(player2.played)), 3)

    print("--------------------------------------------\n")

    save(FILENAME, IGNORELINES, player)


# En funktion som raderar gammal och sparar ny data till Spelarlista.txt
def save(FILENAME, IGNORELINES, player):

    # Kontrollerar antalet rader i FILENAME
    num_lines = file_len(FILENAME)

    # Raderar befintlig data (totalt antal rader minus 5 första). Lämnar filen öppen
    oldlines = open(FILENAME).readlines()
    open(FILENAME, 'w').writelines(oldlines[:-(num_lines - IGNORELINES)])

    # Skriver ny data
    for i in player:
        with open(FILENAME, "a", encoding='utf-8') as file:
            file.write(str(i.name) + '\n')
            file.write(str(i.serveavg) + '\n')
            file.write(str(i.won) + '\n')
            file.write(str(i.played) + '\n')





# --------- Funktioner för gränssnitt -------------

def print_resultlist(player):

    player.sort(key=lambda player: player.averagewon, reverse=True)

    plac = 1
    print("\n----------------------------------------")
    print("Plac. Namn        Vunna  Spelade  %vunna")

    for i in player:
        print(plac, i)
        plac +=1
    print("----------------------------------------\n")


def print_playerlist(player):

    plac = 0
    print("\n----------------------------------------")
    print("Nr. Namn")

    for i in player:
        print(plac," ",i.name)
        plac += 1



# --------- Huvudprogrammet -----------------------

def main():



    # Refererar textfil till konstant
    FILENAME = '../resources/Spelarlista.txt'

    # Kontrollerar att filen finns
    checkfile(FILENAME)

    # Första raderna i textfilen ignoreras
    IGNORELINES = 5

    # Skapar spelarobjekt från data i textfilen
    player = createplayers(FILENAME, IGNORELINES)


    # --------- Huvudmenyn -----------------------
    choice = input("\nVälkommen till Tennisspelet!\n\n1. Spela match\n2. Visa spelare\n3. Visa resultat\n\n5. Avsluta\n\nGör ditt val: ")

    while choice:

        if choice[0] == "1":

            print_playerlist(player)
            print("\n")

            a = int(input("Välj spelare nr 1: "))
            b = int(input("Välj spelare nr 2: "))

            if a == b:
                print("En spelare kan inte spela mot sig själv!")

            else:
                print("\n"+player[a].name,"vs",player[b].name,"!\n")
                print("--------------------------------------------\n")
                playmatch(player[a], player[b], FILENAME, IGNORELINES, player)

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

        choice = input("\n1. Spela match\n2. Visa spelare\n3. Visa resultat\n\n5. Avsluta\n\nGör ditt val: ")


main()