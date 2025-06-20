import random
import time

# Función de búsqueda lineal

def busqueda_lineal(lista, objetivo):
    pasos = 0
    for i in range(len(lista)):
        pasos += 1
        if lista[i] == objetivo:
            return i, pasos
    return -1, pasos

# Función de búsqueda binaria iterativa

def busqueda_binaria_iterativa(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    pasos = 0

    while inicio <= fin:
        pasos += 1
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio, pasos
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1, pasos

# Función de búsqueda binaria recursiva

def busqueda_binaria_recursiva(lista, objetivo, inicio=0, fin=None, pasos=0):
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return -1, pasos

    pasos += 1
    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return medio, pasos
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, fin, pasos)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, inicio, medio - 1, pasos)

# Programa principal

# Generamos una lista ordenada de 100 elementos
lista = sorted(random.sample(range(1, 200), 100))
print("Lista generada (ordenada):")
print(lista)

# Pedimos al usuario un número para buscar
objetivo = int(input("\nIngrese el número que desea buscar: "))

# Búsqueda lineal
print("\n--- Búsqueda Lineal ---")
indice, pasos = busqueda_lineal(lista, objetivo)
print(f"Resultado: {'Encontrado en índice ' + str(indice) if indice != -1 else 'No encontrado'}")
print(f"Pasos realizados: {pasos}")

# Búsqueda binaria iterativa
print("\n--- Búsqueda Binaria Iterativa ---")
indice, pasos = busqueda_binaria_iterativa(lista, objetivo)
print(f"Resultado: {'Encontrado en índice ' + str(indice) if indice != -1 else 'No encontrado'}")
print(f"Pasos realizados: {pasos}")

# Búsqueda binaria recursiva
print("\n--- Búsqueda Binaria Recursiva ---")
indice, pasos = busqueda_binaria_recursiva(lista, objetivo)
print(f"Resultado: {'Encontrado en índice ' + str(indice) if indice != -1 else 'No encontrado'}")
print(f"Pasos realizados: {pasos}")
