a = {1, 2, 3, 8}
b = {3, 1, 2, 9}

# ¿El conjunto es igual?
# print(a == b)

# 1. Unión de conjuntos; operador: |
# c = a | b
# print(c)

# 2. Intersección de conjuntos; operador: &
# c = a & b
# print(c)

# 3. Diferencia de conjuntos; operador: -
c = a - b # Elementos que no se encuentran en a
print(c) # 8
c = b - a
print(c) # 9

# 4. Diferencia simétrica; operador ^
