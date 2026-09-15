# Ejercicio 6
# Dada una secuencia de caracteres, obtener dicha secuencia invertida.
# La solución debe realizarse utilizando recursividad.


# Función recursiva que invierte una secuencia de caracteres
def invertir_secuencia(secuencia):

    # Caso base:
    # si la secuencia tiene 0 o 1 carácter, ya está invertida
    if len(secuencia) <= 1:
        return secuencia

    # Llamada recursiva:
    # toma desde el segundo carácter hasta el final
    # y luego agrega el primer carácter al final
    return invertir_secuencia(secuencia[1:]) + secuencia[0]


# Pedimos al usuario que ingrese una secuencia
secuencia = input("Ingrese una secuencia de caracteres: ")

# Llamamos a la función recursiva
secuencia_invertida = invertir_secuencia(secuencia)

# Mostramos el resultado
print("Secuencia original:", secuencia)
print("Secuencia invertida:", secuencia_invertida)