from typing import Optional, TypeVar, List

from tads import IBinaryTree, LinkedBinaryTree, IPosition

T = TypeVar("T")

tree: IBinaryTree[int] = LinkedBinaryTree()

root: IPosition[int] = tree.add_root(1)

n2: IPosition[int] = tree.add_left(root, 2)
tree.add_left(n2, 4)
tree.add_right(n2, 5)

n3: IPosition[int] = tree.add_right(root, 3)
tree.add_left(n3, 6)
n7: IPosition[int] = tree.add_right(n3, 7)
tree.add_left(n7, 8)

print(tree)


def contar_hojas_aux(btree: IBinaryTree[T],
                     p: Optional[IPosition[T]]) -> int:
    if not p:
        return 0
    elif btree.is_leaf(p):
        return 1
    else:
        return (contar_hojas_aux(btree, btree.left(p)) +
                contar_hojas_aux(btree, btree.right(p)))


def contar_hojas(btree: IBinaryTree[T]) -> int:
    """
    PRE: btree no es vacío
    """
    return contar_hojas_aux(btree, btree.root)


print(contar_hojas(tree))


def contar_ocurrencias_aux(btree: IBinaryTree[T],
                           p: Optional[IPosition[T]], elem: T) -> int:
    if not p:
        return 0
    elif p.element == elem:
        return (1 + contar_ocurrencias_aux(btree, btree.left(p), elem) +
                contar_ocurrencias_aux(btree, btree.right(p), elem))
    else:
        return (contar_ocurrencias_aux(btree, btree.left(p), elem) +
                contar_ocurrencias_aux(btree, btree.right(p), elem))


def contar_ocurrencias_aux1(btree: IBinaryTree[T], elem: T,
                            p: Optional[IPosition[T]]) -> int:
    if not p:
        return 0
    else:
        return ((1 if p.element == elem else 0) +
                contar_ocurrencias_aux1(btree, elem, btree.left(p)) +
                contar_ocurrencias_aux1(btree, elem, btree.right(p)))


def contar_ocurrencias(btree: IBinaryTree[T], elem: T) -> int:
    return contar_ocurrencias_aux(btree, elem, btree.root)


def find_aux(btree: IBinaryTree[T], elem: T, p: Optional[IPosition[T]]) -> \
        Optional[IPosition[T]]:
    if p:
        if p.element == elem:
            return p
        else:
            result: Optional[IPosition[T]] = find_aux(btree, elem, btree.left(p))
            if result is None:
                result = find_aux(btree, elem, btree.right(p))
            return result
    else:
        return None


def find(btree: IBinaryTree[T], elem: T) -> Optional[IPosition[T]]:
    """
    PRE: no hay elems repetidos
    """
    return find_aux(btree, elem, btree.root)


print(find(tree, 8).element)
print(find(tree, 88888))  # no está


def get_elems_pares(btree: IBinaryTree[int],
                    p: Optional[IPosition[int]]) -> List[int]:
    lista: List = []
    if not p:
        return []
    else:
        if p.element % 2 == 0:
            lista.append(p.element)
        return (lista + get_elems_pares(btree, btree.left(p))
                + get_elems_pares(btree, btree.right(p)))


print(get_elems_pares(tree, tree.root))
