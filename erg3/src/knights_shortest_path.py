from collections import deque

class KnightsShortestPath:
    """
    A class to calculate the shortest path for a knight on a chessboard using Breadth-First Search (BFS).

    The knight moves in an L-shape: two squares horizontally or vertically and one square 
    in the perpendicular direction. This algorithm efficiently finds the shortest path between 
    two squares on an 8x8 chessboard.

    Problem Representation:
    - The chessboard squares are represented as vertices in a graph.
    - An edge exists between two vertices if the knight can move directly between them.
    - The graph is undirected, with each vertex connected to up to 8 neighbors.

    Algorithmic Approach:
    - BFS is used to guarantee the shortest path in terms of the number of edges.
    - BFS explores neighbors level-by-level, ensuring that the first time the destination 
      is reached, the shortest path is found.

    Attributes:
        board_size (int): The size of the chessboard. Default is 8 for an 8x8 board.
        moves (list): A list of all possible knight moves as coordinate offsets.

    Methods:
        shortest_path(start, end):
            Calculates the shortest path between the start and end squares on the board.

    """

    def __init__(self, board_size=8):
        """
        Initializes the chessboard and knight's movement properties.

        Args:
            board_size (int): The size of the chessboard (default is 8 for an 8x8 board).
        """
        self.board_size = board_size
        self.moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

    def is_valid(self, x, y):
        """
        Checks if a given position (x, y) is valid on the chessboard.

        Args:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.

        Returns:
            bool: True if the position is within the chessboard bounds, False otherwise.
        """
        return 0 <= x < self.board_size and 0 <= y < self.board_size

    def shortest_path(self, start, end):
        """
        Finds the shortest path for a knight to move from start to end on a chessboard.

        Args:
            start (tuple): The starting position as (x, y).
            end (tuple): The destination position as (i, j).

        Returns:
            int: The minimum number of moves required for the knight to reach the destination. 
                 Returns -1 if the destination is unreachable (should not happen on an 8x8 board).
        """
        if start == end:
            return 0

        queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
        visited = set()
        visited.add(start)

        while queue:
            x, y, distance = queue.popleft()

            for dx, dy in self.moves:
                nx, ny = x + dx, y + dy

                if (nx, ny) == end:
                    return distance + 1

                if self.is_valid(nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, distance + 1))

        return -1  # If no path is found (not applicable for 8x8 chessboard).


knight_solver = KnightsShortestPath()

# Find the shortest path between (0, 0) and (7, 7)
print(knight_solver.shortest_path((0, 0), (7, 7)))  # output: 6
