
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors 


class Solution(object):
    def cloneGraph(self, node):
        # The idea here is to create a copy of the whole graph.
        # you have to make copy of each node and also that connection.
        # We will implement it with BFS such that we travel all nodes through it, while we traverse , we make a copy of the original node.
        # The original node has value and its neighbours in the list.

    # we will use hashmap to keep track of which nodes we have copied thus far such that we do not make a copy of same node again.
    # In hashmap, we keep key as real node and value as copy node.
    # to make the connection(edge) of copy node with other nodes, we can append the nodes in the neighbout list of copy node.
    
        if node == None:
            return None
            # creating a hashmap that keeps key as real node and value as copy node.
        map = {}
        # queue for DFS.
        queue = []

        # make a copy node
        # right now, this copy node has val same as real node but it neighbours are None at moment, we want to fill it with its neighbour nodes.
        copy_node = Node(node.val)
        map[node] = copy_node

        # adding original node to queue.
        # we want to add original node to queue becuase we know the neighbours of original node, not the neighbours of copy node.
        queue.append(node)

        while queue:
            # pop the node from queue.
            current_node = queue.pop(0)
            # now for that node, iterate through the neighbours of that node.
            for neighbour in current_node.neighbors :
                # if that neighbour is something we have seen first time and not present in hashmap, then we create a copy of that node.
                if neighbour not in map:
                    # create a copy of that node.
                    neighbour_copy = Node(neighbour.val)
                    # add its real node and copy in hashmap
                    map[neighbour] = neighbour_copy
                    # add to the queue.
                    queue.append(neighbour)
                # Here if neighbour is map or not, this code executes, because we want to make that connection(edge) with another node.
                # so for current node, we know, its value is copy node and because we are making copy, we want to add neighbours for the copy node. so. 
                # by doing, map[current_node], we get a copy node of current node.
                # by doing, map[current_node].neighbors, we get a lsit of neighbours of copy node which is empty initially.
                #  then, we want to append neighbour on it.
                # so we append, map[neighbour]
                # why node,just neighbour, because neighbour is a original node, not a copy node, and for copy node, we want to append the copy of neighbour node.
                #why map[neighbour] because map[nieghbour] gives value which holds the copy node.

                map[current_node].neighbors.append(map[neighbour])
        # the question says, return the first copy node.
        # and in hashmap, we know node represent the first node and its copy is stored along with it.
        return map[node]
