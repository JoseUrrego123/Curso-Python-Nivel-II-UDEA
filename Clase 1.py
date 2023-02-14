print("Bienvenidos al curso de Python nivel 2")
print("Hola mundo")

#Esto es un comentario de una sola linea
'''Esto 
es un comentario de 
varias lineas'''

#Tipos de datos

Numero=10
print(Numero)
print(type(Numero))

Flotante=50.25
print(Flotante)
print(type(Flotante))

Booleano=True
print(type(Booleano))

suma=Numero+Flotante
print(type(suma))

texto="Curso python nivel 2"
print(type(texto))

#Operadores aritmeticos

a=10
b=20
suma=a+b
print("La suma de los dos numeros es: ",suma)

resta=a-b
print(f"El resultado de la resta es: {resta}")

mult=a*b
print("El resultado de la multiplicacion es: {}".format(mult))

division=a/b
division_ent=a//b
print("El resultado de la division es: {0} y el resultado de la division entera es: {1}".format(division,division_ent))

potencia=a**b
print(f"El valor de la potencia es: {potencia}")

modulo=a%b
print("El residuo de la division entre {0} y {1} es {2}".format(a,b,modulo))

# Operadores logicos

a=10
b=20
c=30

resultado1=(a>b) and (c>b)
print(resultado1)

resultado2=(a>b) or (c>b)
print(resultado2)

#Operadores de asignacion

a=1
b=1
c=1
d=1
e=1

a+=1 #a=a+1
print(a)
b-=1
print(b)
c*=10
print(c)
d/=5
print(d)

'''print("Calculadora basica, validar operacion dependiendo la letra")

print("Que operacion desea realizar: \n\
      S para sumar\n\
      R para restar\n\
      M para multiplicar\n\
      D para dividir\n")
opcion=input("Digite la opcion: ").lower()

num1=eval(input("Digite el primer numero: "))
num2=eval(input("Digite el segundo numero: "))

if (opcion=="s"):
    resultado=num1+num2
elif (opcion=="r"):  #else if
    resultado=num1-num2
elif (opcion=="m"):
    resultado=num1*num2
elif (opcion=="d"):
    if (num2!=0):
        resultado=num1/num2
    else:
        print("No es posible realizar la operacion")
        quit()

else:
    print("El caracter digitado no es valido")
    quit()

print("\nEl resultado de la operacion es: {}".format(resultado))'''

#Listas (Vectores)

Lista=["Jose","Alejandro","Urrego",1,2,3,4,5,True]
print("Primer digito en la lista: ",Lista[0])
print("Segundo elemento en la lista: ",Lista[1])
print(Lista[-1])
print(Lista[:3])
print(Lista[3:9])

Lista.append(10)
print(Lista)
Lista.extend([20,30,40,50])
print(Lista)

Lista+=[60,70,80,90]
print(Lista)

Lista+=[10,10,10,10]
print(Lista.count(10))
print(Lista.index(10))

del Lista[0:2]
print(Lista)

Lista2=Lista.copy()
print(Lista2)

Lista.pop(5)
print(Lista)

Lista.remove("Urrego")
print(Lista)

Lista.reverse()
print(Lista)

Lista.clear()
print(Lista)

#Tuplas 

#Tuplas ()
#Listas []

Tupla=(1,2,3,4,5,6,"python",1,1,1)

print(Tupla)
print(Tupla.index(1))
print(Tupla.count(1))
print(len(Tupla))

Lista=list(Tupla)
print(type(Lista))

Tupla2=tuple(Lista)
print(type(Tupla2))

#Diccionarios {key1:valor1,key2:valor2,key3:valor3}

diccionario={"Python":1,"JavaScript":2,"CSS":3}
print(diccionario)

print(len(diccionario))

print(diccionario["JavaScript"])

diccionario["C++"]=4
print(diccionario)

diccionario["etc"]={10,20,30}
print(diccionario)

alumnos={1:["Pepito","Perez"],2:["Peranito","Perez"],3:["Juanito","Jaramillo"]}

if 1 in alumnos:
    print(alumnos[1])
else:
    print("El alumno 1 no existe")

if 4 in alumnos:
    print(alumnos[4])
else:
    print("El alumno 4 no existe")

print(alumnos.get(1,"El alumno 1 no existe"))
print(alumnos.get(4,"El alumno 4 no existe"))


