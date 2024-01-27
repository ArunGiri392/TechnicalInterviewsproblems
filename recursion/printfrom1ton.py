# difference on using print statement before recursion call and after recusrion call.
# At first code, we call print before recursion call,
# At second code, we call print after recurison call,
# Through both approaches, adjusting their base condition , we were able to solve problem.


def print_from_1_to_n(current, n):
    if current <= n:
        print(current)
        print_from_1_to_n(current + 1, n)

# Example usage
print_from_1_to_n(1, 5)

def print_to_n(n):
    if n > 0:
        print_to_n(n - 1)
        print(n)

# Example usage
print_to_n(5)

