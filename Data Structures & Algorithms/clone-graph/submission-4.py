"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        visited = set()
        d = {}

        def dfs(cur):
            newNode = Node(cur.val, [])
            visited.add(cur)
            d[cur] = newNode
            for nei in cur.neighbors:
                if nei not in visited:
                    newNode.neighbors.append(dfs(nei))
                else:
                    newNode.neighbors.append(d[nei])
            
            return newNode
        
        return dfs(node)