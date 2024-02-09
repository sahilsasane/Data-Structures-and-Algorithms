    stack = [start_node]

        while stack:
            current_node = stack.pop()
            if not visited[current_node]:
                print(current_node, end=" ")
                visited[current_node] = True

                if current_node in self.graph_dict:
                    for neighbor in reversed(self.graph_dict[current_node]):
                        if neighbor not in visited:
                            stack.append(neighbor)