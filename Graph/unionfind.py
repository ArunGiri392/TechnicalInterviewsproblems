# Firstly, the Union function requires two nodes(let’s say u and v) as arguments. Then we will find the ultimate parent (using the findPar() function that is discussed later) of u and v. Let’s consider the ultimate parent of u is pu and the ultimate parent of v is pv.
# After that, we will find the rank of pu and pv.
# Finally, we will connect the ultimate parent with a smaller rank to the other ultimate parent with a larger rank. But if the ranks are equal, we can connect any parent to the other parent and we will increase the rank by one for the parent node to whom we have connected the other one

class UnionFind:
    def __init__(self, n):
        # intially, all nodes are parent of themselves.
        self.parent = {}
        self.rank = []
        # initally, all nodes have a rank of 0.

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0
    
    # this will find the ultimate parent.
            
    def find_parent(self, n):
        parent = self.parent[n]
        while parent != self.parent[parent]:
            # doing path compression. 
            # it is updating the parent of given vertex to point to the grandparent.
            self.parent[parent] = self.parent[self.parent[parent]]
            parent = self.parent[parent]
        return parent
        
    def union(self, n1, n2):
        # n1 and n2 are two nodes and we do union on these.

        parent1 = self.find_parent(n1)
        parent2 = self.find_parent(n2)

        if parent1 == parent2:
            return 
        
        # if rank of parent1 is greater than rank of parent 2,
        # then take parent2 and make it as child of parent1.join it.
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
         
        # if rank of parent2 is greater than rank of parent 2,
        # then take parent1 and make it as child of parent2.join it.
        elif self.rank[parent2] > self.rank[parent1]:
             self.parent[parent1] = parent2
        # if rank of parent1 and parent2 are equal.
        # we could change anyone to anyone.
             # here we take parent1, and connect it to parent2.
             # so rank of parent2 also increments by 1.
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += 1
            
# Time space complexity.
#             In the naive case, the find function will result in 
# 
# O(n) because it is possible that the tree is just a chain like a linked list and we have to traverse every single node. With path compression, since we are updating the parent to be the grandparent each time, we can reduce the complexity down to 
# 
# O(logn).

# If we combine it with the union function, we get a time complexity called Inverse Ackermann, 
# 
# α(n), which can be simplified to constant time, 
# 
# O(1). So, if 

# m is the number of edges we have, then the time complexity of Union-Find is 
# 
# )
# O(m ∗ logn).

