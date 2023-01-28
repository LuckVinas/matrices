tabla =[[],[]]
columna=int(input("de cuantas columnas quieres tu matriz"))
from random import randint
 
fila=0
while fila<5:
    
    columna =0
    while columna< len(tabla):
        tabla.append(randint(1,10))
        columna +=1
    fila +=1



print(tabla)