from typing import List


def multiplicar10(lista: List[int], i: int=0) -> List[int]:
    if i == len(lista):
        return []
    else:
        return [lista[i]*10] + multiplicar10(lista, i+1)


def multiplicar10_1(lista: List[int],
                    new_list: List[int] = [], i: int = 0)\
                    -> List[int]:
    if i == len(lista):
        return new_list
    else:
        new_list.append(lista[i]*10)
        return multiplicar10_1(lista, new_list, i + 1)


def suma(lista: List[int], i: int = 0) -> int:
    if i == len(lista):
        return 0
    else:
        return lista[i] + suma(lista, i + 1)

