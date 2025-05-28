'''
hola = 1
print(hola)

chau = 2
print(chau)

def suma_numero(n1, n2):
    resultado = n1 + n2
    return resultado

print(suma_numero(2, 4))
'''

#Cree un script para mostrar los primeros 100 números enteros positivos, comenzando desde el 1. 

#for i in range(1, 101):
#    print(i)

'''
def numero(n):
    for i in range(1, n):
        print(i)

numero(101)



def n2(num_maximo):
    bandera = True
    numero = 1
    while bandera:
        print(numero)
        numero = numero + 1
        if(numero ==  num_maximo):
            bandera = False

n2(101)
'''

# Cree un script que le solicite al usuario ingresar 10 números, y una vez ingresados, le muestre en pantalla cuál es el máximo,
#y en qué posición lo ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9, y 33,
#se le debería mostrar el mensaje “El mayor número ingresado es 89,
#y lo ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1. 

def ingreso_numeros():
    print("Ingrese 10 numeros ")
    lista = []
    for i in range(1, 11):
        lista.append(int(input("Ingrese un numero: ")))
    print(lista)
    posicion = 0
    mayor = lista[0]
    for i in range(1, 10):
        if(lista[i] > mayor):
            mayor = lista[i]
            posicion = i
    print("El mayor numero encontrado es: ", mayor, "y esta en la posicion: ", posicion + 1)
ingreso_numeros()


