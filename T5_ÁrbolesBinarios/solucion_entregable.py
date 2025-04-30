from typing import Optional, TypeVar, List, Iterator

from tads import IBinaryTree, LinkedBinaryTree, IPosition, ITree

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

tree1: IBinaryTree[int] = LinkedBinaryTree()

root: IPosition[int] = tree1.add_root(1)

n2: IPosition[int] = tree1.add_left(root, 2)
tree1.add_left(n2, 4)
tree1.add_right(n2, 5)

n3: IPosition[int] = tree1.add_right(root, 3)
tree1.add_left(n3, 6)
n7: IPosition[int] = tree1.add_right(n3, 7)


def equals(btree1: IBinaryTree[T], btree2: IBinaryTree[T]) -> bool:
    if btree1.is_empty and btree2.is_empty:
        return True
    return (btree1.size() == btree2.size() and
            equals_aux(btree1, btree2, btree1.root, btree2.root))


def equals_aux(btree1: IBinaryTree[T], btree2: IBinaryTree[T],
               pos1: Optional[IPosition[T]], pos2: Optional[IPosition[T]]) -> bool:
    if pos1 and pos2:
        return (pos1.element == pos2.element and
                equals_aux(btree1, btree2, btree1.left(pos1),
                           btree2.left(pos2))
                and equals_aux(btree1, btree2, btree1.right(pos1),
                               btree2.right(pos2)))
    else:
        return pos1 is None and pos2 is None


print(equals(tree, tree))  # True
print(equals(tree, tree1))  # False


def find_path_aux(btree: IBinaryTree[T], pos: Optional[IPosition[T]],
                  elem: T, path: List[IPosition[T]]) -> (
        List)[IPosition[T]]:
    if pos:
        path.append(pos)
        if pos.element == elem:
            return path
        else:
            path_aux: List[IPosition[T]] = find_path_aux(btree,
                                                         btree.left(pos),
                                                         elem, path)
            if path_aux:
                return path_aux
            else:
                path_aux = find_path_aux(btree, btree.right(pos),
                                         elem, path)
                if path_aux:
                    return path_aux
                path.pop()
                return []
    else:
        return []


def find_path(btree: IBinaryTree[T], elem: T) -> List[IPosition[T]]:
    if btree.is_empty:
        return []
    path: List[IPosition[T]] = []
    return find_path_aux(btree, btree.root, elem, path)


print([a.element for a in find_path(tree, 8)])  # [1, 3, 7, 8]
print(find_path(tree, 88))  # []


def find_path_aux1(btree: IBinaryTree[T], pos: Optional[IPosition[T]],
                   elem: T) -> (
        List)[IPosition[T]]:
    if pos:
        if pos.element == elem:
            return [pos]
        else:
            path_aux: List[IPosition[T]] = find_path_aux1(btree,
                                                          btree.left(pos),
                                                          elem)
            if not path_aux:
                path_aux = find_path_aux1(btree, btree.right(pos),
                                          elem)
            if path_aux:
                path_aux.append(pos)
                return path_aux
            else:
                return []
    else:
        return []


def find_path1(btree: IBinaryTree[T], elem: T) -> List[IPosition[T]]:
    if btree.is_empty:
        return []
    path: List[IPosition[T]] = find_path_aux1(btree, btree.root, elem)
    path.reverse()
    return path


print([a.element for a in find_path(tree, 8)])  # [1, 3, 7, 8]
print(find_path(tree, 88))  # []


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


def replace(btree: IBinaryTree[T], old: T, new: T) -> None:
    if not btree.is_empty:
        pos: IPosition[T] = find(btree, old)
        if pos is not None:
            btree.set(pos, new)


replace(tree, 8, 888)  # 8 -> 888
replace(tree, 99, 999)  # no hace nada
print(tree)
