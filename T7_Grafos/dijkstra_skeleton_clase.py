import sys
from typing import Set, Dict, TypeVar, List, Iterator, Optional

from tads import Vertex, IUndirectedGraph, Edge, UndirectedAdjacencyListGraph

V = TypeVar('V')
E = TypeVar('E')

g: IUndirectedGraph[int, int] = UndirectedAdjacencyListGraph()
v6 = g.insert_vertex(6)
v1 = g.insert_vertex(1)
v2 = g.insert_vertex(2)
v3 = g.insert_vertex(3)
v4 = g.insert_vertex(4)
v5 = g.insert_vertex(5)

e1 = g.insert_edge(v1, v2, 7)
g.insert_edge(v1, v3, 9)
g.insert_edge(v1, v6, 14)
g.insert_edge(v2, v3, 10)
g.insert_edge(v2, v4, 15)
g.insert_edge(v3, v4, 11)
g.insert_edge(v3, v6, 2)
g.insert_edge(v4, v5, 6)
g.insert_edge(v5, v6, 9)

print(g)


def get_neighbors(udg: IUndirectedGraph[V, E], v: Vertex[V]) -> List[Vertex[V]]:
    result: List[Vertex[V]] = []
    for edge in udg.edges_of(v):
        result.append(edge.opposite(v))
    return result


def filter_visited(vertices: List[Vertex[V]], unvisited: Set[Vertex[V]]) -> List[Vertex[V]]:
    result: List[Vertex[V]] = []
    for v in vertices:
        if v in unvisited:
            result.append(v)
    return result


def get_cost(gf: IUndirectedGraph[V, E], org: Vertex[V],
             dest: Vertex[V]) -> int:
    it: Iterator[Edge[V, E]] = gf.edges_of(org)
    edge = next(it, None)
    while edge is not None and gf.opposite(org, edge) != dest:
        edge = next(it, None)
    return edge.element


def dijkstra(udg: IUndirectedGraph[V, E], org: Vertex[V]) -> \
        (Dict[Vertex[V], int], Dict[Vertex[V], Vertex[V]]):
    distances: Dict[Vertex[V], int] = {}
    prev: Dict[Vertex[V], Vertex[V]] = {}
    unvisited: Set[Vertex[V]] = set()
    # initialize weights to inf except for the origin
    for vertex in udg.vertices():
        distances[vertex] = sys.maxsize
        unvisited.add(vertex)
    distances[org] = 0
    a: Vertex[V]
    neighbors: List[Vertex[V]]
    dt: int
    while len(unvisited) > 0:
        #  step 3
        a = min_dist(distances, unvisited)
        #  step 4
        neighbors = filter_visited(get_neighbors(udg, a), unvisited)
        for n in neighbors:
            #   step 4.1
            dt = distances[a] + get_cost(udg, a, n)
            #  step 4.2
            if dt < distances[n]:
                distances[n] = dt
                prev[n] = a
        #  step 5
        unvisited.remove(a)

    return distances, prev


def min_dist(distances: Dict[Vertex[V], int], unvisited: Set[Vertex[V]]) -> Vertex[V]:
    min_v: Optional[Vertex[V]] = None
    min: int = sys.maxsize
    for v in unvisited:
        if distances[v] < min:
            min = distances[v]
            min_v = v
    return min_v


def build_path(org: Vertex[V], target: Vertex[V],
               visited_vertices: Dict[Vertex[V], Vertex[V]])\
                -> List[Vertex[V]]:
    if org == target:
        return [org]
    else:
        path: List[Vertex[V]] = build_path(org,
                                           visited_vertices[target], visited_vertices)
        path.append(target)
    return path


distances, prev = dijkstra(g, v1)

print([(v.element, distances[v]) for v in distances])
print([(v.element, prev[v].element) for v in prev])

print([v.element for v in build_path(v1, v5, prev)])