import sys
from typing import TypeVar, Set, List, Iterator, Tuple

from tads import IUndirectedGraph, UndirectedAdjacencyListGraph, Vertex, Edge

V = TypeVar("V")
E = TypeVar("E")

g: IUndirectedGraph[int, int] = UndirectedAdjacencyListGraph()

v1: Vertex[int] = g.insert_vertex(1)
v2 = g.insert_vertex(2)
v3 = g.insert_vertex(3)
v4 = g.insert_vertex(4)
v5 = g.insert_vertex(5)
g.insert_edge(v1, v2, 3)
g.insert_edge(v2, v3, 1)
g.insert_edge(v3, v4, 2)
g.insert_edge(v1, v3, 3)
g.insert_edge(v2, v4, 4)
print(g)


def get_neighbors(udg: IUndirectedGraph[V, E], v: Vertex[V]) -> List[Vertex[V]]:
    result: List[Vertex[V]] = []
    for edge in udg.edges_of(v):
        result.append(edge.opposite(v))
    return result


print([a.element for a in get_neighbors(g, v1)])


def filter_visited(vertices: List[Vertex[V]], visited: Set[Vertex[V]]) -> List[Vertex[V]]:
    result: List[Vertex[V]] = []
    for v in vertices:
        if v not in visited:
            result.append(v)
    return result


def get_cost(gf: IUndirectedGraph[V, E], org: Vertex[V],
             dest: Vertex[V]) -> int:
    it: Iterator[Edge[V, E]] = gf.edges_of(org)
    edge = next(it, None)
    while edge is not None and gf.opposite(org, edge) != dest:
        edge = next(it, None)
    return edge.element


def find_aux(gf: IUndirectedGraph[V, E], org: Vertex[V],
             dest: Vertex[V], visited: Set[Vertex[V]], cost: int) -> Tuple[List[Vertex[V]], int]:
    if org == dest:
        return [org], cost

    neighbors: List[Vertex[V]] = filter_visited(get_neighbors(gf, org), visited)
    it: Iterator[Vertex[V]] = iter(neighbors)
    neighbor: Vertex[V] = next(it, None)
    path: List[Vertex[V]] = []
    cost1: int = 0
    min_cost: int = sys.maxsize
    min_path: List[Vertex[V]] = []
    while neighbor is not None:
        path, cost1 = find_aux(gf, neighbor, dest, visited | {neighbor},
                               cost + get_cost(gf, org, neighbor))
        if cost1 < min_cost:
            min_cost = cost1
            min_path = path
        neighbor = next(it, None)
    return ([org] + min_path, min_cost) if min_path else ([], sys.maxsize)


path, cost = find_aux(g, v1, v4, {v1}, 0)
print([node.element for node in path], cost)