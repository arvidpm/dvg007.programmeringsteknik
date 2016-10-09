import random

# Skriver ut informationsrutan
def visaInformation():
    print ("""
             ---------------------------------------------------
             |          VEM HAR DEN SNABBASTE SNIGELN?         |
             |                                                 |
             |  Här får din snigel tävla mot en vältränad      |
             |  racersnigel. Skriv in namnet på din snigel     |
             |  så sätter tävlingen igång!                     |
             ---------------------------------------------------""")

# Läser in namnet på användarens snigel
# UT: returnerar namnet på snigeln
def lasNamn():
    namn = input("Vad heter din snigel? ")
    return namn

# Simulerar en tävling mellan två sniglar
# UT: slumpade nummer för snigelbana1 och snigelbana2
def tavling():
    snigelbana1 = 0
    snigelbana2 = 0
    print("Klara...färdiga...gå! \n")
    while snigelbana1 < DISTANS and snigelbana2 < DISTANS:
        snigelbana1 += random.randrange(5)
        snigelbana2 += random.randrange(5)
    return snigelbana1, snigelbana2

# Ritar en snigelbana
# IN: snigelnamn = namnet på snigeln
#     langd = längden på snigelns bana        
def ritaBanan(snigelnamn,langd):
    print(snigelnamn.rjust(12) + ":", end=" ")
    for i in range(1,langd):
        print("-", end = " ")    #slemspåret
    print("@")         # snigeln

# Skriver ut vinnaren
# IN: langd1 = längden på snigel 1's bana 
#     langd2 = längden på snigel 2's bana 
#     namn1 = namnet på snigel 1
#     namn1 = namnet på snigel 2
def utseVinnare(langd1, langd2, namn1, namn2="Racersnigeln"):
    print(langd1, langd2)
    print("\n")
    if langd1 >= DISTANS and langd2 >= DISTANS:
        print("Det blev oavgjort.")
    else:
        if langd1 >= DISTANS:
            print("Det här loppet tog en oväntad vändning," , namn1, "vann!")
        else:
            print(namn2, "vann, som vanligt.")


DISTANS = 30
visaInformation()
dinSnigelsNamn = lasNamn()
snigelbana1, snigelbana2 = tavling()
ritaBanan(dinSnigelsNamn,snigelbana1)
ritaBanan("Racersnigeln",snigelbana2)
utseVinnare(snigelbana1, snigelbana2, dinSnigelsNamn)
