import random

#Retorna un dado aleatorio     
def primario():
    last = 6 #default size 
    var1 = random.randint(0, last)
    if var1 == 1:
        print("El valor del dado es 1")
    elif var1 == 2:
        print("El valor del dado es 2")
    else:
        print(f'El valor del dado es {var1}')
    
#Retorna el valor y tamaño dado por el usuario    
def numberUser(value, tamanio):
    a = value
    b = tamanio
    if a < b:
        print(f"Valor valido!!, el valor del dado es: {a} y el tamanio es: {b}")
    else:
        print(f"Valor invalido por rango, valor del dado es: {a} y el tamanio es: {b}")

#main
if __name__ == "__main__":
    input("Buenas usuario!! \n")
    caracter = input("¿Quiere ingresar usted el valor y tamanio del dado? S/N: \n") 
    if caracter == 's' or caracter == 'S':
        user = True
    elif caracter == 'n' or caracter == 'N':
        user = False
    else:
        raise Exception("El caracter es incorrecto!!")

    if user:
        value = input("Ingrese numero del dado :\n")
        print(f'Numero ingresado: {value}')
        tamanio = input("Ingrese tamanio del dado : \n")
        print(f'Valor ingresado: {tamanio}')
        numberUser(value, tamanio)    
    else:
        print("Se lanzaran el dado de forma aleatoria")
        primario()
   
    
