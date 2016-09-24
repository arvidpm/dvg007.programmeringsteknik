# Programmeringsteknik webbkurs KTH inlämningsuppgift 1.
# Arvid Persson
# 2015-01-08
#
# Detta är ett kort program som:
# 1. Tar ett fyrsiffrigt tal som indata till variabeln talet.
# 2. Kontrollerar så att talet är i intervallet 1-9999.
# 3. while-loop initieras.
# 4. Sorterar siffrorna och lagrar dessa i de nya variablerna a och b.
# 5. Beräknar differensen mellan a och b, skriver över variabeln talet.
# 6. Fortsätter på ovanstående sätt till vi fått talet 6174.
# 7. Printar ut antalet iterationer det tog att genomföra operationen.


# Inmatning av tal
talet = input("Ange ett fyrsiffrigt heltal (ex 1234): ")

# Kontroll att talet inom området
if int(talet) <= 0:
    print("Felaktigt värde, talet måste vara större än 0!")
    
elif int(talet) > 9999:
    print("Felaktigt värde, ange ett fyrsiffrigt tal!")

else:
    # Definerar konstant
    KAPREKAR = 6174

    # Definerar räknarens start
    antal_varv = 0

    while int(talet) != KAPREKAR:
        if len(talet) < 4:
            talet = "0" + talet
        else:
        
            # Sortering av talet
            a = int("".join(sorted(talet, reverse=True)))
            b = int("".join(sorted(talet)))

            # Subtraktion: a - b ersätter talet med ett nytt värde
            talet = str(a - b)
            antal_varv += 1

            # Jämförelse med Kaprekar
            if int(talet) == int(KAPREKAR):
                print("Det tog", antal_varv ,"iterationer att nå 6174.")
