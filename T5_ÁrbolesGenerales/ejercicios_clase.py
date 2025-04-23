from typing import TypeVar, Optional, Iterator, List

from tads import IGeneralTree, IPosition, LinkedGeneralTree, ITree, CircularQueue

T = TypeVar("T")

tree: IGeneralTree[int] = LinkedGeneralTree()
p1: IPosition[int] = tree.add_root(1)
p2: IPosition[int] = tree.add_child_first(p1, 2)
p3: IPosition[int] = tree.add_child_last(p1, 3)

tree.insert_sibling_before(p3, 10)
p4: IPosition[int] = tree.add_child_first(p2, 4)
p6: IPosition[int] = tree.insert_sibling_after(p4, 6)
tree.insert_sibling_before(p6, 5)
tree.add_child_first(p3, 7)
tree.add_child_first(tree.add_child_last(p3, 8), 9)

print(tree)


def contar_nodos_internos_aux(gtree: ITree[T], p: IPosition[T]) -> int:
    count: int = 1 if gtree.is_internal(p) else 0
    for child in gtree.children(p):
        count += contar_nodos_internos_aux(gtree, child)
    return count


def contar_nodos_internos(gtree: ITree[T]) -> int:
    return contar_nodos_internos_aux(gtree, gtree.root)


print(contar_nodos_internos(tree))

def depth(gtree: ITree[T], p: IPosition[T]) -> int:
    if gtree.parent(p):
        return 1 + depth(gtree, gtree.parent(p))
    else:
        return 0


print(depth(tree, p6))


def depth_it(gtree: ITree[T], p: IPosition[T]) -> int:
    cont: int = 0
    p_aux: Optional[IPosition[T]] = gtree.parent(p)
    while p_aux:
        cont += 1
        p_aux = gtree.parent(p_aux)
    return cont


print(depth_it(tree, p6))
