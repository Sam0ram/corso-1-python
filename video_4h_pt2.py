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
"""    
    
    
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
    print("hai perso!!")
else:
    print("bravo hai indovinato")
    