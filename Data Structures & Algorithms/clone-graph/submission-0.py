"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import copy

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        visited = {}

        def dfs(node):
            if node.val in visited:
                return visited[node.val]

            clone = Node(node.val)

            for neighbor in node.neighbors:
                visited[node.val] = clone
                clone.neighbors.append(dfs(neighbor))


            return clone
        
        
        return dfs(node)


            