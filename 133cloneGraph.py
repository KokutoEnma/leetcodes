"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node: return None
        
        head=Node(val=node.val)
        
        visited = {}
        visited[node.val] = (head)
        q = [node]
        
        while len(q)>0:
            
            curr = q.pop()
            cloneNode = visited[curr.val]
            
            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    q.append(neighbor)
                    newNode = Node(neighbor.val)
                    visited[neighbor.val] = newNode
                else:
                    newNode = visited[neighbor.val]
                cloneNode.neighbors.append(newNode)
                    
             
        return head
        