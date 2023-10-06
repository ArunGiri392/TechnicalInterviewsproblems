class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # firstly, convert the prerequsite as a graph relationship.
        # problem says, You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

        # if bi needs to be done before ai , ie bi --> ai which signifies bi needs to be done before ai.
        # so,in graph we keen bi(node) as key and ai as values as it edge.

        # here we have to create a graph for directed graph considering above condition
        graph = defaultdict(list)

        for u, v in prerequisites:
            # here v becomes key and u becomes value because, if bi needs to be done before ai , ie bi --> ai which signifies bi needs to be done before ai.
            graph[v].append(u)
        print(graph)
        
        # kahn's algorithm
#        1) First, we will calculate the indegree of each node and store it in the indegree array. We can iterate through the given adj list, and simply for every node u->v, we can increase the indegree of v by 1 in the indegree array. 

# 2)Initially, there will be always at least a single node whose indegree is 0. So, we will push the node(s) with indegree 0 into the queue.

# 3)Then, we will pop a node from the queue including the node in our answer array, and for all its adjacent nodes, we will decrease the indegree of that node by one. For example, if node u that has been popped out from the queue has an edge towards node v(u->v), we will decrease indegree[v] by 1.

# 4)After that, if for any node the indegree becomes 0, we will push that node again into the queue.
# We will repeat steps 3 and 4 until the queue is completely empty. Finally, completing the BFS we will get the linear ordering of the nodes in the answer array.

# Note: Points to remember when a node is popped out, indegrees for all its adjacent nodes are decreased by one and if any of them becomes 0, we push that node into the queue. Meanwhile, we include the current node in the answer immediately after it is popped out of the queue.

        # toplogical sorting using kanh's algoritm
        # creating a indegre list and length of this will be equal to the numcourses.
        # so basically, we are dealing index as nodes and value at that index as indegree of that node.
        # so if list is [2, 3,4,5 0]
        # then we can say, for node(course) 0, its indegree is 2, for 1, degree is 3 and so on.

        # one question here? but what if the node value is 100?Nice question.
        # but question says, here are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
        # so it says from o to numcourse - 1. so if numcourses is 2 , ie means, those two courses will be 0 and 1 for sure. it starts from 0 and go to n -1.
        indegree = [0]  * numCourses
        
        # here we are calculation the indegree of every node using the ajacencny list graph we made earlier.
        for i in graph:
            for j in graph[i]:
                indegree[j] += 1
        # as per algorithem, we have to append all the nodes who indegree are 0 into queue.
        queue = []
        for i in range(0,len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        # then we queeu, untile queeu is empty, so this is basically a bfs with some slight modifications.
        topo_sort = []
        while queue:
            current_node = queue.pop()
            # we add it our top sort output.
            topo_sort.append(current_node)
            # when a node is popped out, indegrees for all its adjacent nodes are decreased by one and if any of them becomes 0, we push that node into the queue. Meanwhile, we include the current node in the answer immediately after it is popped out of the queue.
            for neighbour in graph[current_node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        print(topo_sort)
        print(numCourses)
        return len(topo_sort) == numCourses

#if len(topo_sort) == numCourses:
#  why this condition works?
# Incomplete Course Ordering: When len(topo_sort) is less than numCourses, it indicates that there are some courses that cannot be scheduled because they have unsatisfied prerequisites. In other words, there is at least one course for which you cannot start because its prerequisites cannot be fulfilled.
