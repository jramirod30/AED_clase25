import sys
from typing import List, TypeVar, Any, Tuple

T = TypeVar("T")


def multiplicar10(lista: List[int], i: int = 0) -> List[int]:
    if i == len(lista):
        return []
    else:
        return [lista[i] * 10] + multiplicar10(lista, i + 1)


def multiplicar10_1(lista: List[int],
                    new_list: List[int] = [], i: int = 0) \
        -> List[int]:
    if i == len(lista):
        return new_list
    else:
        new_list.append(lista[i] * 10)
        return multiplicar10_1(lista, new_list, i + 1)


def suma(lista: List[int], i: int = 0) -> int:
    if i == len(lista):
        return 0
    else:
        return lista[i] + suma(lista, i + 1)


def posiciones(lista: List[T], dato: T, i: int = 0,
               lista_posiciones: List[int] = []) -> List[int]:
    if i >= len(lista):
        return lista_posiciones
    if lista[i] == dato:
        lista_posiciones.append(i)
    return posiciones(lista, dato, i + 1, lista_posiciones)


def posiciones_1(lista: List[T], dato: T, i: int) -> List[int]:
    if i >= 0:
        aux: List[int] = posiciones_1(lista, dato, i - 1)
        if lista[i] == dato:
            aux.append(i)
        return aux
    else:
        return []


print(posiciones_1([3, 3, 12, 25, 67, 3], 3, 5))


def filtro(lista: List[int], elemento: int,
           new_list: List[int] = [], i: int = 0) -> List[int]:
    if i < len(lista):
        if lista[i] % elemento == 0:
            new_list.append(lista[i])
        return filtro(lista, elemento, new_list, i + 1)
    return new_list


def xor(bin1: List[int], bin2: List[int], bin3: List[int], i: int) \
        -> List[int]:
    if i < len(bin1):
        # bin3.append((bin1[i] + bin2[i]) % 2)
        if bin1[i] != bin2[i]:
            bin3.append(1)
        else:
            bin3.append(0)
        return xor(bin1, bin2, bin3, i + 1)
    return bin3


def maximo(lista: List[int], resultado: int = -sys.maxsize, i: int = 0) -> int:
    if i == len(lista):
        return resultado
    if lista[i] > resultado:
        return maximo(lista, lista[i], i + 1)
    return maximo(lista, resultado, i + 1)


def maximo_aux(lista: List[int], resultado: int, i: int = 0) -> int:
    if i == len(lista):
        return resultado
    if lista[i] > resultado:
        return maximo(lista, lista[i], i + 1)
    return maximo(lista, resultado, i + 1)


def max_1(lista: List[int]) -> int:
    """
    PRE: lista no es vacía
    """
    return maximo_aux(lista, lista[0], 1)


def intercalar_listas(l1: List[T], l2: List[T], i: int = 0, lista_final: List[T] = []) -> List[T]:
    if i >= len(l1) and i >= len(l2):
        return lista_final
    if i < len(l1):
        lista_final.append(l1[i])
    if i < len(l2):
        lista_final.append(l2[i])
    return intercalar_listas(l1, l2, i + 1, lista_final)


def intercalar_listas_1_aux(l1: List[T], l2: List[T], minimo: int, i: int = 0, lista_final: List[T] = []) -> List[T]:
    if i < minimo:
        lista_final.append(l1[i])
        lista_final.append(l2[i])
        return intercalar_listas_1_aux(l1, l2, minimo, i + 1, lista_final)
    else:
        if i < len(l1):
            lista_final.extend(l1[i:])
        else:
            lista_final.extend(l2[i:])
        return lista_final


def intercalar_listas_1(l1: List[T], l2: List[T]) -> List[T]:
    return intercalar_listas_1_aux(l1, l2, min(len(l1), len(l2)))


print(intercalar_listas_1([3, 4, 5], [1, 3, 7, 9, 11, 13, 15]))


def aplanar(lista: List[Any]) -> List[Any]:
    if lista:
        if isinstance(lista[0], List):
            return aplanar(lista[0]) + aplanar(lista[1:])
        else:
            return [lista[0]] + aplanar(lista[1:])
    else:
        return []


def dividir(lista: List[T], pivote: T) -> \
        Tuple[List[T], List[T]]:
    menores: List[T] = []
    mayores: List[T] = []
    for a in lista:
        if a < pivote:
            menores.append(a)
        else:
            mayores.append(a)
    return menores, mayores


def quicksort(lista: List[T]) -> List[T]:
    if len(lista) <= 1:
        return lista
    pivote: T = lista[0]
    tupla: Tuple[List[T], List[T]] = dividir(lista[1:], pivote)
    return (quicksort(tupla[0]) + [pivote] +
            quicksort(tupla[1]))


def inverso(lista: List[T], i: int = 0) -> List[T]:
    if i == len(lista):
        return []
    nueva_lista: List[T] = inverso(lista, i + 1)
    nueva_lista.append(lista[i])
    return nueva_lista


def ordenada(lista: List[T], i: int = 0) -> bool:
    if len(lista) - 1 == i:
        return True
    else:
        return (lista[i] <= lista[i + 1] and
                ordenada(lista, i + 1))


# modifica el parámetro lista
def insertar_ordenado(lista:List[int], n:int, i:int = 0):
    if i == len(lista):
        lista.append(n)
        return lista
    else:
        if lista[i] < n:
            return insertar_ordenado(lista, n, i+1)
        else:
            lista.insert(i, n)
            return lista


def insertar_ord(lista: List[int], a: int, result: List[T] = [], i: int = 0) -> List[int]:
    """
    PRE: lista está ordenada de menor a mayor
    """
    if i == len(lista) or a <= lista[i]:
        result.append(a)
        return result + lista[i:]
    else:
        result.append(lista[i])
        return insertar_ord(lista, a, result, i + 1)


def suma_aux(n1: List[int], n2: List[int], i: int, acarreo: int = 0) -> List[int]:
    if i >= 0:
        total: int = n1[i] + n2[i] + acarreo
        sig_acarreo: int = (1 if total > 9 else 0)
        result: List[int] = suma_aux(n1, n2, i - 1, sig_acarreo)
        result.append(total - sig_acarreo * 10)
        return result
    else:
        return [] if acarreo == 0 else [acarreo]


def suma(n1: List[int], n2: List[int]) -> List[int]:
    return suma_aux([0] * (len(n2) - len(n1)) + n1,
                    [0] * (len(n1) - len(n2)) + n2,
                    max(len(n1), len(n2)) - 1)


print(suma([3, 4], [1, 0, 0, 0]))