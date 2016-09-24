# Programmeringsteknik webbkurs KTH inlämningsuppgift 2.
# Arvid Persson
# 2015-03-27
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


# Import av sys-funktioner
import sys

# Skriver ut startinformation
def print_information():
    print ("""
             ---------------------------------------------------
             |                  DIKTAUTOMATEN                  |
             |                                                 |
             |  Skriv in fyra meningar och få ut en rondelet!  |
             ---------------------------------------------------""")
    print("")

# Inmatning av meningar
def type_sentence():
    sentence = 4*[None]
##    För testning
##    sentence[0] = "Det fanns ingen fil när jag handlade på Konsum."
##    sentence[1] = "Bananerna var också slut."
##    sentence[2] = "Jag köpte bröd istället."
##    sentence[3] = "Nån sorts limpa med mycket fibrer."
    i = 0
    while i < 4:
        sentence[i] = input("Skriv in mening nr " + str(i+1) + ":")
        i += 1
    return sentence

# Kontroll av första meningens längd
def check_sentence(sentences):
    sentenceList = sentences[0].split()
    if (len(sentenceList) <= 4):
        print("Första meningen måste vara fyra ord eller längre!")
        sys.exit()

# Split av första meningen och sammansättning
# av fyra första orden
def first_words(sentences):
    firstList = sentences[0].split() 
    firstWords = " ".join(firstList[:4])
    return firstWords

# Split av första meningen och sammansättning
# av alla ord efter de första fyra
def last_words(sentences):
    lastList = sentences[0].split() 
    lastWords = " ".join(lastList[4:])
    return lastWords

# Utskrift av text enligt instruktionerna
def printout(sentences,split_first,split_last):
    print("\n"+split_first.upper()+"\n")
    print(split_first+"\n"+split_last+"\n"+split_first)
    for i in range(1,4):
        print(sentences[i])
    print(split_first)


# Huvudprogram
def main():
    print_information()
    sentences = type_sentence()
    check_sentence(sentences)
    split_first = first_words(sentences)
    split_last = last_words(sentences)
    printout(sentences,split_first,split_last)

# Initierar huvudprogram
main()
