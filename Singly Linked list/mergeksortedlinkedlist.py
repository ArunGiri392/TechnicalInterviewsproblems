# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0 :
            return None
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # The idea here is to break down this problem meaning, we already know how to merge two linked list right?
        # so what could we do to merge k list? continously merge two list and make them one, and do same for other,
        # and continue this process until we get to the last list.

        # solution here.
        # we already have the merge list function which takes two linkedlist and merge them.
        # we have the lists of merge list in lists. so we want to send two list into this function and in return we get the merge linkedlist for those lists. meanng, we want to iterate in the given list, take two list and go on. 
        # we increment i by 2, because when i = 0, we can send first and second list from list[i], list[i + 1] and we inrement i by 1, again we will send same list, so increment i by 2, to send third list.
        # so we keep on send these two lists and keep on getting merge list,
        # we stored merge list into merge_lists. and on first iteration, letss ay, there were 8 linked list and we got to 4 linked list by merging them . now we do the same process, so make our original list as merge list and continue the process untile length of this length becomes one,
        # when it becomes one, we know all of them are merged , and we pass the soluiton.

        while len(lists) > 1:
            merged_lists = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                # this if condition is needed, because we are accessing i + 1 , in else condition, meaning if i reaches at end, then it will go out of bound, in that case, we send the last list and none, to merge function and we know merge does work if there is one list and another is none
                if i == len(lists) - 1:
                    list2 = None
                    
                else:
                    list2 = lists[i + 1]

                merged_lists.append(self.merge_list(list1,list2))
            lists = merged_lists
        return lists[0]


    def merge_list(self,p,q):
        dummy =  ListNode(0)
        temp = dummy
        while p != None and q != None:
            if p.val < q.val:
                temp.next = p
                p = p.next
            else:
                temp.next = q
                q = q.next
            temp = temp.next
        if p == None:
            temp.next = q
        if q == None:
            temp.next = p
        return dummy.next
    
