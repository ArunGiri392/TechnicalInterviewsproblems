class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack -- increasing
        result = [0] * len(temperatures)
        stack = []

        for i in range(0,len(temperatures)):

            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            
            stack.append(i)
        return result