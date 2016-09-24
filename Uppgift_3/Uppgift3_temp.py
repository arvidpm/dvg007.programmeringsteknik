import random, sys

# Programmeringsteknik webbkurs KTH inlämningsuppgift 3.
# Robin Chowdhury
# 2014-08-06
# Ett nöjesfält där man får välja mellan 3 åkturer
# Det finns en chans att åkturen man åker med havererar

# Attraktion för nökesfältet.
# Har funktioner för att starta, stoppa, skriva reklam.
# Denna klass använder man för att skapa åkturer till nöjesfältet
class Attraction:
	"""Attaktion för nöjesfältet"""
	def __init__(self, name, lengthreq, passengers, excitementlevel ):
		self.name = name
		self.lengthReq = lengthreq
		self.passengers = passengers
		self.excitementLevel = excitementlevel
		self.wreckedList = ["exploderade!", "blev till aska!", "blev upäten av en drake!"]
		self.introText = ""
		self.stopSound = ""
		self.excitementSound = ""

	# Används för att starta åkturen
	# Finns en chans att åkturen havererar då den startas.
	def start(self):
		print()
		if random.randrange(0,3) == 0:
			self.wrecked()
			self.stop()
		else:
			print(self.excitementSound)
			self.stop()


	# Då åkturen stannar kallas denna
	def stop(self):
		print(self.stopSound, self.name, "har stannat.")

	# Om åkturen går sönder så kallas denna
	def wrecked(self):
		print("Oh, nej! Något fel hände!")
		print(self.name, self.wreckedList[random.randrange(0,3)])


	# Denna används för att för att beskriva åkturen lite
	def printcommercial(self):
		print()
		print("Så du vill åka", self.name)
		print(self.introText)
		print("Du måste vara längre än", self.lengthReq, "cm för att åka den här")
		if self.excitementLevel > 9000:
			excite = "Livsfarlig"
		elif self.excitementLevel > 20:
			excite = "Spännande"
		else:
			excite = "Rolig"
		print (self.name, "klassas som", excite)
		print("Är du säker på att du vill åka denna?")

	def __str__(self):
		return self.name

# Huvudprogrammet

# Här initieras alla objekt som ska användas.
# De ges även egna ljud (textformat) samt introtexter
rides = [Attraction("Extrema åket", 140, 30, 9421), Attraction("Släppet", 150, 16, 32),
Attraction("Lilla åket", 90, 20, 4)]
rides[0].introText ="Detta åk är den farligaste, snabbaste och mest dödliga attraktionen på nöjesfältet"
rides[0].excitementSound = "AAAhhhhhhhhhh!"
rides[0].stopSound ="Screeeeech!"
rides[1].introText ="Ett 200 m fritt fall. Hoppas att du inte är höjdrädd!"
rides[1].excitementSound = "Whooooooo!"
rides[1].stopSound ="Klonk!"
rides[2].introText ="Perfekt för dem små knattarna. Eller ganska tråkig för dem också"
rides[2].excitementSound = "Weeeeeee!"
rides[2].stopSound ="Gnissel!"

# Här sker det som användaren kommer att få se.
# Alla valalternativ samt flödet av programmet.
print()
print("Välkommen till Spännande åk! Världens bästa nöjespark!")
while True:
	print()
	print("Vilken attraktion vill du åka?")
	for i in range(len(rides)):
		print(rides[i], "[" + str(i) + "]", end = "     ")
	print("Avsluta [q]")
	ride = input()
	if ride == "q":
		sys.exit(9)
	ride = int(ride)
	if ride < len(rides):
		rides[ride].printcommercial()
		choice = input("[y/n]")
		if choice[0] == "y":
			rides[ride].start()
	else:
		print("Den åkturen finns inte, var god välj en annan")
