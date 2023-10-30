# # The first one is the brute force soln
# if i find, none then it is not cycle.
# else i will go on circular linked list but question says, there can be 10to power of 4 nodes at max
# so if i travel more than this no of nodes, than i know i am in the cycle.else
# but even for the one node, i have to move for 10,000 times which is the worst. 
def hascycle():
    temp = head
    while temp != None and  count < 10000:
        temp = temp.next
        count += 1
        if temp == None:
            return False
        return True


# This is the second soln using hashset.
# store the nodes i have seen previously  in the set and if i see same node , then it is cycle.
# else, if i see none then it is not.
# remember: a node has its address so even if there are two nodes that has two same values and two same next (ie 2 points to 3 and another 2 points to 3)
# still, these two nodes are different, because they have two different memory address.
# if i go on cycle, and encounter same node i encountered previously, then the memory adress is same and they are same.
        def hascycle():
            hash_set = set()
            temp = head
        while temp != None:
            if temp not in hash_set:
                hash_set.add(temp)
                temp = temp.next
            else:
                return True
        return False

# keeping two pointer - one pointer move fast and another move slow
# slow - moves one Step , fast moves two step and there will be point that
# fast will meet slow if there is a cycle and when they meet, you knwow it is cycle.
        # using floys's algorithm - two pointers
def hascycle():
    slow_pointer = head
    fast_pointer = head
    while fast_pointer != None and fast_pointer.next != None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            return True
    return False
