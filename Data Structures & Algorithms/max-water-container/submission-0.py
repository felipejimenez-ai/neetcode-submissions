class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        l, r = 0, len(height) - 1
        d, h = 0, 0

        while l < r:
            d = r - l
            h = min(height[l], height[r])
            # print(l, r, height[l], height[r])
            
            if d * h > max: max = d * h

            if height[l] < height[r]: l += 1
            elif height[l] > height[r]: r -= 1
            else: l += 1
        
        return max