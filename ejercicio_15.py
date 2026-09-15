# TP 4 - Lista
# Ejercicio 15
# Lista de entrenadores Pokémon utilizando "lista de lista".


# ----------------------------------------------------------
# TDA LISTA
# ----------------------------------------------------------

class Nodo:
    def __init__(self, info):
        self.info = info
        self.siguiente = None


class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


# Permite indicar el campo por el cual se ordenará la lista.
def criterio(dato, campo=None):
    if campo is None:
        return dato
    return dato[campo]


# Inserta un dato de manera ordenada.
def insertar(lista, dato, campo=None):
    nodo = Nodo(dato)

    # Si la lista está vacía o el dato debe ir al principio.
    if lista.inicio is None or criterio(dato, campo) < criterio(lista.inicio.info, campo):
        nodo.siguiente = lista.inicio
        lista.inicio = nodo

    else:
        anterior = lista.inicio
        actual = lista.inicio.siguiente

        # Buscamos la posición en la que debe insertarse.
        while actual is not None and criterio(actual.info, campo) <= criterio(dato, campo):
            anterior = actual
            actual = actual.siguiente

        nodo.siguiente = actual
        anterior.siguiente = nodo

    lista.tamanio += 1


# Busca un elemento por nombre.
def buscar_por_nombre(lista, nombre):
    actual = lista.inicio

    while actual is not None:
        if actual.info["nombre"].lower() == nombre.lower():
            return actual

        actual = actual.siguiente

    return None


# ----------------------------------------------------------
# FUNCIONES PARA CREAR LOS DATOS
# ----------------------------------------------------------

def crear_pokemon(nombre, nivel, tipo, subtipo):
    return {
        "nombre": nombre,
        "nivel": nivel,
        "tipo": tipo,
        "subtipo": subtipo
    }


def crear_entrenador(nombre, torneos, perdidas, ganadas):
    return {
        "nombre": nombre,
        "torneos": torneos,
        "batallas_perdidas": perdidas,
        "batallas_ganadas": ganadas,

        # Cada entrenador tiene su propia lista de Pokémon.
        # Por eso este ejercicio utiliza una "lista de lista".
        "pokemons": Lista()
    }


# Agrega un Pokémon a la lista de un entrenador.
def agregar_pokemon(entrenador, pokemon):
    insertar(entrenador["pokemons"], pokemon, "nombre")


# ----------------------------------------------------------
# CARGA DE DATOS
# ----------------------------------------------------------

entrenadores = Lista()


# Entrenador 1
ash = crear_entrenador("Ash Ketchum", 8, 18, 82)

agregar_pokemon(ash, crear_pokemon("Pikachu", 90, "Eléctrico", None))
agregar_pokemon(ash, crear_pokemon("Charizard", 88, "Fuego", "Volador"))
agregar_pokemon(ash, crear_pokemon("Bulbasaur", 72, "Planta", "Veneno"))


# Entrenador 2
misty = crear_entrenador("Misty", 4, 20, 80)

agregar_pokemon(misty, crear_pokemon("Starmie", 76, "Agua", "Psíquico"))
agregar_pokemon(misty, crear_pokemon("Psyduck", 55, "Agua", None))
agregar_pokemon(misty, crear_pokemon("Wingull", 64, "Agua", "Volador"))


# Entrenador 3
brock = crear_entrenador("Brock", 2, 35, 65)

agregar_pokemon(brock, crear_pokemon("Onix", 74, "Roca", "Tierra"))
agregar_pokemon(brock, crear_pokemon("Geodude", 60, "Roca", "Tierra"))
agregar_pokemon(brock, crear_pokemon("Geodude", 62, "Roca", "Tierra"))


# Entrenador 4
cynthia = crear_entrenador("Cynthia", 10, 5, 95)

