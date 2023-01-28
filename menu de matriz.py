from tkinter import Menu


matriz=[[],[]]
fila=0
columna=0
Menu=""""
Bienvenido al menu de la matriz escoje una opcion:
[1] quieres rellenar toda la matriz
[2] deseas sumar una fila de tu eleccion 
[3] deseas sumar una columna de tu eleccion 
[4] deseas sumar la diagonal principal 
[5] deseas sumar la diagonal inversa 
[6] deseas obtener la media de la matriz 
"""
print(Menu)
opc=int(input("escoje una opcion "))
if opc ==1:
    print("a continuacion se te pediran los numeros")
    i=0
    while i<4:
        j=0
        while j<4:
         num=int(input("ingresa un numero"))
         num.appened(matriz[i],[j])
        j +=1
    i +=1
elif opc==2:
    num=int(input("que fila deseas sumar"))
    if num<len(matriz):
        suma=0
        for i in range(len(matriz)):
            suma=suma+matriz[i]
            print("la suma es: ", suma)
elif opc==3:
    num=int(input("que columna deseas sumar"))
    if num<len(matriz):
        suma=0
        for j in range(len(matriz)):
            suma=suma+matriz[j]
            print("la suma es : ", suma)
        
elif opc==4:
    print(" la suma es : ", matriz[0][0]+matriz[-1][-1]+matriz[-2][-2]+matriz[-3][-3])
elif opc==5:
    print(" la suma es : ", matriz[1][0]+matriz[-1][-2]+matriz[-2][-1]+matriz[-3][-1])
elif opc==6:
    while fila< len(matriz):
     columna =0
    while columna< len(matriz):
        suma=suma+matriz[fila][columna]
        print("la media es: ",suma/16)
        columna +=1
    fila +=1
else:
 print("opcion fuera de rango ")

    
    
    