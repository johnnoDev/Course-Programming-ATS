"""
Ejercicio 2:
Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes listas (en las que no debe haber repeticiones):
    - Lista de elementos que aparecen en las dos listas.
    - Lista de elementos que aparecen en la primera lista, pero no en la segunda.
    - Lista de elementos que aparecen en la segunda lista, pero no en la primera.
    - Lista de elementos que aparecen en ambas listas. (Repetidos)
"""
lista_uno = [1, 2, 3, "Johnny", "Jose", "Carlos"]
lista_dos = [4, 5, 6, "Alexis", 1, 2, 3]


# 1.
# lista_uno = set(lista_uno)
# lista_dos = set(lista_dos)
# lista_union = list(lista_uno | lista_dos)
lista_union = list(set(lista_uno) | set(lista_dos))

# 2
lista_diferencia = list(set(lista_uno) - set(lista_dos))

# 3 
lista_diferencia_dos = list(set(lista_dos) - set(lista_uno))

# 4
lista_repetidos = list(set(lista_uno) & set(lista_dos))

print(lista_repetidos)