from typing import TypeVar

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
