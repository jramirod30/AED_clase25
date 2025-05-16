from typing import TypeVar, List, Set, Iterator

from tads import IUndirectedGraph, UndirectedAdjacencyListGraph, Vertex, Edge

V = TypeVar("V")
E = TypeVar("E")

g: IUndirectedGraph[int, int] = UndirectedAdjacencyListGraph()

v1: Vertex[int] = g.insert_vertex(1)
v2 = g.insert_vertex(2)
v3 = g.insert_vertex(3)
v4 = g.insert_vertex(4)
g.insert_edge(v1, v2, 0)
g.insert_edge(v2, v3, 1)
g.insert_edge(v3, v4, 2)
g.insert_edge(v1, v3, 3)
g.insert_edge(v2, v4, 4)

print(g)


def get_neighbors(g: IUndirectedGraph[V, E], org: Vertex[V]) -> (
        List)[Vertex[V]]:
    lista:List[Vertex[V]]=[]
    for i in g.edges_of(org):
        lista.append(g.opposite(org, i))
    return lista


def filtrar(vertices: List[Vertex[V]], visited: Set[Vertex[V]]) -> List[Vertex[V]]:
    result: List[Vertex[V]] = []
    for vertice in vertices:
        if vertice not in visited:
            result.append(vertice)
    return result


def find_path_aux(g: IUndirectedGraph[V, E], org: Vertex[V],
              dest: Vertex[V], visited: Set[Vertex[V]])-> List[Vertex[V]]:
    if org == dest:
        return [org]
    neighbors: List[Vertex[V]] = filtrar(get_neighbors(g, org), visited)
    it: Iterator[Vertex[V]] = iter(neighbors)
    neighbor: Vertex[V] = next(it, None)
    path: List[Vertex[V]] = []
    while neighbor is not None and not path:
        visited.add(neighbor)
        path = find_path_aux(g, neighbor, dest, visited)
        neighbor = next(it, None)
    return [org] + path if path else []


def find_path(g: IUndirectedGraph[V, E], org: Vertex[V],
              dest: Vertex[V]) -> List[Vertex[V]]:
    return find_path_aux(g, org, dest, {org})



print([a.element for a in find_path(g, v1, v4)])