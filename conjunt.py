# Conjunto de datos desordenados
conjunt = set()
conjunt = {5, 8, 5.99, "Hola", False}

# Agrega un elemento al conjunto.
conjunt.add(99)

# Busca y elimana el elemento.
conjunt.discard("Hola")

# Elimina todos los elementos del conjunto (queda vacío)
conjunt.clear()
print(conjunt)