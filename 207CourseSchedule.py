class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        """
        Use a list to keep the order or courses to take
        at the end if then length of the list === numCourses then return True
        
        
        store each node's child degree
        0 child degree can add to list
        each time visite the node reduce child degree by 1
        
        the list order means take the course in desc         
        """
        child_degree = {n:0 for n in range(numCourses)}
        graph = {n:[] for n in range(numCourses)}
        for parent, child in prerequisites:
            child_degree[child]+=1
            graph[parent].append(child)
        
        def BFS():
            queue, li = [], []
            for c in child_degree:
                if child_degree[c]==0: queue.append(c)
            while len(queue)>0:
                curr = queue.pop(0)
                li.append(curr)
                for child in graph[curr]:
                    child_degree[child]-=1
                    if child_degree[child]==0:
                        queue.append(child)
            return True if len(li)==numCourses else False
        
        def DFS():
            stack, li = [], []
            for c in child_degree:
                if child_degree[c]==0: stack.append(c)
            while len(stack)>0:
                curr = stack.pop()
                li.append(curr)
                for child in graph[curr]:
                    child_degree[child]-=1
                    if child_degree[child]==0:
                        stack.append(child)
            return True if len(li)==numCourses else False
        
        return DFS()
        
        
        
        
        
            
        
                
                