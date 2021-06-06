class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        
        """
        run BFS or DFS from each contour node
        A: store nodes can go atlantic
        B: store nodes can go pacific
        return nodes can go both ocean
        """
        
        n_row, n_col = len(heights), len(heights[0])
        
        pacific = []
        atlantic = []
        for i in range(n_row):
            for j in range(n_col):
                if i==0 or j==0: pacific.append((i,j))
                if i+1==n_row or j+1==n_col: atlantic.append((i,j))
        
        
        def BFS(queue):            
            cango = set(queue)
            
            while len(queue)>0:
                i, j = queue.pop(0)
                
                children = [(i+1,j), (i, j+1), (i-1,j), (i, j-1)]
                children = [(i,j) for i, j in children if i>=0 and j>=0 and i<n_row and j<n_col and (i, j) not in cango]
                for c_i, c_j in children:
                    if (c_i, c_j) not in cango and heights[c_i][c_j]>=heights[i][j]:
                        queue.append((c_i,c_j))
                        cango.add((c_i, c_j))
            return cango
        
        def DFS(stack):
            cango = set(stack)
            
            while len(stack)>0:
                i, j = stack.pop()
                
                children = [(i+1,j), (i, j+1), (i-1,j), (i, j-1)]
                children = [(i,j) for i, j in children if i>=0 and j>=0 and i<n_row and j<n_col and (i, j) not in cango]
                for c_i, c_j in children:
                    if (c_i, c_j) not in cango and heights[c_i][c_j]>=heights[i][j]:
                        stack.append((c_i,c_j))
                        cango.add((c_i, c_j))
            return cango
        
        pacific = DFS(pacific)
        atlantic = DFS(atlantic)
        return pacific & atlantic
                        
                