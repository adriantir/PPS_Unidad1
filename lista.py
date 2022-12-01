#Comprobamos si el numero esta en la lista
def estaEnLista(numero, lista):

    if numero in lista:
        print("El número " + str(numero) + " esta en la lista.")
    else:
        print("El número  " + str(numero) + " no  esta en la lista.")

# Se comprueba si el número está dentro del rango, si lo está entonces se chequea si está dentro de la lista.


def estaEnRango(valores, minimo, maximo):

    if valores < minimo or valores > maximo:
        print("El número " + str(valores) + " está fuera del rango de la lista")
        exit
    else:
        print("El número " + str(valores) + " está dentro del rango de la lista")

# Ejecución segura ante fallos, solo se permitirá numeros no letras.


try:
    lista = [6, 14, 11, 3, 2, 1, 15, 19]
    estaEnRango(5, 5, 10)
    estaEnLista(-1, lista)
except (ValueError, TypeError):
    print("Introduce un valor de forma correcta")
