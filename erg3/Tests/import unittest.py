import unittest
import networkx as nx
import os
from src.visual import DFSVisualizer
import shutil



class TestDFSVisualizer(unittest.TestCase):

    def setUp(self):
        self.graph = nx.Graph()
        self.graph.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3)])  # Example graph
        self.visualizer = DFSVisualizer(self.graph)

    def tearDown(self):
         # Clean up the frames directory after each test
        if os.path.exists(self.visualizer.frames_dir):
            shutil.rmtree(self.visualizer.frames_dir)

    def test_dfs_traversal(self):
        discovery, finish, parent = self.visualizer.dfs(0)

        # Check discovery and finish times
        self.assertEqual(discovery[0], 1)
        self.assertEqual(finish[0], 8)
        self.assertEqual(discovery[1], 2)
        self.assertEqual(finish[1], 5)
        self.assertEqual(discovery[2], 6)
        self.assertEqual(finish[2], 7)
        self.assertEqual(discovery[3], 3)
        self.assertEqual(finish[3], 4)


        # Check parent relationships
        self.assertIsNone(parent[0])
        self.assertEqual(parent[1], 0)
        self.assertEqual(parent[2], 0)
        self.assertEqual(parent[3], 1)


    def test_dfs_disconnected_graph(self):
        self.graph.add_node(4)  # Add a disconnected node
        discovery, finish, parent = self.visualizer.dfs(0)

        # Check that the disconnected node is not visited
        self.assertNotIn(4, discovery)
        self.assertNotIn(4, finish)
        self.assertEqual(parent[4], None) # Parent should be None since it's disconnected and unvisited


    def test_dfs_empty_graph(self):
        empty_graph = nx.Graph()
        visualizer = DFSVisualizer(empty_graph)
        discovery, finish, parent = visualizer.dfs(0)
        self.assertEqual(discovery, {})
        self.assertEqual(finish, {})
        self.assertEqual(parent, {})

        discovery, finish, parent = visualizer.dfs(None)  # Test with None and empty graph
        self.assertEqual(discovery, {})
        self.assertEqual(finish, {})
        self.assertEqual(parent, {})


    def test_save_frame(self):
        self.visualizer.dfs(0) # Call dfs to save some frames
        frame_count = len([name for name in os.listdir(self.visualizer.frames_dir)
                           if os.path.isfile(os.path.join(self.visualizer.frames_dir, name))])
        self.assertEqual(frame_count, 8)  # Check that 8 frames (discovery + finish for 4 nodes) are saved



if __name__ == '__main__':
    unittest.main()
