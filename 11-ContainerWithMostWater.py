class Solution(object):
    def maxArea(self, height):
        n = len(height)
        left = 0
        right = n-1
        max_value = 0
        while left!=right:
            if max_value < (right-left)*min(height[left], height[right]):
                max_value = (right-left)*min(height[left],height[right])
            if height[left] < height[right] or height[left] == height[right]:
                left = left+1
            else:
                right = right-1
