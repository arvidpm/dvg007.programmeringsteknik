# -*- coding: latin-1 -*-
#
#    Ett program som fixar med en kodbok s� att man kan 
#    h�lla reda p� sina koder i en fil. Det �r inte
#    krypterat s� man kan tjuvl�sa, men det skall jag
#    fixa i n�sta version.
#

import sys
class CodeBook(object):

   # Skapa en kodbok med samma inneh�ll som filen
   def __init__(self,filename):
       self.data =[] # H�r lagras alla koder (objekt av klassen Code)
       f=open("KodBok.txt","r")
       self.accessCode =int(f.readline().strip()) # H�r lagras kodbokens hemliga nycken.
       
       while True:
           namn = f.readline().strip()
           if namn =="":
               break
           kod = int(f.readline())
           c = Code(kod, namn)
           self.addCode(c)
      
       f.close()
   

   #Lagra hela kodboken p� en fil
   def save(self,filename):
       f=open("KodBok.txt","w")
       f.write(str(self.accessCode))
       for c in self.data:
           f.write("\n")
           f.write(c.getName()+"\n")
           f.write(str(c.getCode()))
       f.close()
   

   # Kolla om koden �r r�tt.
   def checkCode(self,accessCode):
       return self.accessCode == accessCode
   

   # L�gg till en ny kod.
   def addCode(self,myCode):
      self.data.append(myCode)
   

   # Sl� upp en kod. Om koden saknas eller om accesskoden �r
   # fel s� returneras 0.
   def getCode(self,name,accessCode):
       if self.accessCode == accessCode:
           return self.lookUp(name)
       else:
           return 0
   

   def lookUp(self,name):
      for c in self.data:
         if c.getName()==(name):
            return c.getCode()
        
      return 0


class Code:
    def __init__(self, code,name):
        self.__code = code
        self.__name = name
    
    def getCode(self):
        return self.__code
        
    def getName(self):
        return self.__name




def vaelj_alternativ():
   print( "1: Sl� upp en kod")
   print( "2: L�gg till en ny kod")
   print( "3: Avsluta")
   print()

   svar = int(input(">"))
   return svar


def slaaUpp():
    svar = input("Vilken kod s�ker du?")
    print (c.getCode(svar, huvudKod))

def laeggTill():
    namn=input("Vad g�ller kod (textstr�ng)?")
    kod =int(input("Vad �r koden (siffror)?"))
    kaad = Code(kod, namn)
    c.addCode(kaad)


SLAA_UPP = 1
LAEGG_TILL = 2
SLUTA = 3

c = CodeBook("CodeBook.txt")
print ("V�lkommen till kodboken 'CodeBook.txt'")
svar=int(input("Ange din hemliga kod:"))
huvudKod = int(svar)
if c.checkCode(huvudKod)==False:
    print ("DET VAR FEL! H�RDDISKEN RADERAS! HAHAHA!")
    sys.exit(0)

val = 0
while val!=SLUTA:
    val=vaelj_alternativ()
    if val == SLAA_UPP:
        slaaUpp()
    elif val == LAEGG_TILL:
        laeggTill()
c.save("CodeBook.txt")
print ("Ha en bra dag!")


