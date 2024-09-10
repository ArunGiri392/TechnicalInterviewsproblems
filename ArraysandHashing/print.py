array = [[5, 10], [2, 5], [4, 7], [3, 9]]

# Sort the list based on the second element of each sublist in ascending order
sorted_array = sorted(array, key=lambda x: x[1])

print(sorted_array)