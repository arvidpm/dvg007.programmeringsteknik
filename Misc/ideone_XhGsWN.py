# Programmeringsteknik webbkurs KTH inlämningsuppgift 3.
# David Henriksson
# 20150808
# Program som simulerar ett besök på ett nöjesfält

import random
import time # För dramatiska pauser

# Klass som beskriver en besökare.
#
# Attribut:
#   alder - Besökarobjektets ålder.
#   mood - Besökarens 'humör'. Går den över tio har besökare för roligt.
#
class Visitor:

    def __init__(self, alder):
        self.age = alder
        self.mood = 0

    def __str__(self):
        return str(self.age) + " * " + str(self.mood)

    # Besökarklassen slutar här
    # ------------------------

# Klass som beskriver en attraktion/åktur på nöjesfältet.
#
# Attribut:
#   name - attraktionens namn
#   typ - typ av attraktion
#   duration - attraktionens varaktighet i minuter
#   ex_fact - spänningsfaktor
#   restrict - åldersgräns
#   info - kort information om åkturen
#
class Attraktion:

    def __init__(self,attraktionsnamn,typ,varaktighet,spänningsfaktor,åldersgräns,info):
        self.name = attraktionsnamn
        self.typ = typ
        self.duration = varaktighet
        self.ex_fact = spänningsfaktor
        self.restrict = åldersgräns
        self.info = info

    def __str__(self):
        return self.name + '/' + self.typ + '/"' + self.info + '"'

    # Starta en åktur
    def ride_start(self,user_choice):
        ''' Startar en åktur

            param user_choice: heltal, pekar på index i lista 'introfraser'
        '''

        print()
        print("Välkommen till " + self.name + "!")

        # Varierande introduktionsfraser, tillhörande olika attraktionstyper
        introfraser = [
                "-- Byglarna spänns fast, och vagnarna börjar sakta röra sig",
                "-- Dörrarna stängs (o)lustigt bakom dig när du klivit in i huset",
                "-- Vagnen gnisslar olycksbådande när hjulet sätts i rörelse"
                ]

        # Skriver ut tre punkter med en sekunds mellanrum, för immersionskänsla
        def suspense():
            for i in range(3):
                time.sleep(1)
                print(".",end="",flush=True)
            print(" --")

        # Om parameter user_choice inte återfinns i 'introfraser', skriv ut standardfras
        if int(user_choice) > len(introfraser):
            print("-- Attraktionen sätter igång med ett mycket oroande brak",end="",flush=True)
            suspense()
        else:
            print(introfraser[user_choice],end="",flush=True)
            suspense()

    def ride_mid(self):
        ''' Skriver ut slumpmässiga fraser baserat på åkturens varaktighet
        '''

        # Några immersionsfraser
        immersionsfraser = [
                "IIIH!",
                "WAAAAAH!",
                "HAHAHAAAA!!",
                "HERREGUUU..",
                "KYAAAAAH!",
                "HJÄÄÄLP!"
                ]

        print("Till höger och vänster hörs andra människor ropa i - vad du bara kan hoppas på är -\n"
                "skräckblandad förtjusning:",flush=True)
        for i in range(0,self.duration):
            time.sleep(1)
            print(random.choice(immersionsfraser),flush=True)

    def accident(self,user_choice):
        ''' Simulerar en olycka, sannolikhet baserat på åkturens spänningsfaktor

            param user_choice: heltal, pekar på index i lista olycksfraser
        '''

        # Varierande immersionsfraser vid olycka, tillhörande olika attraktionstyper
        olycksfraser = [
            'I en plötslig explosion känner du din kropp disintegreras bit för bit, \n'
            'och du inser sakta men säkert att du har blivit till konfetti i \n'
            'regnbågens alla färger. Någonstans hörs en röst tala till dig: \n'
            '"Konfetti är allt världen behöver."',
            'Golvet under dig rasar samman, och du faller nedåt i ett bottenlöst hål. \n'
            'Någonstans hörs en röst tala till dig: \n'
            '"Du verkar ha hamnat i en oändlig tidsloop. Beklagar."',
            'Hjulet lossnar från sin axel och börjar rulla iväg, för att aldrig synas igen. \n'
            'Du känner saliv rinna från din mungipa i en cirkelbana runt ditt ansikte, \n'
            'och du börjar ångra ditt val av attraktion. \n'
            'Någonstans hörs en röst tala till dig: \n'
            '"Livet är fyllt av dåliga beslut."'
            ]

        # Tar global variabel 'not_accident'
        global not_accident

        print("Plötsligt hör du ett konstigt ljud, och en olustig \n"
                "känsla infinner sig - något har gått sönder")
        time.sleep(2)
        print()
        print(olycksfraser[user_choice],end="",flush=True)

        # not_accident sätt till False för att ange att en olycka har inträffat
        not_accident = False

    def ride_end(self,Visitor):
        ''' Avslutar åkturen

            param Visitor: Tar ett besökarobjekt
        '''

        print("Efter vad som verkar ha varat en evighet (" + str(self.duration) + " minuter) \n"
            "verkar äntligen åkturen vara slut. Du känner dig utmattad i själen.")

        # Ökar på besökarens humör-attribut med åkturens spänningsfaktor
        Visitor.mood += self.ex_fact

    def ride(self,Visitor,val):
        ''' Simulerar en hel åktur från start till slut, med eventuellt inslag av olycka

            param Visitor: Tar ett besökarobjekt
            param val: Tar ett heltal
        '''

        # Skriv ut attraktionsinfo och låt användaren avgöra om denne vill åka eller inte
        print(self.name + ' är en attraktion av slaget ' + self.typ + ', med tag-linen '
                + '"' + self.info + '"')
        user_choice = input('Vill du testa "' + self.name + '"? (J/n): ') or 'j'
        while user_choice.lower()[0] == 'j' or user_choice.lower()[0] == 'y':
            # Kolla besökarobjekts ålder mot attraktionens åldersgräns
            if Visitor.age >= self.restrict:
                while True:
                    # Kolla olycksrisk baserat på attraktionens spänningsfaktor
                    olycksrisk = random.randrange(100)
                    # Olycksscenario
                    if olycksrisk <= (self.ex_fact*10):
                        self.ride_start(val)
                        self.ride_mid()
                        self.accident(val)
                        return False
                    # Vanlig åktur
                    else:
                        self.ride_start(val)
                        self.ride_mid()
                        self.ride_end(Visitor)
                        return False
            else:
                print()
                print('Vakten vid attraktionen tittar dömande ut dig, och säger sedan: \n'
                     '"Du är för liten för den här. Stick iväg, kisen!"')
                break



