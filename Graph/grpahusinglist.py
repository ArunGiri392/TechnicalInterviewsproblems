
# THis function works fine well for directed, undirected or weighted graph 
#because we are inserting a new node and driection and weight of graph is dependent
#upon edge, it is connected to edge, not connected to node.

# but while adding new edge, we need to consider cases seperaely
#for directed, or undirected or weighted graph.

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


#code for the undirected weighted graph:
# def add_edge(v1,v2,cost):
    

#     # check if vertices are present in graph or not.
#     if v1 not in graph:
#         print(v1,"is not present in the graph")
#     elif v2 not in graph:
#         print(v2,"is not present in the graph")
#     else:
#         list1 = [v2,cost]
#         list2 = [v1,cost]
#         graph[v1].append(list1)
#         graph[v2].append(list2)

#code for the directed weighted graph:
# because this is direcetd, we dont have to change two sides so , only change is:
# remove, list2 = [v1,cost] graph[v2].append(list2) from above function and everything is write.

# code for undirected, unweighted graph
def delete_node(v):
    if v not in graph:
        print(v,"is not present in the graph")
    else:
        # remove that node from the graph
        graph.pop(v)
        # now i have to remove edges coming to that node.
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)

# code for undirected, weighted graph
# def delete_node(v):
#     if v not in graph:
#         print(v,"is not present in the graph")
#     else:
#         # remove that node from the graph
#         graph.pop(v)
#         # now i have to remove edges coming to that node.
#         # it is in two 2d . [edge, weight]
#         # travel in two 2d list and delete it
#         for i in graph:
#             list1 = graph[i]
#             for j in list1:
#                 if v == j[0]:
#                     list1.remove(j)
#                     # once i remove it, cause one node will only have one edge, so we dont have to check others.
#                     break

#code for undirected, unweighted graph
def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        # the else condition is required here,  because even if A and B (lets say) are present, but there is a change there might not be a edge between them
        # and if there is not edge and if you directly try to delete anyting from list, without checking if actually it is there, then there will be error.
        # so we must use this if condition.
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)
        
        # for the directed graph, the same code works , only remove  graph[v2].remove(v1) from the code.
    
   # for undirected weighted graph

# def delete_edge(v1,v2,cost):
#     if v1 not in graph:
#         print(v1,"is not present in the graph")
#     elif v2 not in graph:
#         print(v2,"is not present in the graph")
#     else:
#         temp = [v1,cost]
#         temp1 = [v2,cost]
#         if temp1 in graph[v1]:
#             graph[v1].remove(temp1)
#             graph[v2].remove(temp)
        
       


graph = {}
add_node("A")
add_node("B")
add_node("C")
print('Graph after adding nodes')
print(graph)
add_edge("A","B")
add_edge("A","C")
add_edge("B","C")
print("Graph after adding edges")
print(graph)
print("Graph after deleting Node A")
delete_node("A")
print(graph)
print("Graph after deleting edge between B and C")
delete_edge("B", "C")
print(graph)