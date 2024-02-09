from collections import deque


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        # print(self.graph_dict)

    def bfs(self, start_node):
        visited = {node: False for node in self.graph_dict}
        queue = deque([start_node])
        visited[start_node] = True

        while queue:
            current_node = queue.popleft()
            print(current_node, end=" ")

            if current_node in self.graph_dict:
                for neighbor in self.graph_dict[current_node]:
                    if neighbor not in visited:
                        visited[neighbor] = False
                    if not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True

    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = {node: False for node in self.graph_dict}

        visited[start_node] = True
        print(start_node, end=" ")

        if start_node in self.graph_dict:
            for neighbor in self.graph_dict[start_node]:
                if neighbor not in visited:
                    visited[neighbor] = False
                if not visited[neighbor]:
                    self.dfs(neighbor, visited)

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("B", "E"),
        ("C", "F"),
        ("E", "F"),
        ("E", "G"),
        ("F", "G"),
    ]

    graph = Graph(edges)
    print(graph.get_paths("A", "F"))
    print(graph.get_shortest_path("A", "F"))
    graph.bfs("A")
    graph.dfs("A")
