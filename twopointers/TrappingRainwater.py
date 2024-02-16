class Solution:
    def trap(self, height: List[int]) -> int:

        # The idea is. 
        # for each index, we calculate what is the greatest height on its left side and greatest height on its right side.
        # and we take the smaller(minimum) from greatest height on left side and greatest heigh on right side for each index.
        # then that gives us level, but that index could also have some height. so, we have to decrease that height.

        # min(left_greast, right_greatest) - height[index]

            left = []
            right = []


            left_greatest = 0
            right_greatest = 0
            # calculating the left greatest for each index.
            for i in range(0, len(height)):

                if height[i] > left_greatest:
                    left.append(height[i])
                    left_greatest = height[i]
                else:
                    left.append(left_greatest)
            
             # calculating the right greatest for each index.
            for i in range(len(height) -1, -1, -1):

                if height[i] > right_greatest:
                    right.append(height[i])
                    right_greatest = height[i]
                else:
                    right.append(right_greatest)
            
            # remember, the right greatest is in opposite order.
            # then, we store the minimum of each index in minimum array.
            minimum = []

            for i in range(0, len(height)):
                minimum.append(min(left[i], right[len(height) - i - 1]))

            # then by using minimum of each index, we calculate whether it can store water or not.
            water = 0
            for i in range(0, len(height)):
                
                water += minimum[i] - height[i]
            return water
    # Time complexity - o(N)
    # space complexity - o(N)
            
            # could be done i o(1) space complexity using two pointers.

            if not height:
                return 0
            
            left = 0
            right = len(height) - 1

            left_max = height[left]
            right_max = height[right]
            water = 0

            while left < right:

                if left_max < rightmax:
                    
                    left += 1
                    left_max = max(left_max, height[i])
                    water += leftmax - height[left]

                else:
                    right -= 1
                    right_max = max(right_max, height[i])
                    water += rightmax - height[right]
            return water
            