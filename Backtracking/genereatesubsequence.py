def print_subsequences(index, subseq, arr, n):
    if index == n:
        print(subseq)
        return
    # include the current element.
    subseq.append(arr[index])
    print_subsequences(index + 1, subseq, arr, n)

    subseq.pop()# Backtrack to remove the current element
    
     # Not include the current element
    print_subsequences(index + 1, subseq, arr,n)




arr = [3,1,2]
print_subsequences(0,[],arr,len(arr))