#Aufgabe 4.1
def berechne_dreieckswerte(katheten):
    a, b = katheten
    hypotenuse = (a**2 + b**2)**0.5
    flaecheninhalt = 0.5 * a * b
    return (a, b, hypotenuse, flaecheninhalt)

kath1 = float(input("Gebe Kathete 1 an: "))
kath2 = float(input("Gebe Kathete 2 an: "))
kathetentuple = (3.0, 4.0)
ergebnistuple = berechne_dreieckswerte(kathetentuple)
print("a, b, Hypotenuse, flächeninhalt")
print(ergebnistuple)

#Aufgabe 4.2
def pruefe(liste, dictionary):
    for wert in liste:
        if wert in dictionary:
            print("Listenwert: " + str(wert) + ", Dictionary-Key: " + str(dictionary[wert]))
        else:
            print("Der Key '" + str(wert) + "' ist nicht im Dictionary vorhanden.")

key_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}

beispiel_liste = ['a', 'b', 'c', 'd']

pruefe(beispiel_liste, key_dictionary)

#Aufgabe 4.3 
# ...

input("Done")