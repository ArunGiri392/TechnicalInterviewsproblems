def add_node(v):
    #if node
    if v in graph:
        print(v,"is already present in graph")
    else:
        # adding a node with empty list
        # empty list suggest it does not have any adjacent nodes.
        graph[v] = []

def add_edge(v1,v2):
    # writing for undirected unweighted, graph
    
    # check if vertices are present in graph or not.
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        graph[v1].append(v2)
        #graph[v1] here we acess the key from dictionary which is list 
        # and then append the v2
        graph[v2].append(v1)

def DFS_recursive(node,visited,graph):
    # if provided node is not present in the graph
    if node not in graph:
        print(node,"is not present in the Graph")
        return
    # node represent the starting node
    # firstly, i will check if node is visited or not. 
    if node not in visited:
        # now i will visit that node.
        print(node)
        # now mark that node as visited 
        visited.add(node)
        # to access the all the adjacent nodes of that current node
        for i in graph[node]:
            DFS_recursive(i,visited,graph)
        
        # for the weighted graph, which will have 2d list cause [b, 10] we have node and cost,
        # we do this: DFS(i[0], visited, graph) inside the loop , this is only the change we need to make
        # because on doing i , we access [b,10] and on doing i[0] we access b which is the node and we pass it to the recursive function

def DFS_iterative(node,graph):
    #visited could also be defined here, cause this is not a recursion and iterative.
    if node not in graph:
        print(node,"is not present in the Graph")
        return
    
    visited = set()
    stack = []

    #push starting node to stack
    stack.append(node)
    visited.add(node)
    while stack: 

        currentnode = stack.pop()
        print(currentnode)
        # get all the adjacent nodes of all the current nodes and push it in the stack
        for adjacent_node in graph[currentnode]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
                visited.add(adjacent_node)


def BFS_iterative(node,graph):
    if node not in graph:
        print(node, "is not present in the graph")
        return 
    visited = []
    queue = []
        # push starting node to queue
    visited.append(node)
    queue.append(node)
    while queue:
        current_node = queue.pop(0)
        print(current_node)
        for adjacent_node in graph[current_node]:
            if adjacent_node not in visited:
                visited.append(adjacent_node)
                queue.append(adjacent_node)
     
    
# step , path -- BFS
#count, connect -- DFS
visited = set()
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A","B")
add_edge("B","E")
add_edge("A","C")
add_edge("A","D")
add_edge("B","D")
add_edge("C","D")
add_edge("E","D")
print(graph)

DFS_iterative("A",visited,graph)