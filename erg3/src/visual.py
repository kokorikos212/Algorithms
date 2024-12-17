import networkx as nx
import matplotlib.pyplot as plt
import os
import shutil


class DFSVisualizer:
    def __init__(self, graph):
        """
        Initializes the visualizer with a graph and prepares for DFS traversal.

        Args:
            graph (networkx.Graph): The graph to visualize the DFS traversal on.
        """
        self.graph = graph
        self.color_map = {node: "white" for node in graph.nodes}  # Start with all nodes as unvisited (white)
        self.time = 0  # Initialize DFS timer
        self.frames_dir = "frames"  # Directory to save frames for visualization
        self.positions = nx.spring_layout(graph)  # Layout for consistent visualization
        if os.path.exists(self.frames_dir):
            shutil.rmtree(self.frames_dir)  # Clean up previous frames
        os.makedirs(self.frames_dir)  # Create new directory for frames
    
    def dfs(self, start):
        """
        Performs Depth-First Search (DFS) traversal starting from a given node.

        This method implements an iterative DFS using a stack, capturing frames at each step for visualization,
        and tracking the ancestor forest (parent-child relationships) during the traversal.  Nodes are colored
        according to their state during the traversal:

        - White: Unvisited
        - Gray: Currently being visited
        - Black: Fully visited (all descendants explored)

        The algorithm uses discovery and finish times to track the progress of the DFS.  These times
        represent the order in which nodes are first encountered and completely explored, respectively.

        Args:
            start: The starting node for the DFS traversal.

        Returns:
            tuple: A tuple containing three dictionaries:
                - discovery_time: Maps each node to its discovery time.
                - finish_time: Maps each node to its finish time.
                - parent: Maps each node to its parent node in the DFS tree (None for the root).
        """
        stack = [start]
        visited = set()
        parent = {node: None for node in self.graph.nodes}
        discovery_time = {}
        finish_time = {}

        while stack:
            node = stack[-1]

            if node not in visited:
                visited.add(node)
                self.time += 1
                discovery_time[node] = self.time
                self.color_map[node] = "gray"
                self._save_frame()

                for neighbor in sorted(self.graph.neighbors(node), reverse=True):
                    if neighbor not in visited and neighbor not in stack:
                        parent[neighbor] = node
                        stack.append(neighbor)

            else:
                self.time += 1
                finish_time[node] = self.time
                self.color_map[node] = "black"
                stack.pop()
                self._save_frame()

        return discovery_time, finish_time, parent


    def _save_frame(self):
        """
        Saves the current state of the graph as a frame, reflecting the DFS traversal state.

        This method creates a snapshot of the graph at the current DFS state, with nodes colored 
        according to their state (white for unvisited, gray for visiting, black for fully visited).
        The frame is saved in the frames directory for later visualization.
        """
        plt.figure(figsize=(8, 6))
        nx.draw(
            self.graph,  # The graph to draw
            pos=self.positions,  # The layout of the graph
            node_color=[self.color_map[node] for node in self.graph.nodes],  # Color based on node state
            with_labels=True,  # Display node labels
            node_size=500,  # Size of the nodes
            font_color="white",  # Color of the node labels
            edge_color="gray",  # Color of the edges
        )
        frame_path = os.path.join(self.frames_dir, f"frame_{self.time:03d}.png")  # Path to save the frame
        plt.savefig(frame_path)  # Save the figure as a PNG file
        plt.close()  # Close the plot to free memory


    def create_animation(self, output_file="Animations/dfs_animation.mp4"):
        """Create a video from the saved frames."""
        import subprocess
        subprocess.call([
            "ffmpeg", "-y", "-framerate", "2", "-i", f"{self.frames_dir}/frame_%03d.png",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", output_file
        ])
        print(f"Animation saved to {output_file}")

# Example Usage
if __name__ == "__main__":
    G = nx.Graph()
    G = nx.erdos_renyi_graph(10, 0.3)  # Generate a random graph with 10 nodes
    visualizer = DFSVisualizer(G)  # Initialize the visualizer with the graph
    discovery, finish, parents = visualizer.dfs(0)  

    # Create animation
    visualizer.create_animation(output_file="../Animations/anim40.mp4")

    # Print discovery and finish times
    print("Discovery Time:", discovery)
    print("Finish Time:", finish)
    print("Parents:", parents)
