
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
print("Lesmo\npuzza")# \n manda a capo
print ("lesmo \"puzza\"")
float_t = 3.0
sting = "3"
intero = 3
bool = False



#STRINGA
L = "LESMo"
print(L.lower()) # tutta var in minuscolo
print(L.upper()) # tutta var in MAIUSCOLO
print(L.isupper()) # tutta var o False o True (anche upper, ma solo se lo è tutto)
print(L.upper().isupper()) # si può fare di fila
print(len(L)) # letter nel testo
print(L[4]) # lettera specificata e si inizia sempre da zero in tutto
print(L.index("o")) # ci dice la posizione della lettera della str (si può fare con una o più lettere,)
print(L.index("SMo")) # esempio 2 sopra
print(L.replace("SMo", "LE")) # ripiazzi parte di varabile: print(variabile.replace("parte text da rimpizzare", "rimpiazzo"))



#NUMERI
N = 7
n = 2.14
N1 = -5
n1 = -9.23
print(3 * (N+4))
print(10%3) # resto
print(2**8) # elevazione a potenza
print(str(N)+str(N1 ), "sono la metà del totale delle stagioni")
print(abs(n1)) # ci da il valore assoluto (il numero con il segno +)
print(pow(abs(n1), 2)) # pow=** (entrambi elvamento a potenza, si possono mettere più di uno)
print(max(4, 6)) # il numero più grande
print(min(4, 6,)) # il numero più piccolo
print(max(4, 6, pow(5.234658, 6), pow(5.96354, 6))) # mettere di più insieme pt2
print(round(n)) # arrotonda il numero decimale a 1 cifra intera



#input
name = input("Inserisci il tuo nome: ")
age = input("Inserisci la tua età: ")
print ("Ciao", name+"!", "tu hai", age, "anni")



#basic calcolatrice
num1 = float(input("inserici un primo numero: "))
num2 = float(input("inserici un secondo numero: "))
result = num1+num2
print(result)



#LISTE
tabellina_5 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
family = ["mom", "dad", "brothers", "dog", "cat", "cousins"]
family2 = family.copy()
family[4] = "grandparents" # (nome_lista)[(posizione elemento)] = (sostituto)
print(family)
print(family[2])
print("my family =", family[0:3]) # dalla 1 alla 4, 1 incluso e 4 escluso
print(family[2:]) # prende tutto dalla seconda posizione compresa, si inizia SEMPRE da 0
#family.extend(tabellina_5)   # serve per stringe e variabili. se str allora aggiungie ogni carattere alla lista in modo separato, se lista/variabile, allora aggiunge tutti gli elementi della lista.
family.append("uncles")  # aggiunge elemento a fine lista
tabellina_5.insert(8, 55) #inserisce 55 nella posizione 8 (partendo da sempre da 0), la posizione 8 va a destra insieme a tutti gli elementi che vengono dopo 
family.remove("cousins") # come dice il nome lo rimuove
tabellina_5.clear() # rimuove tutti gli elementi della lista
family.pop() # rimuove ultimo elemento da lista
print(family.index("dad")) # in che posizione si trova
print(family.count("mom")) # quante volte appare un elemento specifico  nella listas
print(tabellina_5.reverse())
print(family.sort()) #mette in ordine alfabetico o numerico
print(tabellina_5)


#TOUPLES
cartesiano = (5,6) #gli elementi non possono essere aggiunti ne eleminati ne modificati. sono intoccabili. 
#cartesiano[0] = 1  #questo ci darebbe errore. le liste sono modificabili e usano "[]". touples NON sono modificabili e usano "()"
coordinate = [(1, 1), (5 ,3), (7,4)] #lista di tpouples, la lista si possono aggiungere elementi o rimuovere. ma le touple resta intoccabili. si possono rimuovere le touples_
# _dalla lista ma non i singoli elementi delle touple
coordinate.pop()
print(coordinate)
print(cartesiano)
print(cartesiano[0])

#import (da più funzioni, in questo caso di matematica), ("math" è un modulo)
from math import*
print(floor(9.6546532)) # solo num int
print(ceil(9.6546532)) # solo part decimale
print(sqrt(81)) # radice quadrata


#FUNZIONI:  sono un "blocco" di linee di codice che fanno una cosa, e qundo vogliamo eseguire quel blocco dobbiamo richiamarlo. per fare una funzione usiamo "def". servono per organizzare il codice
def say_hi(nome, age): # def (nome_funzione)(): e sotto le rige di codice. non succederà nulla se non viene richiamate per farla eseguire. possiamo aggiungere una variabile che verrà definita dopo. se ne possono mettere+1
    print("Ciao", nome +", tu hai", age, "anni")
say_hi("Sem", 14) # oer richiamarlo (nome_funzione)(definizione variabile se messo uno in precedenza)
say_hi("Jenno", 26) #in questo caso ne fa due perchè lo ho richiamato due volte



