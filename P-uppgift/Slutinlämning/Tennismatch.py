# Programmeringsteknik webbkurs KTH inlämningsuppgift P-uppgift
# Slutinlämning för P-uppgift Tennismatch
#
# Arvid Persson Moosavi
# 2016-10-05
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

import sys, os.path, time
from itertools import islice
from random import randint


# ---------- Klass Player som skapar spelarobjekt -----------
class Player:

    # Skapar nytt spelarobjekt
    def __init__(self, name, serveavg, m_won, m_played, average_won):
        self.name = name
        self.serveavg = serveavg
        self.won = m_won
        self.played = m_played
        self.averagewon = average_won

    # Returnerar spelaren med attribut, samt formaterar korrekt för resultatlista
    def __str__(self):
        return '    {:15} {:>1} {:>8}   {}'.format(self.name, self.won, self.played, self.averagewon)


# ---------- Funktioner för filkontroll ------------

# Kontrollerar filens existens
def checkfile(FILENAME):
    if os.path.isfile(FILENAME):
        print(FILENAME, "hittad!")
    else:
        sys.exit("Spelarlista.txt kunde inte hämtas")


# Funktion för att kontrollerar så varje spelare har fyra rader i FILENAME
def check_player_lines(IGNORELINES, LINES):
    playerlines = LINES - IGNORELINES

    if playerlines % 4 == 0:
        return
    else:
        sys.exit("Antalet spelarrader går inte jämnt upp!")


# Kontrollerar 1) att vunna matcher inte är fler än spelade, och 2) att vunnen serve inte är högre än 1.
def check_player_data(player):
    for pobject in player:

        if int(pobject.won) > int(pobject.played):
            print("Antalet vunna matcher (" + pobject.won + ") för spelare", pobject.name,
                  "kan inte vara fler än antalet spelade (" + pobject.played + ") !")
            sys.exit("Programmet avslutas.")
        elif float(pobject.serveavg) > float(1):
            print("Vunnen serve (" + pobject.serveavg + ") för", pobject.name, "kan inte vara större än 1!")
            sys.exit("Programmet avslutas.")


# ---------- Funktioner för skapande av spelare, matcher, resultatuppdatering, spara ny data till fil ------------

# Funktion som kontrollerar antalet rader i textfilen
def file_len(FILENAME):
    with open(FILENAME) as file:
        for index, item in enumerate(file):
            pass
    return index + 1


# En funktion som läser indata från FILENAME och sedan skapar objekt av Player
def createplayers(FILENAME, IGNORELINES, LINES):
    player_count = int((LINES - IGNORELINES) / 4)

    # playerelement, playerobject
    pelement = 0
    pobject = 0

    # Skapar arrays för data. v1 för att hålla objekten och v2 för att hålla attributen
    array1 = [None] * player_count
    array2 = [None] * 4

    with open(FILENAME, encoding="utf-8") as file:

        # Loopar igenom data från rad 5 till slutet av textfilen
        for line in islice(file, IGNORELINES, LINES):

            # Tar bort radbyte
            line = line.replace('\n', '')

            if pelement < 3:

                # Varje rad sparas till element i v2
                array2[pelement] = line
                pelement += 1

            elif pelement == 3:

                # Sista spelarraden sparas till elementet i v2
                array2[pelement] = line

                # Beräknar snitt vunna matcher
                averagewon = round((int(array2[2]) / int(array2[3])), 3)

                # Spelarobjekt skapas från datan till v1
                array1[pobject] = Player(array2[0], array2[1], array2[2], array2[3], averagewon)

                # Nollställer p, ökar s för nästa objekt
                pelement = 0
                pobject += 1

        # Returnerar lista med spelarobjekt
        return array1


