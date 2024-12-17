import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    """
    Represents a graph using an adjacency list.

    Attributes:
        vertices (set): A set of vertices in the graph.
        adj_list (dict): An adjacency list representation of the graph.
    """

    def __init__(self, edges):
        """
        Initializes a graph from a list of edges.

        Args:
            edges (list): A list of tuples representing edges (u, v).
        """
        self.vertices = set()
        self.adj_list = {}

        for u, v in edges:
            self.vertices.add(u)
            self.vertices.add(v)
            self.adj_list.setdefault(u, []).append(v)
            self.adj_list.setdefault(v, []).append(u)  # For undirected graph

    def dfs(self, start):
        """
        Performs Depth-First Search (DFS) starting from the specified vertex using an iterative,
        stack-based approach.

        This implementation uses an explicit stack to manage traversal, avoiding the limitations
        of recursion such as stack overflow for deep or large graphs. The stack maintains a 
        Last-In-First-Out (LIFO) order of vertices, ensuring that each vertex is fully explored 
        before backtracking. 

        The algorithm follows these steps:
        1. Initialize an empty set `visited` to track visited vertices.
        2. Initialize a stack with the starting vertex to manage the traversal process.
        3. While the stack is not empty:
            - Pop a vertex from the stack.
            - If the vertex has not been visited:
                - Mark it as visited and add it to the traversal list.
                - Push all its unvisited neighbors onto the stack, ensuring that neighbors 
                are processed in the desired order.

        Args:
            start (int): The starting vertex.

        Returns:
            list: A list of vertices visited in DFS order.
        """
        stack = [start]
        visited = set()  
        traversal = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                traversal.append(node)

                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return traversal


edges = [(1, 2), (1, 3), (2, 4), (3,1), (1,3), (3,4),(1,4), (6,7), (6,8), (8,7), (8,10)]
g = Graph(edges)
result = g.dfs(1)
print(result)  # Output: [1, 4, 3, 2]


# # Create an undirected graph
G = nx.Graph()
G.add_edges_from(edges) 
                
# Visualize the graph
pos = nx.spring_layout(G)  # Positions the nodes in a spring layout
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
