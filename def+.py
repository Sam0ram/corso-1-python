lista = [1,2,3,4,5,6,7,8,9,10]
numero1 = 15
numero2 = 17
def is_in_list(elemento, lista):
    return elemento in lista

def somma_due_numeri(numero1, numero2):
    return numero1 + numero2


elemento = input ("Inserisci un numero:")

if elemento.isdigit():
    if is_in_list(int(elemento), lista):
        print("nella lista")
    else:
        print("non nella lista")
    print("Si tratta di un intero")
else:
    print("Una stringa")
