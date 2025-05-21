import sys
from typing import TypeVar, List, Set, Iterator, Tuple

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


def get_neighbors(g: IUndirectedGraph[V, E], org: Vertex[V]) -> (
        List)[Vertex[V]]:
    lista: List[Vertex[V]] = []
    for i in g.edges_of(org):
        lista.append(g.opposite(org, i))
    return lista


def filtrar(vertices: List[Vertex[V]], visited: Set[Vertex[V]]) -> List[Vertex[V]]:
    result: List[Vertex[V]] = []
    for vertice in vertices:
        if vertice not in visited:
            result.append(vertice)
    return result


def get_accesibles_aux(g: IUndirectedGraph[V, E], v: Vertex[V],
                       visited: Set[Vertex[V]]) -> Set[Vertex[V]]:
    neighbors: List[Vertex[V]] = filtrar(get_neighbors(g, v), visited)
    it: Iterator[Vertex[V]] = iter(neighbors)
    neighbor: Vertex[V] = next(it, None)
    while neighbor is not None:
        visited.add(neighbor)
        visited = get_accesibles_aux(g, neighbor, visited)
        neighbor = next(it, None)
    return visited


def get_accesibles(g: IUndirectedGraph[V, E], v: Vertex[V]) -> Set[Vertex[V]]:
    return get_accesibles_aux(g, v, {v})


print([v.element for v in get_accesibles(g, v5)])


def get_cost(g: IUndirectedGraph[V, E], org: Vertex[V],
                  dest: Vertex[V]) -> int:
    it: Iterator[Edge[V, E]] = g.edges_of(org)
    edge: Edge[V, E] = next(it, None)
    while edge is not None and g.opposite(org, edge) != dest:
        edge = next(it, None)
    return edge.element


def find_path_aux(g: IUndirectedGraph[V, E], org: Vertex[V],
                  dest: Vertex[V],
                  visited: Set[Vertex[V]],
                  coste: int) -> Tuple[List[Vertex[V]], int]:
    if org == dest:
        return [org], coste
    neighbors: List[Vertex[V]] = filtrar(get_neighbors(g, org), visited)
    it: Iterator[Vertex[V]] = iter(neighbors)
    neighbor: Vertex[V] = next(it, None)
    path: List[Vertex[V]] = []
    coste: int
    while neighbor is not None and not path:
        visited.add(neighbor)
        path, coste = find_path_aux(g, neighbor, dest,
                                    visited, coste + get_cost(g, org, neighbor))
        neighbor = next(it, None)
    return ([org] + path, coste) if path else ([], sys.maxsize)


def find_path(g: IUndirectedGraph[V, E], org: Vertex[V],
              dest: Vertex[V]) -> Tuple[List[Vertex[V]], int]:
    return find_path_aux(g, org, dest, {org}, 0)


path, coste = find_path(g, v1, v4)
print([a.element for a in path], coste)