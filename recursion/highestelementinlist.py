def highestelement(list,n):
    if n == 0:
        print("list is empty")
    if n == 1:
        return list[n]
    
    max_in_rest = highestelement(list,n-1)

    if max_in_rest != None and max_in_rest > list[n-1]:
        return max_in_rest
    else:
        return list[n-1]

print(highestelement([2,1,4,5], 4))

#                recursive cases 
#                [2,1,4,5] -- 4
#                [2,1,4,5] -- 3
#                [2,1,4,5] -- 2
#                [2,1,4,5] -- 1
#                here now, n == 1: 
#                so , it returns 2 ie  return list[n] and our n is 1 in this case.
#                where does it return? it returns to its caller and who is the caller ? 
#                [2,1,4,5] -- 2 here this is the caller  such that max_in_rest = highestelement(list,n-1) becomes:
#                max_in_rest = 2 now it got some value then code below it willhave to execute for that call.
      
#               if max_in_rest != None and max_in_rest > list[n-1]:
#         return max_in_rest
#     else:
#         return list[n-1]
# basically we are comparing maxinrest in this case 2 with (n-1) in this call, n =2 so (n-1 ) =1 so list[1] =1  so
#  we compare 2 and  1 and continue this process and return continously.
