# we will have two list
# first list is to store all the nodes in graph
# the other is to store the matrix(1 and 0)

def add_node(v):
    global node_count
    # checking if node is present already
    if v in nodes:
        print(v, "is already present in the graph")
    else:
        # add that node in the graph
        node_count += 1
        # we also append the new node to our node list
        nodes.append(v)
        # we need to add a new column upon adding a new node.
        for n in graph:
            n.append(0)
        # we also need to add a new row
        # ie basically adding a new list . 
        # and we also add 0 on it, how many ??
        # we add equal to the no of nodes.
        temp = []
        for i in range(0,node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2,cost):
    # function for undirected, unweighted graph
    # but you can always make minor changes here for this func to work for 
    # undirected weighted graph, weighted directed graph, weighted undirected graph
    # we want to check if that node is in graph or not.
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")
    else:
        # here we want to find where the index is located.
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v, "is not present in the graph")

    else:
        # finding the index at which node is present such that we can delete the row and column from the matrix
        index1 = nodes.index(v)
        # when we delete that node, we need to remove it from nodes list and also decrement the no of nodes from nodes
        node_count -= 1
        nodes.remove(v)
        # removing that row 
        graph.pop(index1)
        # remove column, we cannot directly delete the column like row.
        # so the idea is to go through each row and delete the value from each row. 
        for i in graph:
            i.pop(index1)

def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1, "is not present in the Graph")
    elif v2 not in nodes:
        print(v2, "is not present in the Graph")
    else:
        # this is for undirected, unweighted graph.
        # this also works for undirected, weighted graph .
        index_of_v1 = nodes.index(v1)
        index_of_v2 = nodes.index(v2)
        # we basically have to make that value in matrix as 0.
        graph[index_of_v1][index_of_v2] = 0
        graph[index_of_v2][index_of_v1] = 0

        # for directed . we just do this: 
        # index_of_v1 = nodes.index(v1)
        #index_of_v2 = nodes.index(v2)
        # graph[index_of_v1][index_of_v2] = 0
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"), end=" ")
        print()

nodes = []
graph = []
node_count = 0
print("Before adding nodes")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("D")
add_edge("A","B",50)
add_edge("A","D",40)

print("after adding nodes")
print(nodes)
print(graph)
print_graph()
print()
delete_node("B")
print("after deleting nodes")
print(nodes)
print(graph)
print_graph()