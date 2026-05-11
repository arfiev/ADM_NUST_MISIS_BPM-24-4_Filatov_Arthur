"""Задание 2: программные представления графа из задания 1."""

from pprint import pprint

EDGES = [(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (1, 4), (4, 3), (3, 2)]

ADJACENCY_MATRIX = [
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
]

# Строки - вершины, столбцы - дуги.
# -1 - дуга выходит из вершины, 1 - дуга входит в вершину.
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

EDGE_LIST = EDGES.copy()
ORDERED_EDGE_LIST = sorted(EDGES)

REPRESENTATIONS = {
    "матрица смежности": ADJACENCY_MATRIX,
    "матрица инцидентности": INCIDENCE_MATRIX,
    "список смежности": ADJACENCY_LIST,
    "список дуг": EDGE_LIST,
    "упорядоченный список дуг": ORDERED_EDGE_LIST,
}


def main():
    print("Задание 2. Представления графа")
    for name, graph in REPRESENTATIONS.items():
        print(f"\n{name}:")
        pprint(graph, width=120)


if __name__ == "__main__":
    main()