empresa={
    "Empleados":[
    {"Nombre":"Jose Alejandro","Edad":23},
    {"Nombre":"Juan Carlos","Edad":27},
    {"Nombre":"Daniel Esteban","Edad":29}
    ],
    "Maquinas":[
    {"Tipo":"Inyectora","Marca":"Siemmens"},
    {"Tipo":"PLC","Marca":"Siemmens"},
    {"Tipo":"Imporesora 3D","Marca":["2020","2022"]}
    ]
}

print(empresa["Empleados"][1]["Edad"])
print(empresa["Maquinas"][2]["Marca"][1])

#Estructuras de repeticion

#For (yo se la cantidad de iteraciones) y el while (Cuando no las se)

'''dividendo=eval(input("Ingrese el dividendo: "))
divisor=eval(input("Ingrese el divisor: "))

while divisor==0:
    print("Ingresaste mal el divisor, intentalo de nuevo: ")
    divisor=eval(input())
division=dividendo/divisor
print("El resultado de la division es: ",division)

#Ciclo for

Universidad={
    "Alumnos":[
    {"Nombre":"Jose Alejandro", "Especialidad":"Desarrollo de software"},
    {"Nombre":"Daniel Esteban","Especialidad":"Automatizacion"},
    {"Nombre":"Juan carlos","Especialidad":"CFD"}
    ],
    "Profesores":[
    {"Nombre":"Pepito perez","Grado":"Doctorado"},
    {"Nombre":"Juanito","Grado":"Maestria"},
    {"Nombre":"Peranito","Grado":"Doctorado"}

    ]
}

print("ALUMNOS")
for i in Universidad["Alumnos"]:
    print("Nombre: ",i["Nombre"], "Especialidad: ",i["Especialidad"])

print("PROFESORES")
for i in Universidad["Profesores"]:
    print("Nombre: ",i["Nombre"], "Especialidad: ",i["Grado"])'''

#Exceptciones
#Validar division correcta

'''a=eval(input("Digite el primer numero: "))
b=eval(input("Digite el segundo numero: "))
try:
    resultado=a/b
    print("El resultado es: {}".format(resultado))
except Exception as err:
    print("No fue posible realizar la operacion", err)'''

#Validar indice correcto de una lista

'''lista=[]
a=eval(input("Digite un primer valor: "))
lista.append(a)
b=eval(input("Digite un segundo valor: "))
lista.append(b)

try:
    print("El indice es: ", lista[5])
except Exception as err:
    print("No fue posible realizar la busqueda ", err)'''


# POO (Programacion orientada a objetos)

# Clase: Objeto

# Atributos: Caracteristicas del objeto (variables)

#Metodos: Acciones que realiza el objeto (funciones)

class Auto():
    #Atributos publicos
    color=""
    modelo=""
    marca=""
    encendido=False
    velocidad=0

    #Atributos privados
    __llave=""

    #Metodos publicos

    def __init__(self,llave,color,modelo,marca): #Metodo que me sirve para inicializar
        self.__llave=llave
        self.color=color
        self.marca=marca
        self.modelo=modelo
    
    def encender(self,llave):
        if self.__llave==llave:
            self.encendido=True
            print("El auto esta encendido")
        else:
            print("La llave es incorrecta")

    def acelera(self):
        if self.encendido==True:
            self.velocidad=self.velocidad+10

    def frena(self):
        if self.velocidad>0:
            self.velocidad=self.velocidad-10
            self.__luzfreno()
    
    def apaga(self):
        if self.encendido==True:
            self.encendido=False
            self.velocidad=0

    #Metodo privados
    def __luzfreno(self):
        print("La luz del freno esta ecendida")


Carro=Auto("12345","Blanco","2015","Ford")
Carro.encender("12345")
Carro.acelera()
Carro.acelera()
Carro.acelera()
Carro.acelera()
print(Carro.encendido)
print(Carro.velocidad)
Carro.frena()
Carro.frena()
print(Carro.velocidad)
print(Carro.color)

Carro2=Auto("102030","Negro","2020","Nissan")
Carro2.encender("102030")
Carro2.acelera()
Carro2.acelera()
Carro2.acelera()
Carro2.acelera()
Carro2.acelera()
print(Carro2.encendido)
print(Carro2.velocidad)


    










