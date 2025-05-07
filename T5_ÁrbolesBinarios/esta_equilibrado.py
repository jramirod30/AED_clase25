from typing import TypeVar, Optional

from tads.position.iposition import IPosition
from tads.tree.linked_binary_tree import IBinaryTree
from tads.tree.linked_binary_tree import LinkedBinaryTree

T = TypeVar('T')
# árbol de prueba
tree: IBinaryTree[int] = LinkedBinaryTree()
tree.add_root(10)
nl: IPosition = tree.add_left(tree.root, 2)
nl1 = tree.add_left(nl, 1)
tree.add_right(nl, 5)

nr: IPosition = tree.add_right(tree.root, 30)
tree.add_left(nr, 20)
nr1 = tree.add_right(nr, 70)
nr2 = tree.add_right(nr1, 80)

print("tam " + str(tree.size()))

print(tree)


def height(btree: IBinaryTree[T], p: Optional[IPosition[T]]) -> int:
    """
    PRE: btree is not empty

    POST: return the height of btree
    """
    if p is None or btree.is_leaf(p):
        return 0
    else:
        return (1 +
                max(height(btree, btree.left(p)),
                    height(btree, btree.right(p))))


def esta_equilibrado(btree: IBinaryTree[T]) -> bool:
    return btree.is_empty or esta_equilibrado_aux(btree, btree.root)


def esta_equilibrado_aux(btree: IBinaryTree[T],
                         p: Optional[IPosition[T]]) -> bool:
    if p is None:
        return True
    return abs(height(btree, btree.left(p)) - height(btree, btree.right(p))) <= 1 \
        and \
        esta_equilibrado_aux(btree, btree.left(p)) and \
        esta_equilibrado_aux(btree, btree.right(p))


print(esta_equilibrado(tree))