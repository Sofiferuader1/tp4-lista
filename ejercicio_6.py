# TP 4 - Lista
# Ejercicio 6
#
# Dada una lista de superhéroes de comics, de los cuales se conoce:
# nombre, año de aparición, casa de comic (Marvel o DC) y biografía.


# Clase Nodo
# Cada nodo guarda la información de un superhéroe
# y un enlace al siguiente nodo.
class Nodo:
    def __init__(self, info):
        self.info = info
        self.siguiente = None


# Clase Lista
# Guarda el inicio de la lista y su tamaño.
class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


# Permite elegir por qué campo se quiere comparar.
def criterio(dato, campo=None):
    if campo is None:
        return dato
    return dato[campo]


# Inserta un elemento de manera ordenada.
def insertar(lista, dato, campo=None):

    nodo = Nodo(dato)

    # Si la lista está vacía o el dato debe ir primero.
    if lista.inicio is None or criterio(dato, campo) < criterio(lista.inicio.info, campo):
        nodo.siguiente = lista.inicio
        lista.inicio = nodo

    else:
        anterior = lista.inicio
        actual = lista.inicio.siguiente

        # Buscamos la posición correcta.
        while actual is not None and criterio(actual.info, campo) < criterio(dato, campo):
            anterior = actual
            actual = actual.siguiente

        nodo.siguiente = actual
        anterior.siguiente = nodo

    lista.tamanio += 1


# Busca un elemento dentro de la lista.
def buscar(lista, buscado, campo=None):

    actual = lista.inicio

    while actual is not None:

        if criterio(actual.info, campo) == buscado:
            return actual

        actual = actual.siguiente

    return None


# Elimina un elemento de la lista.
def eliminar(lista, clave, campo=None):

    actual = lista.inicio
    anterior = None

    while actual is not None:

        if criterio(actual.info, campo) == clave:

            # Si es el primer nodo.
            if anterior is None:
                lista.inicio = actual.siguiente

            else:
                anterior.siguiente = actual.siguiente

            lista.tamanio -= 1
            return actual.info

        anterior = actual
        actual = actual.siguiente

    return None


# Creamos la lista de superhéroes.
superheroes = Lista()


# Cargamos datos de ejemplo.
datos = [
    {
        "nombre": "Batman",
        "anio": 1939,
        "casa": "DC",
        "biografia": "Utiliza un traje especial para combatir el crimen."
    },
    {
        "nombre": "Capitana Marvel",
        "anio": 1968,
        "casa": "Marvel",
        "biografia": "Heroína con grandes poderes cósmicos."
    },
    {
        "nombre": "Dr. Strange",
        "anio": 1963,
        "casa": "DC",
        "biografia": "Hechicero experto en artes místicas."
    },
    {
        "nombre": "Flash",
        "anio": 1940,
        "casa": "DC",
        "biografia": "Superhéroe capaz de moverse a gran velocidad."
    },
    {
        "nombre": "Linterna Verde",
        "anio": 1940,
        "casa": "DC",
        "biografia": "Utiliza un anillo de poder."
    },
    {
        "nombre": "Mujer Maravilla",
        "anio": 1941,
        "casa": "DC",
        "biografia": "Guerrera amazona y miembro de la Liga de la Justicia."
    },
    {
        "nombre": "Spider-Man",
        "anio": 1962,
        "casa": "Marvel",
        "biografia": "Utiliza un traje y posee habilidades arácnidas."
    },
    {
        "nombre": "Star-Lord",
        "anio": 1976,
        "casa": "Marvel",
        "biografia": "Líder de los Guardianes de la Galaxia."
    },
    {
        "nombre": "Wolverine",
        "anio": 1974,
        "casa": "Marvel",
        "biografia": "Mutante con garras y gran capacidad de regeneración."
    },
    {
        "nombre": "Iron Man",
        "anio": 1963,
        "casa": "Marvel",
        "biografia": "Utiliza una armadura tecnológica."
    }
]


