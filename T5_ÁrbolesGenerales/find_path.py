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


def find_aux(gtree: ITree[T], elem: T, p: IPosition[T]) -> Optional[IPosition[T]]:
    """
    PRE: p is a valid position of gtree

    POST: returns the position of the node that contains elem
    in the subtree ref by p, if exits. Otherwise, returns None
    """
    if elem == p.element:
        return p
    else:
        # no hace falta el found de la transparencia
        it: Iterator[IPosition[T]] = gtree.children(p)
        child_pos: Optional[IPosition[T]] = next(it, None)
        pos: Optional[IPosition[T]] = None
        # As soon as elem is found in a subtree, it leaves the loop
        while pos is None and child_pos is not None:
            pos = find_aux(gtree, elem, child_pos)
            child_pos = next(it, None)
        return pos


def find(gtree: ITree[T], elem: T) -> Optional[IPosition[T]]:
    return find_aux(gtree, elem, gtree.root)


def find_path_aux(gtree: ITree[T], elem: T, p: IPosition[T]) -> \
        List[IPosition[T]]:
    if elem == p.element:
        return [p]
    else:
        it: Iterator[IPosition[T]] = gtree.children(p)
        child_pos: Optional[IPosition[T]] = next(it, None)
        # As soon as elem is found in a subtree, it leaves the loop
        path: List[IPosition[T]] = []
        while not path and child_pos is not None:
            path = find_path_aux(gtree, elem, child_pos)
            child_pos = next(it, None)

        if path:
            path.append(p)
        return path


def find_path(gtree: ITree[T], elem: T) -> List[IPosition[T]]:
    """
    PRE: gtree no es vacío
    """
    resultado: List[IPosition[T]] = find_path_aux(gtree, elem, gtree.root)
    resultado.reverse()
    return resultado


print([p.element for p in find_path(tree, 9)])  # [1, 3, 8, 9]
print(find_path(tree, 999))  # []

