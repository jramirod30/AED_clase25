from typing import List, Set, TypeVar, Tuple

T = TypeVar("T")
V = TypeVar("V")


# Función para convertir una lista en un conjunto (elimina duplicados)
def elems(l1: List[T]) -> Set[T]:
    # Inicializa un conjunto vacío 'result'
    # Para cada elemento 'a' en la lista 'l1':
    #   - Añadir el elemento 'a' al conjunto 'result'
    # Retorna el conjunto 'result'

    conjunto: Set[T] = set()
    for elemento in l1:
        conjunto.add(elemento)
    return conjunto


# Ejemplo para probar la función elems
print(elems([1, 1, 1, 3, 4]))  # Salida esperada: {1, 3, 4}


# Función para encontrar los elementos comunes entre dos listas
def elems_comunes(l1, l2: List[T]) -> Set[T]:
    # Convertir las listas 'l1' y 'l2' en conjuntos utilizando la función 'elems'
    # Retornar la intersección de los dos conjuntos

    conjunto1: Set[T] = elems(l1)
    conjunto2: Set[T] = elems(l2)
    return conjunto1 & conjunto2


# Ejemplo para probar la función elems_comunes
print(elems_comunes([1, 1, 2, 3], [2, 3, 4]))  # Salida esperada: {2, 3}


# Función para verificar si todos los elementos de una lista están en otra lista (verificación de subconjunto)
def esta_incluida(l1, l2: List[T]) -> bool:
    # Convertir las listas 'l1' y 'l2' a conjuntos utilizando la función 'elems'
    # Retornar True si el conjunto de 'l1' es un subconjunto de 'l2', de lo contrario False

    return elems(l1) <= elems(l2)


# Función para extraer los elementos de 'l1' que no están en 'l2'
def extraer_elems(l1, l2: List[T]) -> Set[T]:
    # Convertir 'l1' y 'l2' en conjuntos utilizando la función 'elems'
    # Retornar la diferencia entre los dos conjuntos (elementos de 'l1' que no están en 'l2')

    return elems(l1) - elems(l2)


# Función para extraer los elementos de 'l1' que no están en 'l2', devolviéndolos como una lista
def extraer_elems1(l1, l2: List[T]) -> List[T]:
    # Convertir 'l2' en un conjunto 's2' utilizando la función 'elems'
    # Inicializar una lista vacía 'result'
    # Para cada elemento 'a' en 'l1':
    #   - Si 'a' no está en 's2', añadirlo a la lista 'result'
    # Retornar la lista 'result'

    s2 = elems(l2)
    result = []
    for a in l1:
        if a not in s2:
            result.append(a)
    return result


# Función para calcular el producto cartesiano de dos conjuntos
def producto_cartesiano(s1: Set[T], s2: Set[V]) -> Set[Tuple[T, V]]:
    # Inicializar un conjunto vacío 'producto' para almacenar el producto cartesiano
    # Para cada elemento 'a' en el conjunto 's1':
    #   - Para cada elemento 'b' en el conjunto 's2':
    #     - Añadir la tupla (a, b) al conjunto 'producto'
    # Retornar el conjunto 'producto'

    res: Set[Tuple[T, V]] = set()
    for a in s1:
        for b in s2:
            res.add((a, b))
    return res


print(producto_cartesiano({1, 2}, {4, 5}))