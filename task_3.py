"""Задание 3: просмотр дуг, исходящих из заданной вершины."""

ADJACENCY_MATRIX = [
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
]

INCIDENCE_MATRIX = [
    [-1, -1, -1, 0, 0, 0, 0, 0],
    [1, 0, 0, -1, -1, -1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, -1],
    [0, 0, 1, 0, 0, 1, -1, 0],
]

ADJACENCY_LIST = {
    0: [1, 2, 4],
    1: [2, 3, 4],
    2: [],
    3: [2],
    4: [3],
}

EDGE_LIST = [(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (1, 4), (4, 3), (3, 2)]
ORDERED_EDGE_LIST = sorted(EDGE_LIST)

REPRESENTATIONS = {
    "матрица смежности": ADJACENCY_MATRIX,
    "матрица инцидентности": INCIDENCE_MATRIX,
    "список смежности": ADJACENCY_LIST,
    "список дуг": EDGE_LIST,
    "упорядоченный список дуг": ORDERED_EDGE_LIST,
}


def normalize_representation_name(name):
    aliases = {
        "adjacency_matrix": "матрица смежности",
        "incidence_matrix": "матрица инцидентности",
        "adjacency_list": "список смежности",
        "edge_list": "список дуг",
        "ordered_edge_list": "упорядоченный список дуг",
    }
    normalized = name.strip().lower()
    return aliases.get(normalized, normalized)


def graph_to_edges(graph, representation_name):
    """Перевести представление графа в список дуг."""
    representation_name = normalize_representation_name(representation_name)

    if representation_name == "матрица смежности":
        return [
            (start, finish)
            for start, row in enumerate(graph)
            for finish, value in enumerate(row)
            if value
        ]

    if representation_name == "матрица инцидентности":
        edges = []
        for edge_index in range(len(graph[0])):
            start = finish = None
            for vertex, row in enumerate(graph):
                if row[edge_index] == -1:
                    start = vertex
                elif row[edge_index] == 1:
                    finish = vertex
            edges.append((start, finish))
        return edges

    if representation_name == "список смежности":
        return [(start, finish) for start, neighbors in graph.items() for finish in neighbors]

    if representation_name in {"список дуг", "упорядоченный список дуг"}:
        return list(graph)

    raise ValueError(f"Неизвестное представление графа: {representation_name}")


def outgoing_edges(graph, representation_name, vertex):
    """Вернуть дуги, исходящие из указанной вершины, в формате (i, j)."""
    edges = graph_to_edges(graph, representation_name)
    return [(start, finish) for start, finish in edges if start == vertex]


def main():
    vertex = 1
    print(f"Задание 3. Дуги, исходящие из вершины {vertex}")
    for name, graph in REPRESENTATIONS.items():
        print(f"{name}: {outgoing_edges(graph, name, vertex)}")


if __name__ == "__main__":
    main()
