"""
Ejercicio 1:
Escriba un programa donde tenga una lista y que, a continuación, elime los elementos repetidos, por último mostrar la lista.
"""

lista = [7,8,9,7,7,6]

# conjunto = set(lista)
# lista = list(conjunto)
# Refactor:
lista = list(set(lista))


print(lista)