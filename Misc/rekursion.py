def summa(n):
    if n > 1:
        return summa(n-1) + n
    else:
        return 1

print("Välkommen till summaberäkningsprogrammet!")
n = int(input("Vilket tal ska vara det sista i summan? "))
print("Summan = ", summa(n))
