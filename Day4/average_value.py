class Solution(object):
    def averageValue(self, nums):
        total = 0
        count = 0
        
        for num in nums:
            if num % 6 == 0:
                total += num
                count += 1
        
        if count == 0:
            return 0
        
        return total // count