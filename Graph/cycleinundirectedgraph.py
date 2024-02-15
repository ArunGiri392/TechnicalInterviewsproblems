def cycle(node, adj):
    queue = []
    visited = set()
    # -1 is to suggest it came from nowhere.
    queue.append((node, -1))
    visited.append(node)

    while queue:
        node, parent = queue.pop(0)
        for adjancecy in node:
            if adjancecy not in visited:
                # visit it.
                queue.append(adjancecy, node)
                visited.append(adjancecy)
            else:
                # if it is already visited.

                # so if it already visited, then we cannot directly say that forms  a cycle.

                # 1 -- 2 ---  3
                # lets say , 1 is our node, which is already visited then , when we explore its adjacent nodes through Loop 
                # then, we get 2 right, for 2 we check its adjacent , ie 1 first, here 1 will be already visited, so can i directly say it is cycle? not, because 2 came from 1, so 1 is preety obvious that is should be visted first.filter
                # so in this case, adjacent node(ie 1) should be equal to the parent(ie where it came from)  of 2, ie 2 came from 1 so 1 == 1, so it is fine. 

                # but if parent != adjacent node, then it means, we are coming from somewhere else to the same point which has alrady been visited, and if we are coming to the visited place from somewhere else, it means, it forms a cycle. because we are coming to the same place form diffrent places.

                if parent != adjancecy:
                    return True
    # if we do all treaversal through bfs then ,we return false suggesting there is no cycle present.
    return False


    # Hi Rasneet Didi, i came to know that you got into a grad school. So much congratulations to you. I know, you might not have made a decision, but still, it is such a good news. Congratulations and so well deserved.