agregar_pokemon(cynthia, crear_pokemon("Garchomp", 96, "Dragón", "Tierra"))
agregar_pokemon(cynthia, crear_pokemon("Roserade", 84, "Planta", "Veneno"))
agregar_pokemon(cynthia, crear_pokemon("Spiritomb", 86, "Fantasma", "Siniestro"))


# Entrenador 5
diantha = crear_entrenador("Diantha", 5, 15, 85)

agregar_pokemon(diantha, crear_pokemon("Tyrantrum", 82, "Roca", "Dragón"))
agregar_pokemon(diantha, crear_pokemon("Gardevoir", 91, "Psíquico", "Hada"))


# Entrenador 6
leon = crear_entrenador("Leon", 7, 10, 90)

agregar_pokemon(leon, crear_pokemon("Terrakion", 89, "Lucha", "Roca"))
agregar_pokemon(leon, crear_pokemon("Cinderace", 87, "Fuego", None))


# Insertamos los entrenadores ordenados por nombre.
for entrenador in (ash, misty, brock, cynthia, diantha, leon):
    insertar(entrenadores, entrenador, "nombre")


# ----------------------------------------------------------
# FUNCIONES PARA RESOLVER LOS PUNTOS
# ----------------------------------------------------------

# Devuelve la cantidad de Pokémon de un entrenador.
def cantidad_pokemons(entrenador):
    return entrenador["pokemons"].tamanio


# Devuelve el entrenador con mayor cantidad de torneos.
def entrenador_mas_torneos(lista):
    actual = lista.inicio
    mayor = None

    while actual is not None:
        if mayor is None or actual.info["torneos"] > mayor["torneos"]:
            mayor = actual.info

        actual = actual.siguiente

    return mayor


# Devuelve el Pokémon de mayor nivel.
def pokemon_mayor_nivel(lista_pokemons):
    actual = lista_pokemons.inicio
    mayor = None

    while actual is not None:
        if mayor is None or actual.info["nivel"] > mayor["nivel"]:
            mayor = actual.info

        actual = actual.siguiente

    return mayor


# Muestra todos los datos de un entrenador y sus Pokémon.
def mostrar_entrenador(entrenador):
    print("Nombre:", entrenador["nombre"])
    print("Torneos ganados:", entrenador["torneos"])
    print("Batallas ganadas:", entrenador["batallas_ganadas"])
    print("Batallas perdidas:", entrenador["batallas_perdidas"])
    print("Pokémon:")

    actual = entrenador["pokemons"].inicio

    while actual is not None:
        pokemon = actual.info

        if pokemon["subtipo"] is None:
            subtipo = "Sin subtipo"
        else:
            subtipo = pokemon["subtipo"]

        print(
            "-",
            pokemon["nombre"],
            "| Nivel:", pokemon["nivel"],
            "| Tipo:", pokemon["tipo"],
            "| Subtipo:", subtipo
        )

        actual = actual.siguiente


# Calcula el porcentaje de batallas ganadas.
def porcentaje_batallas_ganadas(entrenador):
    total = entrenador["batallas_ganadas"] + entrenador["batallas_perdidas"]

    if total == 0:
        return 0

    return entrenador["batallas_ganadas"] * 100 / total


# Determina si hay un Pokémon de un tipo determinado.
def tiene_tipo(lista_pokemons, tipo):
    actual = lista_pokemons.inicio

    while actual is not None:
        if actual.info["tipo"].lower() == tipo.lower():
            return True

        actual = actual.siguiente

    return False


# Determina si existe un Pokémon con tipo y subtipo determinados.
def tiene_tipo_y_subtipo(lista_pokemons, tipo, subtipo):
    actual = lista_pokemons.inicio

    while actual is not None:
        pokemon = actual.info

        if (
            pokemon["tipo"].lower() == tipo.lower()
            and pokemon["subtipo"] is not None
            and pokemon["subtipo"].lower() == subtipo.lower()
        ):
            return True

        actual = actual.siguiente

    return False


