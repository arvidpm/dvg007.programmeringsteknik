# Programmeringsteknik webbkurs KTH inlämningsuppgift 2.
# Arvid Persson
# 2015-01-12
#
# Detta är ett program som skapar en dikt av en inläst text.
# Programmet läser in fyra meningar och skriver sedan ut texten
# uppdelad på följande rader:
#
# Textens fyra första ord med stora bokstäver
# En tom rad
# Textens fyra första ord
# Resten av första meningen
# Textens fyra första ord igen
# Andra meningen
# Tredje meningen
# Fjärde meningen
# Textens fyra första ord en sista gång


# Skapar lista och import av sys-funktioner
import sys

# Bortkommenterat global variabel
# sentence = 4*[None]

# Skriver ut startinformation
def printInformation():
    print ("""
             ---------------------------------------------------
             |                  DIKTAUTOMATEN                  |
             |                                                 |
             |  Skriv in fyra meningar och få ut en rondelet!  |
             ---------------------------------------------------""")
    print("")

# Inmatning av meningar
def typeSentence():
    sentence = 4*[None]
    i = 0
    while i < 4:
        sentence[i] = input("Skriv din mening här: ")
        i += 1
    print("")
    
#   För testning
#   sentence[0] = "Det fanns ingen fil när jag handlade på Konsum."
#   sentence[1] = "Bananerna var också slut."
#   sentence[2] = "Jag köpte bröd istället."
#   sentence[3] = "Nån sorts limpa med mycket fibrer."

# Kontroll av första meningens längd
def checkSentence():
    sentenceList = sentence[0].split()  
    if (len(sentenceList) <= 4):  
        print("Första meningen måste vara fyra ord eller längre!")
        sys.exit()

# Split av första meningen och sammansättning
# av fyra första orden
def firstWords():
    firstList = sentence[0].split() 
    firstWords = " ".join(firstList[:4])
    return firstWords

# Split av första meningen och sammansättning
# av alla ord efter de första fyra
def lastWords():
    lastList = sentence[0].split() 
    lastWords = " ".join(lastList[4:])
    return lastWords

# Utskrift av text enligt instruktionerna
def printOut():
    print(firstWords.upper())
    print("")
    print(firstWords)
    print(lastWords)
    for i in range(1,4):
        print(sentence[i])
    print(firstWords)

# Huvudprogram
printInformation()
typeSentence()
checkSentence()
firstWords = firstWords()
lastWords = lastWords()
printOut()
