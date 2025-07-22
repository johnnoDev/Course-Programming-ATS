a = {1, 4, 10, 3}
b = {3, 7, 2, 9}

# ¿El conjunto es igual?
# print(a == b)

# 1. Unión de conjuntos; operador: |
# c = a | b
# print(c)

# 2. Intersección de conjuntos; operador: &
# c = a & b
# print(c)

# 3. Diferencia de conjuntos; operador: -
# c = a - b # Elementos que no se encuentran en a
# print(c) # 8
# c = b - a
# print(c) # 9

# 4. Diferencia simétrica; operador ^
# Son todos los números menos la intersección
# c = a ^ b
# print(f'Diferencia simétrica del conjunto a y b: {c}')

# 5. Determinar si es un subconjunto
# Conjunto inmutable coon el método frozenset
x = frozenset({1, 2, 7})
y = {4, 5, 8}
z = {1, 2, 3, 4, 5, 8}
# print(x.issubset(z)) # True

# 6. Determinar si es un super conjunto
# print(z.issuperset(y)) 

# 7. Determinar si un conjunto es disconexo (que no comparte ningún elemento en común)
# print(x.isdisjoint(y))

