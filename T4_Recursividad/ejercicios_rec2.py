from typing import List, TypeVar

T = TypeVar("T")


def es_palindroma(palabra: str, i: int) -> bool:
    if i >= 0:
        return palabra[i] == palabra[len(palabra) - i - 1] and es_palindroma(palabra, i - 1)
    else:
        return True


palabra1 = "aaacdaaa"
print(es_palindroma(palabra1, int(len(palabra1) / 2 - 1)))


def rotar_izquierda(lista: List[T], n: int, result: List[T] = [], i: int = 0) -> List[T]:
    if n == i:
        return lista[n:] + result
    else:
        result.append(lista[i])
        return rotar_izquierda(lista, n, result, i + 1)


print(rotar_izquierda([3, 4, 5, 7, 9], 2))

