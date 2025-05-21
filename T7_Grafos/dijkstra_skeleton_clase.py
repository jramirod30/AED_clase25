def dijkstra(udg: IUndirectedGraph[V, E], org: Vertex[V]) -> (Dict[Vertex[V], int], Dict[Vertex[V], Vertex[V]]):
    distances: Dict[Vertex[V], int] = {}
    prev: Dict[Vertex[V], Vertex[V]] = {}
    unvisited: Set[Vertex[V]] = set()
    # initialize weights to inf except for the origin
    for vertex in udg.vertices():
        distances[vertex] = sys.maxsize
        unvisited.add(vertex)
    distances[org] = 0
    # TODO: Update the minimum distances and the previous vertex
    return distances, prev


def min_dist(distances: Dict[Vertex[V], int], unvisited: Set[Vertex[V]]) -> Vertex[V]:
    min_v: Optional[Vertex[V]] = None
    # TODO: return the vertex with the minimum distance
    return min_v
