"""Задание 4: перевод графа из одного представления в другое."""

from pprint import pprint

VERTICES = [0, 1, 2, 3, 4]
EDGE_LIST = [(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (1, 4), (4, 3), (3, 2)]


def normalize_representation_name(name):
    aliases = {
        "adjacency_matrix": "матрица смежности",
        "incidence_matrix": "матрица инцидентности",
        "adjacency_list": "список смежности",
        "edge_list": "список дуг",
    }
    normalized = name.strip().lower()
    return aliases.get(normalized, normalized)


def graph_to_edges(graph, representation_name):
    """Перевести любое представление графа в список дуг."""
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

    if representation_name == "список дуг":
        return list(graph)

    raise ValueError(f"Неизвестное представление графа: {representation_name}")


def edges_to_adjacency_matrix(edges, vertices=VERTICES):
    size = max(vertices) + 1
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for start, finish in edges:
        matrix[start][finish] = 1
    return matrix


def edges_to_incidence_matrix(edges, vertices=VERTICES):
    matrix = [[0 for _ in edges] for _ in vertices]
    for edge_index, (start, finish) in enumerate(edges):
        matrix[start][edge_index] = -1
        matrix[finish][edge_index] = 1
    return matrix


def edges_to_adjacency_list(edges, vertices=VERTICES):
    adjacency_list = {vertex: [] for vertex in vertices}
    for start, finish in edges:
        adjacency_list[start].append(finish)
    return adjacency_list


def convert_graph(graph, source_representation, target_representation):
    """Перевести граф из одного представления в другое.

    target_representation может быть: матрица смежности, матрица инцидентности,
    список смежности, список дуг.
    """
    target_representation = normalize_representation_name(target_representation)
    edges = graph_to_edges(graph, source_representation)

    if target_representation == "матрица смежности":
        return edges_to_adjacency_matrix(edges)
    if target_representation == "матрица инцидентности":
        return edges_to_incidence_matrix(edges)
    if target_representation == "список смежности":
        return edges_to_adjacency_list(edges)
    if target_representation == "список дуг":
        return edges

    raise ValueError("Требуемое представление должно быть одним из заданий 1а-г")


def main():
    print("Задание 4. Примеры перевода из списка дуг")
    for target in ("матрица смежности", "матрица инцидентности", "список смежности"):
        print(f"\nсписок дуг -> {target}:")
        pprint(convert_graph(EDGE_LIST, "список дуг", target), width=120)


if __name__ == "__main__":
    main()