# Insertamos todos los superhéroes ordenados por nombre.
for heroe in datos:
    insertar(superheroes, heroe, "nombre")


# ----------------------------------------------------------
# A) Eliminar el nodo que contiene a Linterna Verde.
# ----------------------------------------------------------

eliminado = eliminar(superheroes, "Linterna Verde", "nombre")

if eliminado is not None:
    print("a) Linterna Verde fue eliminado de la lista.")
else:
    print("a) Linterna Verde no se encontró.")


# ----------------------------------------------------------
# B) Mostrar el año de aparición de Wolverine.
# ----------------------------------------------------------

wolverine = buscar(superheroes, "Wolverine", "nombre")

if wolverine is not None:
    print("\nb) Año de aparición de Wolverine:", wolverine.info["anio"])


# ----------------------------------------------------------
# C) Cambiar la casa de Dr. Strange a Marvel.
# ----------------------------------------------------------

doctor_strange = buscar(superheroes, "Dr. Strange", "nombre")

if doctor_strange is not None:
    doctor_strange.info["casa"] = "Marvel"
    print("\nc) La casa de Dr. Strange fue cambiada a Marvel.")


# ----------------------------------------------------------
# D) Mostrar los superhéroes cuya biografía mencione
#    la palabra "traje" o "armadura".
# ----------------------------------------------------------

print("\nd) Superhéroes que mencionan traje o armadura:")

actual = superheroes.inicio

while actual is not None:

    biografia = actual.info["biografia"].lower()

    if "traje" in biografia or "armadura" in biografia:
        print("-", actual.info["nombre"])

    actual = actual.siguiente


# ----------------------------------------------------------
# E) Mostrar nombre y casa de los superhéroes
#    que aparecieron antes de 1963.
# ----------------------------------------------------------

print("\ne) Superhéroes anteriores a 1963:")

actual = superheroes.inicio

while actual is not None:

    if actual.info["anio"] < 1963:
        print(actual.info["nombre"], "-", actual.info["casa"])

    actual = actual.siguiente


# ----------------------------------------------------------
# F) Mostrar la casa de Capitana Marvel y Mujer Maravilla.
# ----------------------------------------------------------

print("\nf) Casas:")

for nombre in ["Capitana Marvel", "Mujer Maravilla"]:

    heroe = buscar(superheroes, nombre, "nombre")

    if heroe is not None:
        print(nombre, "-", heroe.info["casa"])


# ----------------------------------------------------------
# G) Mostrar toda la información de Flash y Star-Lord.
# ----------------------------------------------------------

print("\ng) Información de Flash y Star-Lord:")

for nombre in ["Flash", "Star-Lord"]:

    heroe = buscar(superheroes, nombre, "nombre")

    if heroe is not None:
        print("\nNombre:", heroe.info["nombre"])
        print("Año:", heroe.info["anio"])
        print("Casa:", heroe.info["casa"])
        print("Biografía:", heroe.info["biografia"])


# ----------------------------------------------------------
# H) Listar los superhéroes que comienzan con B, M y S.
# ----------------------------------------------------------

print("\nh) Superhéroes que comienzan con B, M o S:")

actual = superheroes.inicio

while actual is not None:

    inicial = actual.info["nombre"][0].upper()

    if inicial in ["B", "M", "S"]:
        print("-", actual.info["nombre"])

    actual = actual.siguiente


# ----------------------------------------------------------
# I) Determinar cuántos superhéroes hay de Marvel y DC.
# ----------------------------------------------------------

marvel = 0
dc = 0

actual = superheroes.inicio

while actual is not None:

    if actual.info["casa"] == "Marvel":
        marvel += 1

    elif actual.info["casa"] == "DC":
        dc += 1

    actual = actual.siguiente


print("\ni) Cantidad de superhéroes por casa:")
print("Marvel:", marvel)
print("DC:", dc)