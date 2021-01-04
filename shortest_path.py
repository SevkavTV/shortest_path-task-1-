"""
Topic 1 (Find shortest path)

Team: Archakov Vsevolod, Kozak Tymofii, Kryvyi Mykola
      Onyshkiv Taras, Rodzin Taras
"""
import doctest
import random
import math


def generate_doctest(n, m):
    """
    Generates random doctest.
    """
    matrix = []
    for _ in range(n):
        lst = []
        for _ in range(m):
            height = random.randint(1, 100)
            lst.append(height)
        matrix.append(lst)

    return matrix


def convert_matrix_to_graph(matrix: list, step: int) -> dict:
    """
    Converts given matrix of heights to graph.
    """
    graph = {}
    move_lst = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for idx_row, row in enumerate(matrix):

        for idx_column, value in enumerate(row):

            for move in move_lst:
                new_idx_row = idx_row + move[0]
                new_idx_column = idx_column + move[1]

                if new_idx_row in range(0, len(matrix)) and \
                   new_idx_column in range(0, len(row)):

                    new_value = matrix[new_idx_row][new_idx_column]
                    dist = find_distance(value, new_value, step)

                    if (idx_row, idx_column) not in graph:
                        graph[(idx_row, idx_column)] = [
                            ((new_idx_row, new_idx_column), dist)]

                    else:
                        graph[(idx_row, idx_column)].append(
                            ((new_idx_row, new_idx_column), dist))

    return graph


def find_distance(height1: int, height2: int, step: int) -> float:
    """
    Calculates distance between two heights.
    """
    return math.sqrt((height1 - height2) ** 2 + step ** 2)


def find_shortest_distance(graph: dict, points: tuple) -> list:
    """
    Calculates shortest path and returns a list of indexes.
    """
    num_of_vertices = len(graph)

    distance = {key: 1e9 for key in graph.keys()}
    visited = {key: False for key in graph.keys()}
    ancestor = {}

    start_point = points[0]
    end_point = (points[1][0] - 1, points[1][1] - 1)

    distance[start_point] = 0
    ancestor[start_point] = -1

    for _ in range(num_of_vertices):
        mins = 1e10
        temp_point = -1

        for key, value in distance.items():

            if (not visited[key] and value < mins):
                mins = value
                temp_point = key

        visited[temp_point] = True

        for item in graph[temp_point]:
            point = item[0]
            dist_to_point = item[1]

            if (not visited[point] and distance[temp_point] + dist_to_point < distance[point]):
                distance[point] = distance[temp_point] + dist_to_point
                ancestor[point] = temp_point

    path_lst = [points[1]]

    while ancestor[end_point] != -1:
        path_lst.append((ancestor[end_point][0] + 1,
                         ancestor[end_point][1] + 1))
        end_point = ancestor[end_point]

    path_lst.reverse()

    return path_lst


if __name__ == '__main__':
    matrix = generate_doctest(10, 20)

    graph = convert_matrix_to_graph(matrix, 1)

    print(find_shortest_distance(graph, ((0, 0), (10, 20))))
