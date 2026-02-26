class Solution(object):
    def returnToBoundaryCount(self, nums):
        position = 0
        count = 0
        
        for move in nums:
            position += move
            if position == 0:
                count += 1
                
        return count