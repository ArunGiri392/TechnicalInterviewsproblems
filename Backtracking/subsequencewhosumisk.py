def print_subsequences(index, subseq, arr, n, target, sum):
    if index == n:
        if sum == target:
            print(subseq)
        return
    
    # include the current element. 
    subseq.append(arr[index])
    sum += arr[index]
    print_subsequences(index + 1, subseq, arr, n, target, sum)

    sum -= arr[index]
    subseq.pop()# Backtrack to remove the current element

     # Not include the current element
    print_subsequences(index + 1, subseq, arr,n, target, sum)




arr = [1,2,1]
target = 2
print_subsequences(0,[],arr,len(arr), target,0)