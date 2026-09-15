# Ejercicio 15
# Desarrollar una función que permita calcular la raíz cuadrada entera
# de un número entero utilizando recursividad.


# Función auxiliar recursiva
def buscar_raiz(numero, candidato):

    # Caso base:
    # La raíz cuadrada entera es el mayor número entero
    # cuyo cuadrado no supera al número ingresado.
    # Por ejemplo: la raíz cuadrada entera de 20 es 4,
    # porque 4² = 16 y 5² = 25.
    if (candidato + 1) * (candidato + 1) > numero:
        return candidato

    # Llamada recursiva:
    # probamos con el siguiente número
    return buscar_raiz(numero, candidato + 1)


# Función principal
def raiz_cuadrada_entera(numero):

    # Si el número es negativo, no podemos calcular
    # una raíz cuadrada entera real
    if numero < 0:
        return None

    # Comenzamos a buscar desde 0
    return buscar_raiz(numero, 0)


# Pedimos un número al usuario
numero = int(input("Ingrese un número entero: "))

# Calculamos la raíz cuadrada entera
resultado = raiz_cuadrada_entera(numero)

# Mostramos el resultado
if resultado is None:
    print("No se puede calcular la raíz cuadrada entera de un número negativo.")
else:
    print("La raíz cuadrada entera de", numero, "es:", resultado)