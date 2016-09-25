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
    def preparematch(self, player1, player2):
        return

    # En funktion som uppdaterar resultatlistan
    def resultlist(self, player1, player2):
        return

    # En funktion som sparar ny data till Spelarlista.txt
    def save(self, player1, player2, FILENAME):
        return



# Huvudprogram
def main():

    # Kontroll av filens existens och rimlig indata
    # if FILENAME !EXIST {
    #   sys.exit("Meddelande")
    # }
    # elif DÅLIG INDATA {
    #   sys.exit("Meddelande")
    # }


    # En funktion som läser indata från FILENAME och sedan skapar objekt av Player
    def playerdata(FILENAME):

        return

        # Whileloopa igenom FILENAME och skapa spelarobjekt baserat på indatan
        # player = Player[indata1, indata2, indata3, indata4]


    FILENAME = 'Spelarlista.txt'
    match = Match(FILENAME)

    # Meny för val av händelser
    # choice = '';
    # while choice != 'S':
    #       Välj två spelare som ska gå en match
    #       Match.preparematch(player1, player2)
