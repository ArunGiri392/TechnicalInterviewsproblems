class UnionFind:
    def __init__(self, n):
        self.parents  = {}
        self.rank = {}

        for i in range(0, n):
            self.parents[i] = i
            self.rank[i] = 0
        
    def find_parent(self,node):
        parent = self.parents[node]
        while parent != self.parents[parent]:
            parent = self.parents[parent]
        return parent

    def find_union(self, n1, n2):
        p1 = self.find_parent(n1)
        p2 = self.find_parent(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
        
        elif self.rank[p2] > self.rank[p1]:
            self.parents[p1] = p2
        else:
                self.parents[p1] = p2
                self.rank[p2] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        for edge in edges:
            dsu.find_union(edge[0], edge[1])


        unique_parents = set()
        for i in range(0, n):
            parent = dsu.find_parent(i)
            print(parent)
            unique_parents.add(parent)
        print(unique_parents)
        return len(unique_parents)

