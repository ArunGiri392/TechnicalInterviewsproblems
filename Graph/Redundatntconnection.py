class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {}
        rank = {}

        Nodes = len(edges)
        for i in range( 1, Nodes + 1):
            parents[i] = i
            rank[i] = 0
        


        def find_ultimate_parent(node):
            parent = parents[node]
            while parent != parents[parent]:
                # parent = parents[parent[parent]]
                parent = parents[parent]
            return parent


        
        def find_union(n1, n2):
            
            parent1 = find_ultimate_parent(n1)
            parent2 = find_ultimate_parent(n2)

            if parent1 == parent2:
                return False
            
            if rank[parent1] > rank[parent2]:
                parents[parent2] = parent1
            elif rank[parent2] > rank[parent1]:
                parents[parent1] = parent2
            else:
                parents[parent1] = parent2
                rank[parent2] += 1
            return True
        

        for edge in edges:
            if find_union(edge[0], edge[1]) == False:
                return edge
            
