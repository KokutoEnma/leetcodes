class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        create graph store (i, j) with its children, then BFS/DFS
        """
    
        """
        BFS appears to be slower than DFS and does not pass time limit
        """
        def BFS():
            ret = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] =="1":
                        ret+=1
                        queue = [(i, j)]
                        while len(queue)>0:
                            curr_i, curr_j = queue.pop(0)
                            grid[curr_i][curr_j]="0"
                            if curr_i-1>=0 and grid[curr_i-1][curr_j]=="1":
                                queue.append((curr_i-1, curr_j))
                            if curr_i+1<len(grid) and grid[curr_i+1][curr_j]=="1":
                                queue.append((curr_i+1, curr_j))
                            if curr_j-1>=0 and grid[curr_i][curr_j-1]=="1":
                                queue.append((curr_i, curr_j-1))
                            if curr_j+1<len(grid[i]) and grid[curr_i][curr_j+1]=="1":
                                queue.append((curr_i, curr_j+1))
            return ret
        
        def DFS():
            ret = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] =="1":
                        ret+=1
                        stack = [(i, j)]
                        while len(stack)>0:
                            curr_i, curr_j = stack.pop()
                            grid[curr_i][curr_j]="0"
                            if curr_i-1>=0 and grid[curr_i-1][curr_j]=="1":
                                stack.append((curr_i-1, curr_j))
                            if curr_i+1<len(grid) and grid[curr_i+1][curr_j]=="1":
                                stack.append((curr_i+1, curr_j))
                            if curr_j-1>=0 and grid[curr_i][curr_j-1]=="1":
                                stack.append((curr_i, curr_j-1))
                            if curr_j+1<len(grid[i]) and grid[curr_i][curr_j+1]=="1":
                                stack.append((curr_i, curr_j+1))
            return ret
        
        return DFS()

    
            
            
                        