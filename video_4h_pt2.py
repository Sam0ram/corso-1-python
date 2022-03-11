"""   
#def e return
from time import sleep


def cubico(numero):
    return numero**3 # return ci da tutto quello che c'è dopo il comando. se facissimo print(cubico(3)) non ci darebbe nulla
    print("ciao") # appena vede return tutto quello che c'è sotto non lo considera
risultato = cubico(6)
print(risultato)

# IF, ELSE, ELIF, COMPARISONS
is_male = False
is_tall = True

if is_male and is_tall:
    print("sei un maschio alto")
elif is_male and not is_tall:
    print("sei un maschio basso")
elif not is_male and not is_tall:
    print (" sei una femmina bassa")
elif not is_male and is_tall:
    print("sei una femmina alta")

def max_num(a, b, c):
    if a >= b and a >= c:
        return print(a, "è il numero più grande")
    elif b >= a and b>= c:
        return (b, "è il numero più grande")
    else:
        return (c, "è il numero più grande")
    
num1 = 3
num2 = 2
num3 = 10
print(max_num(num1, num2, num3))

# calcolatrice migliorata
num_1 = float(input("inserisci il primo numero: "))
op = input("inserisci l'operazione da svolgere: ")
num_2 = float(input("inserisci il secondo numero: "))

if op == "+":
   print (num_1+num_2)
elif op == "-":
    print(num_1-num_2)
elif op == "/":
    print(num_1/num_2)
elif op == "*":
    print(num_1*num_2)
else:
    print (" errore: operazione non valida ")
 
    
    
#dizionari #più facile da capire nell'esemio. comunque è (nome dizionario) = {
#  (chive) : "definizione", 
#} ogni chiave deve essere diversa

mese_conv = {
    "gen": "gennaio",
    "feb": "febbraio",
    "mar": "marzo",
    "apr": "aprile",
    "mag": "maggio",
    "giu": "giugno",
    "lug": "luglio",
    "ago": "agosto",
    "set": "settembre",
    "ott": "ottobre",
    "nov": "novembre",
    "dic": "dicembre"
}

# adesso si può accedere a quel dizionario

print(mese_conv.get("dec")) # print(nome_dizionario.get(chiave)). se metessimo(chive non esistente, "non c'è questa chiave") e facessimo print uscirebbe "non c'è questa chiave"
variabile1 = mese_conv["feb"]
print(variabile1)

#while loop: nel frattempo che una condizione è vera, fai questo processo (o serie di processi) in loop
i = 1
while i <= 10:
   print(i)
   i += 1
print("loop finito")


#indovina il numero gioco

num_segreto = 5
tentativo = None
num_tent = 0
max_tent = 3
tent_0 = False
while num_segreto != tentativo and not tent_0:
    if num_tent < max_tent:
      tentativo = float(input("insersci il numero segreto: "))
      num_tent += 1
    else:
        tent_0 = True

if tent_0:
    print("hai perso")
else:
    print("bravo hai indovinato.")
 
"for loop"
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for meri:
    print(i)
#elevamento a potenza

base_num = float(input("inserisci un numero: "))
esponente_num = float(input("a che poteza lo vuoi elevare?: "))
risultato = base_num**esponente_num
print("il risultato è: '"+str(risultato)+"'")
 
#griglia in 2D

from inspect import trace


num_griglia = [ 
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    [1, 2, 3, 4]
]

#for loop annidito
for i in num_griglia:
    for x in i:
        print(x)
#traduttore
def Traduzione (frase):
     traduzione = ""
     for lettera in frase:
         if lettera in ("AEIOUaeiou"):
             traduzione = traduzione + "g"
         else:
             traduzione = traduzione + lettera
     return(traduzione)
            
print(Traduzione(str(input("inserisci un frase: "))))
      
# try and excep: per frovare una cosa e se ci fosse un errore fare un'operazione

try:
    risultato = 1/0
    numero_z = int(input("inserisci un numero: "))
    print(risultato)
except ValueError:
    print("solo numeri interi")
except ZeroDivisionError as err:
    print(err)

# leggere file esterni
file_1 = open("ciao_1.txt", "r") # può essere cos' ("nome file", "r") "r"= read; "w": write; "r+" read and write; "a" append (agguingere info e basta)

print(file_1.readable()) #per capire se si può leggere
print(file_1.read()) #leggere tutto il file
print(file_1.readline()) # leggere prima riga
print(file_1.readline()) # legge seconda riga perchè la prima è stata letta prima
print(file_1.readlines()) # tutte le righe in un lista, si può specificare la riga facendo print(nome_var.redlines()[num_riga])
file_1.close() # bisogna poi chiuderlo

file = open("ciao_1.txt", "a") # se mettessi la "w" rescriverebbe tutto il file con solo le cose che metto dopo. ma se metto un'altro nome al file e metto "w" allora crerà un altro file
 
file.write("\nciao 11 (appesso)")
 
file.close


pyfile = open("strumenti_utili.py", "w")

pyfile.write("hi")
pyfile.close()
# moduli e pip


import strumenti_utili

print(strumenti_utili.dadi(10))
 

from strumenti_utili import prof
    
prof_fumagalli = prof("marco", False, 38)

print(prof_fumagalli._è_cattivo)
"""
import random

range_min = int(input("inserisci il valore minimo: "))
range_max = int(input("inserisci il valore massimo: "))
max_tent = int(input("inserisci il numero massimo di tentativi: "))

random_num = random.randrange(range_min, range_max)
print(random_num)
risposta = int
numero_tent = 0


while risposta is not random_num and numero_tent is not max_tent:
    numero_tent += 1
    risposta = int(input("indovina il numero: "))
    if risposta < random_num:
        print("il numero è più alto")
    elif risposta > random_num:
        print("il numero è più basso")
    elif risposta == random_num:
        print("bravo hai indovinato")
    if numero_tent == max_tent and risposta != random_num:
        print("non hai più tentativi perdente. HA! HA!")