# Calcula el promedio de nivel de los Pokémon.
def promedio_nivel(entrenador):
    actual = entrenador["pokemons"].inicio
    suma = 0
    cantidad = 0

    while actual is not None:
        suma += actual.info["nivel"]
        cantidad += 1
        actual = actual.siguiente

    if cantidad == 0:
        return 0

    return suma / cantidad


# Busca si un entrenador tiene un Pokémon determinado.
def entrenador_tiene_pokemon(entrenador, nombre_pokemon):
    return buscar_por_nombre(entrenador["pokemons"], nombre_pokemon)


# Determina si un entrenador tiene Pokémon repetidos.
def tiene_pokemon_repetido(entrenador):
    actual = entrenador["pokemons"].inicio
    vistos = set()

    while actual is not None:
        nombre = actual.info["nombre"].lower()

        if nombre in vistos:
            return True

        vistos.add(nombre)
        actual = actual.siguiente

    return False


# ----------------------------------------------------------
# A) Cantidad de Pokémon de un determinado entrenador.
# ----------------------------------------------------------

nombre_a = "Ash Ketchum"
entrenador_a = buscar_por_nombre(entrenadores, nombre_a)

print("a) Cantidad de Pokémon de", nombre_a, ":")

if entrenador_a is not None:
    print(cantidad_pokemons(entrenador_a.info))
else:
    print("Entrenador no encontrado.")


# ----------------------------------------------------------
# B) Entrenadores con más de tres torneos ganados.
# ----------------------------------------------------------

print("\nb) Entrenadores con más de tres torneos ganados:")

actual = entrenadores.inicio

while actual is not None:
    if actual.info["torneos"] > 3:
        print("-", actual.info["nombre"])

    actual = actual.siguiente


# ----------------------------------------------------------
# C) Pokémon de mayor nivel del entrenador
#    con mayor cantidad de torneos ganados.
# ----------------------------------------------------------

mejor_entrenador = entrenador_mas_torneos(entrenadores)
mejor_pokemon = pokemon_mayor_nivel(mejor_entrenador["pokemons"])

print("\nc) Entrenador con más torneos:", mejor_entrenador["nombre"])
print("Pokémon de mayor nivel:", mejor_pokemon["nombre"])
print("Nivel:", mejor_pokemon["nivel"])


# ----------------------------------------------------------
# D) Mostrar todos los datos de un entrenador
#    y sus Pokémon.
# ----------------------------------------------------------

nombre_d = "Misty"
entrenador_d = buscar_por_nombre(entrenadores, nombre_d)

print("\nd) Datos del entrenador y sus Pokémon:")

if entrenador_d is not None:
    mostrar_entrenador(entrenador_d.info)
else:
    print("Entrenador no encontrado.")


# ----------------------------------------------------------
# E) Entrenadores cuyo porcentaje de batallas ganadas
#    sea mayor al 79 %.
# ----------------------------------------------------------

print("\ne) Entrenadores con más del 79 % de batallas ganadas:")

actual = entrenadores.inicio

while actual is not None:
    porcentaje = porcentaje_batallas_ganadas(actual.info)

    if porcentaje > 79:
        print("-", actual.info["nombre"], "-", round(porcentaje, 2), "%")

    actual = actual.siguiente


# ----------------------------------------------------------
# F) Entrenadores que tengan Pokémon de tipo fuego y planta
#    o agua/volador.
# ----------------------------------------------------------

print("\nf) Entrenadores con Pokémon fuego y planta, o agua/volador:")

actual = entrenadores.inicio

while actual is not None:
    lista_pokemons = actual.info["pokemons"]

    fuego_y_planta = (
        tiene_tipo(lista_pokemons, "Fuego")
        and tiene_tipo(lista_pokemons, "Planta")
    )

    agua_volador = tiene_tipo_y_subtipo(
        lista_pokemons,
        "Agua",
        "Volador"
    )

    if fuego_y_planta or agua_volador:
        print("-", actual.info["nombre"])

    actual = actual.siguiente


