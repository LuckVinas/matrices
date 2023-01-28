nombres =[]
apellidos =[]
matriculas =[]
carreras =[]
promedios =[]
tamaño=10
calf=0
calificacion=0
j=1
for i in range(tamaño):
    print("ingresa los datos de la persona",i+1)
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    matricula = input("matricula: ")
    carrera = input("carrera: ")
    for j in range(10):
      calificacion=int(input("calificaciones: "))
      calf=calf+calificacion
      j=j+1
    
    j=1
    prom=calf/10
    nombres.append(nombre)
    apellidos.append(apellido)
    matriculas.append(matricula)
    carreras.append(carrera)
    promedios.append(prom)
    

if promedios[i] >=6:
 for i in range(tamaño):
    print("alumnos reprobados: ")
    print("nombre: ",nombres[i])
    print("apellido: ",apellidos[i])
    print("promedio: ",promedios[i])
    
elif promedios[i]<6:
    for i in range(tamaño):
        print("alumnos reprobados: ")
        print("nombre: ",nombres[i])
        print("apellido: ",apellidos[i])
        print("promedio: ",promedios[i])
        
        
