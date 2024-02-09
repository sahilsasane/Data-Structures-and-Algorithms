from collections import deque


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for src, dest in self.edges:
            if src in self.graph_dict:
                self.graph_dict[src].append(dest)
            else:
                self.graph_dict[src] = [dest]

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

    def bfs(self, start):
        visited = {node: False for node in self.graph_dict}
        queue = deque([start])
        visited[start] = True
        while queue:
            curr_node = queue.popleft()
            print(curr_node, end=" ")
            if curr_node in self.graph_dict:
                for neighbour in self.graph_dict[curr_node]:
                    if neighbour not in visited:
                        visited[neighbour] = False
                    if not visited[neighbour]:
                        queue.append(neighbour)
                        visited[neighbour] = True

    def dfs(self, start, visited=None):
        if visited is None:
            visited = {node: False for node in self.graph_dict}

        visited[start] = True
        print(start, end=" ")

        if start in self.graph_dict:
            for neighbor in self.graph_dict[start]:
                if neighbor not in visited:
                    visited[neighbor] = False
                if not visited[neighbor]:
                    self.dfs(neighbor, visited)


if __name__ == "__main__":
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
    # print(graph.get_shortest_path("A", "F"))
    graph.bfs("A")
    print("\n")
    graph.dfs("A")
