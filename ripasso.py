var = 4 + 3 + 1
var2 = "Ventilatore"

if var == 8:
    print("é vero")
else:
    print("non è vero")


lista = [0, 1, 2, 3, 4, 5, 6, 7,  var, 9, 10 ]
print(lista)

for i in lista:
    print(i)

#liste "a fette"
#prende le prime tre parti della lista visto che partiamo dal numero zero e andiamo fino al terzo compreso. quindi abbiamo l'1, il 2 el il 3 elemento
lista_spezzata = lista[0:3]

print(lista_spezzata)
 # a fette da "print"

print (lista[0:3])

# "il passo nelle leiste"

print (lista[0:5:2]) #prende il secondo elemento facendo passi due a due
print (lista[0:5:3]) #prende il terzo elemento facendo passi tre a tre

# IN = se è presente nella lista
if 5 in lista:
    print("il numero 5 è nella lista")
else:
    print("il numero 5 NON è presente nella lista")


#import sys
#sys.exit() quando si esegue il codice questo comando fa fermare il codice dal punto del comando in giù
elemento = input ("unserisci un numero: ")
elemento = int(elemento)


if elemento in lista:
    print ("Il numero che hai inserito è nella lista")
else:
    print("il numero che hai insetito NON  è nella lista")

#CONCATENZAIONE liste usando il +
lista1 = [0, 1, 2, 3, 4, 5 ]
lista2 = [5, 6, 7,  var, 9, 10 ]

lista3 = lista1+lista2
print(lista3)

#MOLTIPLICARE una lista x volte in modo tale che la lista si ripeta x volte nella stessa lista di partenza
lista12 = [ 1, 2, 3 ]
var12 = lista12*3
print (var12)

#la lunghezza di una lista. mi esce il numero di elementi presenti nella mia lista

lunghezza_lista = len(lista)
print(lunghezza_lista)

#minimo e massimo di una lista di int.

minimo = min(lista)
print(minimo)

massimo = max(lista)
print(massimo)

print("l'elemento minimo di queata lista è", )

input = input()
print(input)