def get_info():
    ''' Tar input från användare kring vilken attraktion denne vill veta mer om.

    Returns: användarens val
    '''

    print()
    print('"Jag är inte på prathumör idag, håll dig kortfattat. Vad vill du veta mer om?", frågar '
            'clownen.')
    while True:
        try:
            global val
            val = int(input('[1: Berg- och dalbanan, 2: Lustiga huset, 3: Pariserhjulet]'
                ', 4: Lämna nöjesfältet]: '))
            # Endast värden mellan 1-4 tillåtna
            if int(val) < 1 or int(val) > 4:
                raise Exception
            # Gör om valet för att passa index i listor
            val = val - 1
            return val
        # Endast numeriska värden tillåtna
        except ValueError:
            print('"Jag kan inte läsa, okej? Ge mig siffrorna bara."')
        except Exception:
            print('"Kul skämt, ge mig en av dom här siffrorna nu bara:"')

# Huvudprogram
def main():
    # Skapar global variabel 'not_accident' och sätter den till True
    global not_accident
    not_accident = True

    # "Startar" programmet
    while True:
        print('''

                Du befinner dig vid grindarna till ett nöjesfält. På en skylt kan du läsa:
                          "VÄLKOMMEN TILL RUTTNEBUK! - Ett helt okej nöjesfält"
                Du går fram till biljettkassan och möts av en person som skulle kunna vara
                din spegelbild, om det inte vore för den enorma mustaschen.

Personen i kassan frågar dig ''')

        # Skapa ett besökarobjekt, och ta input från användare för ålder
        # Avslutar program ifall ingen godtycklig ålder anges
        try:
            visitor = Visitor(int(input('"Hur gammal är du då, slyngel?": ')))
        except ValueError:
            print()
            print('"Det där ser inte ut som någon ålder i siffror, vad jag vet. \n'
            'Det var banne mig det sjukaste jag har sett, du får gå hem!"')
            print('Du lämnar nöjesfältet med en bitande sorg i ditt hjärta, och med en \n'
                    'övertygelse om att alltid svara i siffror hädanefter.')
            return False

        print('"' + str(visitor.age) + ' år? Det har jag hört ska vara den gyllene åldern. Närå, \n'
                'jag har inget begrepp om vare sig tid eller rum, så jag vet faktiskt'
                ' inte. Välkommen!')
        print()
        print('Du traskar in på området och kikar dig omkring. En bit framför dig är ett \n'
                'informationsbås uppställt. Där står en clown som dystert sparkar'
                ' stenar på marken.\n'
                'Du går fram till clownen för att höra vad nöjesfältet erbjuder för nöjen.')

        # Startar informationsclownen
        while True:
            get_info()
            # Avslutar programmet
            if val == 3:
                print('Tack för besöket!')
                return False
            # Startar attraktionen som användaren valt
            ATTRAKTIONER[val].ride(visitor,val)
            print()

            # När besökarobjektets humörsattribut överstiger 10 avslutas programmet
            # (Man får inte ha hur roligt som helst)
            if visitor.mood > 10:
                print('Din själ är nu så utmattad att den inte längre kan hålla ihop fibrerna \n'
                        'som utgör din existens. Din kropp förvandlas till socker och sprids \n'
                        'över backen. Ett sötsuget barn kommer och slickar i sig det mesta av '
                        'vad som en gång varit du. \n'
                        'Tack för besöket!')
                return False
            # Ifall olycka har inträffat avslutas programmet
            elif not_accident == False:
                print()
                print('Osis med olyckan där hörru, men tack för besöket. Välkommen åter!')
                return False
            # Loopar informationsclownen
            else:
                print('Du återvänder till clownen vid informationsbåset.')


# Lista med tillgängliga attraktioner
ATTRAKTIONER = [
        Attraktion("The Lyfe","Berg- och dalbana",2,3,15,"Snabb som vinden, litegrann som en tax."),
        Attraktion("Das Haus","Lustigt Hus",5,2,10,"Ditt nya hem."),
        Attraktion("Hjulet - En uppfinning","Pariserhjul",2,1,0,"Lev riskfritt, dö gammal.")
        ]

# Starta huvudprogram
main()