# ----------------------------------------------------------
# G) Promedio de nivel de los Pokémon
#    de un determinado entrenador.
# ----------------------------------------------------------

nombre_g = "Ash Ketchum"
entrenador_g = buscar_por_nombre(entrenadores, nombre_g)

print("\ng) Promedio de nivel de los Pokémon de", nombre_g, ":")

if entrenador_g is not None:
    print(round(promedio_nivel(entrenador_g.info), 2))
else:
    print("Entrenador no encontrado.")


# ----------------------------------------------------------
# H) Cantidad de entrenadores que tienen
#    un determinado Pokémon.
# ----------------------------------------------------------

pokemon_h = "Pikachu"
cantidad_entrenadores = 0

actual = entrenadores.inicio

while actual is not None:
    if entrenador_tiene_pokemon(actual.info, pokemon_h) is not None:
        cantidad_entrenadores += 1

    actual = actual.siguiente

print(
    "\nh) Cantidad de entrenadores que tienen a",
    pokemon_h + ":",
    cantidad_entrenadores
)


# ----------------------------------------------------------
# I) Entrenadores que tienen Pokémon repetidos.
# ----------------------------------------------------------

print("\ni) Entrenadores que tienen Pokémon repetidos:")

actual = entrenadores.inicio
hay_repetidos = False

while actual is not None:
    if tiene_pokemon_repetido(actual.info):
        print("-", actual.info["nombre"])
        hay_repetidos = True

    actual = actual.siguiente

if not hay_repetidos:
    print("No hay entrenadores con Pokémon repetidos.")


# ----------------------------------------------------------
# J) Entrenadores que tengan Tyrantrum,
#    Terrakion o Wingull.
# ----------------------------------------------------------

print("\nj) Entrenadores con Tyrantrum, Terrakion o Wingull:")

actual = entrenadores.inicio

while actual is not None:
    tiene_alguno = (
        entrenador_tiene_pokemon(actual.info, "Tyrantrum") is not None
        or entrenador_tiene_pokemon(actual.info, "Terrakion") is not None
        or entrenador_tiene_pokemon(actual.info, "Wingull") is not None
    )

    if tiene_alguno:
        print("-", actual.info["nombre"])

    actual = actual.siguiente


# ----------------------------------------------------------
# K) Determinar si un entrenador X tiene al Pokémon Y.
#    Los dos nombres deben ser ingresados por el usuario.
# ----------------------------------------------------------

print("\nk) Buscar un Pokémon dentro de un entrenador:")

nombre_entrenador = input("Ingrese el nombre del entrenador: ")
nombre_pokemon = input("Ingrese el nombre del Pokémon: ")

entrenador = buscar_por_nombre(entrenadores, nombre_entrenador)

if entrenador is None:
    print("El entrenador no se encuentra en la lista.")

else:
    pokemon = entrenador_tiene_pokemon(
        entrenador.info,
        nombre_pokemon
    )

    if pokemon is None:
        print(
            entrenador.info["nombre"],
            "no tiene al Pokémon",
            nombre_pokemon
        )

    else:
        print("\nDatos del entrenador:")
        print("Nombre:", entrenador.info["nombre"])
        print("Torneos ganados:", entrenador.info["torneos"])
        print("Batallas ganadas:", entrenador.info["batallas_ganadas"])
        print("Batallas perdidas:", entrenador.info["batallas_perdidas"])

        print("\nDatos del Pokémon:")
        print("Nombre:", pokemon.info["nombre"])
        print("Nivel:", pokemon.info["nivel"])
        print("Tipo:", pokemon.info["tipo"])

        if pokemon.info["subtipo"] is None:
            print("Subtipo: Sin subtipo")
        else:
            print("Subtipo:", pokemon.info["subtipo"])