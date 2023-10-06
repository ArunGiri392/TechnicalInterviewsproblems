class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if edges == []:
            return True
 
        graph = defaultdict(list)
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        #print(graph)
        queue = []

        visited = set()
        queue.append(source)
        visited.add(source)

        while queue:
            current_node = queue.pop(0)
            for adjacent_node in graph[current_node]:
                print(adjacent_node)
                if adjacent_node == destination:
                    return True
                if adjacent_node not in visited:
                    visited.add(adjacent_node)
                    queue.append(adjacent_node)
        return False

