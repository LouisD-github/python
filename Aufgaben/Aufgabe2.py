from random import *
min = int(input("Geben Sie die Zahlen in Minuten an: "))
h = min//60
min = min%60
sek = min%1
min = min - sek
sek = sek*60
sek = int(sek)
print(h, "h", min, "min", sek, "sek")

print()

print("Errate eine Zah von 1 bis 100: ")
z = randint(1,100)
print(z)
erraten = False
while erraten == False :
    r = input()
    if r.isnumeric() : 
        r = int(r)
        if r == z :
            print("Erraten!")
            erraten = True
        if r > z : 
            print("Eingabe ist zu groß!")
        if r < z :
            print("Eingabe ist zu klein!")
    else :
        print("Eingabe ist keine Zahl!")

print(" ")

s = input("Gebe zufällige Buchstaben und Zahlen ein: ")
zahlen = 0
buchstaben = ""
for char in s:
    if char.isnumeric():
        zahlen += int(char)
    else:
        buchstaben += char
    
print(zahlen, buchstaben)
input("Done")