# En funktion med lite felkontroll som förbereder en match mellan två spelare
def selectplayers(FILENAME, IGNORELINES, LINES, player):
    print_playerlist(player)
    print()
    print("Avbryt matchen genom att ange '5' på någon av raderna.\n")

    # Inmatning av spelare
    p1 = int(input("Välj spelare nr 1: "))
    p2 = int(input("Välj spelare nr 2: "))

    # Om 5, avbryt matchen
    if p1 == 5 or p2 == 5:
        print("\nMatchen avbruten!")
        return

    # Om spelarnr >=3 så är detta för högt
    elif p1 >= (player.__len__()-1) or p2 >= (player.__len__()-1):
        print("\nSpelarnummer kan inte vara högre än "+str((player.__len__()-1)))
        selectplayers(FILENAME, IGNORELINES, LINES, player)

    elif p1 == p2:
        print("\nEn spelare kan inte spela mot sig själv!")

    else:
        print("\n" + player[p1].name)
        time.sleep(0.5)
        print("vs")
        time.sleep(0.5)
        print(player[p2].name)
        time.sleep(2)

        print("--------------------------------------------")
        playmatch(player[p1], player[p2], FILENAME, IGNORELINES, LINES, player)


# En funktion som simulerar en match mellan två valda spelare
def playmatch(player1, player2, FILENAME, IGNORELINES, LINES, player):
    player1.played = int(player1.played) + 1
    player2.played = int(player2.played) + 1

    result = randint(0, 1)

    if result == 0:
        player1.won = int(player1.won) + 1
        print(player1.name, "won!")
    else:
        player2.won = int(player2.won) + 1
        print(player2.name, "won!")

    player1.averagewon = round((int(player1.won) / int(player1.played)), 3)
    player2.averagewon = round((int(player2.won) / int(player2.played)), 3)

    print("--------------------------------------------\n")

    savefile(FILENAME, IGNORELINES, LINES, player)


# En funktion som raderar gammal och sparar ny data till Spelarlista.txt
def savefile(FILENAME, IGNORELINES, LINES, player):

    # Raderar befintlig data (totalt antal rader minus de 5 första). Lämnar filen öppen
    oldlines = open(FILENAME).readlines()
    open(FILENAME, 'w').writelines(oldlines[:-(LINES - IGNORELINES)])

    # Skriver ny data, "a" = append
    for pobject in player:
        with open(FILENAME, "a", encoding='utf-8') as file:
            file.write(str(pobject.name) + '\n')
            file.write(str(pobject.serveavg) + '\n')
            file.write(str(pobject.won) + '\n')
            file.write(str(pobject.played) + '\n')


# --------- Funktioner för gränssnitt -------------

# Utsrift av resultatlista sorterat på spelare från högst till lägst vinstsnitt.
# Den ordinarie ordningen är från lägst till högst men reverseras genom reverse=True
def print_resultlist(player):
    player.sort(key=lambda player: player.averagewon, reverse=True)

    plac = 1
    print("\n----------------------------------------")
    print("Plac. Namn        Vunna  Spelade  %vunna")

    for pobject in player:
        print(plac, pobject)
        plac += 1
    print("----------------------------------------")

# Utskrit av spelarlista, utan sortering, tagna i samma ordning som de listas i textfilen
def print_playerlist(player):
    plac = 0
    print("\n----------------------------------------")
    print("Nr. Namn")

    for pobject in player:
        print(plac, " ", pobject.name)
        plac += 1

    print("----------------------------------------")


# --------- Huvudprogrammet -----------------------

def main():
    # Refererar textfil till konstant
    FILENAME = '../resources/Spelarlista.txt'

    # Kontrollerar att filen finns
    checkfile(FILENAME)

    # Konstant för att ignorera första raderna i FILENAME
    IGNORELINES = 5

    # Kontrollerar antalet rader i FILENAME
    LINES = file_len(FILENAME)

    # Kontrollerar att varje spelare i FILENAME har fyra rader
    check_player_lines(IGNORELINES, LINES)

    # Skapar spelarobjekt från data i textfilen
    player = createplayers(FILENAME, IGNORELINES, LINES)

    # Kontrollerar rimlig spelardata
    check_player_data(player)

    # --------- Huvudmenyn -----------------------

    print()
    print('   ,odOO"bo,')
    print(" ,dOOOP'dOOOb,")
    print(",O3OP'dOO3OO33,")
    print('P",ad33O333O3Ob')
    print('?833O338333P",d')
    print("`88383838P,d38'")
    print(" `Y8888P,d88P'")
    print('   `"?8,8P"'"")
    print()

    choice = input(
        "Välkommen till Tennisspelet!\n\n1. Spela match\n2. Visa spelare\n3. Visa resultat\n\n5. Avsluta\n\nGör ditt val: ")

    while choice:

        if choice[0] == "1":
            selectplayers(FILENAME, IGNORELINES, LINES, player)

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
