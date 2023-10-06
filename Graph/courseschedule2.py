class Solution:
   def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # firstly, convert the prerequsite as a graph relationship.
        # Kanh's algorithm to find out the topological sort of the directed graph.

        graph = defaultdict(list)

        # here, we are making a  directed graph.
        #
        for u, v in prerequisites:
            graph[v].append(u)
        print(graph)
        


        # toplogical sorting using kanh's algoritm
        indegree = [0]  * numCourses
        

        for i in graph:
            for j in graph[i]:
                indegree[j] += 1
        queue = []
        for i in range(0,len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
            
        topo_sort = []
        while queue:
            current_node = queue.pop()
            topo_sort.append(current_node)

            for neighbour in graph[current_node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(topo_sort) == numCourses:
            return topo_sort
        return []


 #if len(topo_sort) == numCourses:
#  why this condition works?
# Incomplete Course Ordering: When len(topo_sort) is less than numCourses, it indicates that there are some courses that cannot be scheduled because they have unsatisfied prerequisites. In other words, there is at least one course for which you cannot start because its prerequisites cannot be fulfilled.
