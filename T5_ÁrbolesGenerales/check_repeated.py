from typing import Optional, TypeVar, Iterator, List

from tads import IGeneralTree, LinkedGeneralTree, IPosition, ITree

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
tree.add_child_first(tree.add_child_last(p3, 8), 1)

print(tree)


def check_repeated_elems2(tree: ITree[T], pos: IPosition[T], elements: List[T]) -> bool:
    if pos.element in elements:
        return True

    elements.append(pos.element)

    it: Iterator[IPosition[T]] = tree.children(pos)
    child_pos: IPosition[T] = next(it, None)
    acabado: bool = False
    while not acabado and child_pos is not None:
        acabado = check_repeated_elems2(tree, child_pos, elements)
        child_pos = next(it, None)
    return acabado


def check_repeated_elems(tree: ITree[T]) -> bool:
    if tree.is_empty:
        return False

    return check_repeated_elems2(tree, tree.root, [])


print(check_repeated_elems(tree))  # true
