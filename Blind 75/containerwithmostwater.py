class Solution:
    def maxArea(self, height: List[int]) -> int:
        # # problem statement -- using two pointers concepts.
        # o(n2) solution for this problem is straght forward so i have to think of o(n)
        # for any pillar, we can think what could be the maximum water it could hold?
        # it could hold, maximum, when its distance to another pole keeps on increasing. 
        # meaning to increase the distance, we could keep two pointers, where one pointer is on th eleftmost part and the other one is on the rightmost part.

        # in that way, we could have the maximum distance and calcuate its maximum possibility of water.
        # but lets say: our left pillar is smaller than the right most pillar, than for left pilllar, we could calcualte its maximum area, but what if left most is taller than the right most, meaning in this case.
        # we cannot directly, say, hey left most pillar , breath is maximum to right pillar and calcualte. left most pillar could pair with any other pillar in middle too to have maxiumum area.

        # so the point is. we need to pick the smaller in between left and right, and by doing so, we make sure that we calcuate the maximum for that smaller one because for smaller one, it id guranteed that , that range is the maxium breath and also the maximum area. 
        # so once we calcualte for smaller, we increment or decrement the pointer depending upon, wehich side the smaller values lies. in. 
          left = 0
          right = len(height) - 1
          max_area = 0
          area = 1
          while left < right:
              area = min(height[left],height[right]) * (right - left)
              max_area = max(area, max_area)

              if height[left]  < height[right]:
                  left += 1
              else:
                  right -= 1
          return max_area

# Timecompexity - o(N)
# SpaceComplexity -o(N)