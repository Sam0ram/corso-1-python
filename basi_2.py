#STRINGA (str) attenzione ai doppi apici
nome = "Samed"

# NUMERO INTERO (int) numero SENZA virgola e SENZA doppi apici
età = 14
dita_piedi = 10
dita_mani = 10
print (dita_piedi+dita_mani)
var = dita_piedi+dita_mani
# NON si possono mescolare int e str

#l'unico modo per farlo è mettendo la virgola che sostituisce lo spazio e la somma. in sintesi non si può sommare str e int
print ("io sono", nome, "e ho", età,".", "io ho", dita_piedi, "dita dei piedi e", dita_mani, "dita delle mani.", "in totale ho", var, "dita.")
#conversione da "int" a "str" 
eta_int = (14)
testo = ("la mia eta è: " )
print (testo+str(eta_int))

testo = "In italia si diventa maggiorenni a questa eta: "
intero = 20
testo2 = "io sono maggiorenne pechè la mia età è: "
intero2 = 18
print (testo+str(intero2)+" "+testo2+ str(intero)) 
