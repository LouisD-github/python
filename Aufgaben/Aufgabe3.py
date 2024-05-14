liste = [2, 5, 3, 8, 2, 7, 4, 6, 9, 2, 5, 8, 1, 3, 6]
print("Liste: ", liste)

#Aufgabe 3.1
def aufgabe1(liste):
   i = int(input("Gebe eine Zahl ein, welche aus der Liste entfernt werden soll:"))
   for x in liste:
      if i in liste:
         liste.remove(i)
   return liste

aufgabe1(liste)
print("Aufgabe 3.1 - Liste: ", liste)

#Aufgabe 3.2
def aufgabe2(liste):
   zahlen = []
   doppelt = []
    
   for x in liste:
        if x not in zahlen:
            zahlen.append(x)
        elif x not in doppelt:
            doppelt.append(x)
    
   for x in doppelt:
        zahlen.remove(x)

   for x in doppelt:
       zahlen.append(x) 
   
   return zahlen

liste = aufgabe2(liste)
print("Aufgabe 3.2 - Liste: ", liste)

#Aufgabe 3.3
def aufgabe3(liste):
   for z in range(len(liste)-1):
      for y in range(len(liste)-z-1):
         if(liste[y] > liste[y + 1]):
            temp = liste[y] 
            liste[y] = liste[y + 1]
            liste[y+1] = temp
   return liste

liste = aufgabe3(liste)
print("Aufgabe 3.3 - Liste: ", liste)

input("Done")