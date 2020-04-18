# Alekseeva Elena

"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""


def get_graph(n):
    graph = []

    for i in range(n):
        while True:
            tmp = input(f'Введите через запятую вершины к которым ведет {i}: ')
            try:
                tmp = [int(i) for i in tmp.split(', ')]
            except ValueError:
                print('Введите целые числа, разделенные запятой и пробелом'
                      ' (пример: 1, 2, 3)')
                continue
            graph.append(tmp)
            break

    return graph


def dfs(graph, start, visited=None):
    """Алгоритм поиска (или обхода) в глубину (англ. Depth-First Search, DFS)
    позволяет построить обход ориентированного или неориентированного графа,
    при котором посещаются все вершины, доступные из начальной вершины."""
    if visited is None:
        visited = set()
    visited.add(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

    return visited


if __name__ == '__main__':
    n = 0
    while True:
        try:
            n = int(input('Введите количество вершин графа: '))
        except ValueError:
            print('Введите целое число!!!')
            continue
        if n > 1:
            break
        else:
            print('Введите число больше 1')

    w = 0
    while True:
        try:
            w = int(input('Введите номер вершины из которой искать путь: '))
        except ValueError:
            print('Введите целое число!!!')
            continue
        if 0 <= w < n:
            break
        else:
            print('Введенной вешины не существует в графе!!!')

    graph = get_graph(n)
    print('Случайно сгенерированный граф:')
    print(graph)
    print(dfs(graph, 0))


# class Graph:
#
#     def __init__(self, graph_dict=None):
#         """ Инициализация графа
#             В случае, если graph_dict отсутствует
#             или None, то используется пустой словарь
#         """
#         if graph_dict is None:
#             graph_dict = {}
#         self.__graph_dict = graph_dict
#
#     def vertices(self):
#         """ Возвращаются вершины графа """
#         return list(self.__graph_dict.keys())
#
#     def edges(self):
#         """ Возвращаются ребра графа """
#         return self.__generate_edges()
#
#     def add_vertex(self, vertex):
#         """Если vertex "vertex" не является
#             self.__graph_dict,
#             key «вершина» с пустым списком
#             в качестве значения добавляется
#             в словарь. В противном случае
#             ничего не должно быть сделано.
#         """
#         if vertex not in self.__graph_dict:
#             self.__graph_dict[vertex] = []
#
#     def add_edge(self, edge):
#         """ предполагает, что ребро имеет тип set, tuple or list;
#             между двумя вершинами может быть несколько ребер!
#         """
#         edge = set(edge)
#         (vertex1, vertex2) = tuple(edge)
#         if vertex1 in self.__graph_dict:
#             self.__graph_dict[vertex1].append(vertex2)
#         else:
#             self.__graph_dict[vertex1] = [vertex2]
#
#     def __generate_edges(self):
#         """ Статический метод генерации ребер графа
#             "graph". Ребра представлены в виде sets
#             с одной (петля обратно к вершине) или
#             двумя вершинами
#         """
#         edges = []
#         for vertex in self.__graph_dict:
#             for neighbour in self.__graph_dict[vertex]:
#                 if {neighbour, vertex} not in edges:
#                     edges.append({vertex, neighbour})
#         return edges
#
#     def __str__(self):
#         res = "Вершины: "
#         for k in self.__graph_dict:
#             res += str(k) + " "
#         res += "\nРебра: "
#         for edge in self.__generate_edges():
#             res += str(edge) + " "
#         return res
#
#
# visited = set()  # Множество для хранения пути посещённых узлов
#
#
# def dfs(visited, graph, node):
#     """Алгоритм поиска (или обхода) в глубину (англ. Depth-First Search, DFS)
#     позволяет построить обход ориентированного или неориентированного графа,
#     при котором посещаются все вершины, доступные из начальной вершины.
#     Args:
#         visited: Множество для хранения пути посещённых узлов
#         graph: граф
#         node: узел
#     """
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)
#
#
# if __name__ == "__main__":
#     g = {
#         'A': ['B', 'C'],
#         'B': ['D', 'E'],
#         'C': ['F'],
#         'D': [],
#         'E': ['F'],
#         'F': []
#     }
#
#     graph = Graph(g)
#     print(graph)
#
#     # Вызов функции для алгоритма поиска в глубину
#     dfs(visited, g, 'B')

"""
Теория:

Графы, в которых все рёбра являются звеньями (порядок двух концов ребра графа не существенен), 
называются неориентированными.

Алгоритм поиска (или обхода) в глубину (англ. Depth-First Search, DFS) позволяет построить обход ориентированного 
или неориентированного графа, при котором посещаются все вершины, доступные из начальной вершины.

Отличие поиска в глубину от поиска в ширину заключается в том, что (в случае неориентированного графа) 
результатом алгоритма поиска в глубину является некоторый маршрут, следуя которому можно обойти 
последовательно все вершины графа, доступные из начальной вершины. Этим он принципиально отличается от поиска в 
ширину, где одновременно обрабатывается множество вершин, в поиске в глубину в каждый момент исполнения 
алгоритма обрабатывается только одна вершина. С другой стороны, поиск в глубину не находит кратчайших путей, 
зато он применим в ситуациях, когда граф неизвестен целиком, а исследуется каким-то автоматизированным устройством.
"""
