class Solution(object):
    def maxDepth(self, s):
        current_depth = 0
        max_depth = 0
        
        for ch in s:
            if ch == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif ch == ')':
                current_depth -= 1
                
        return max_depth