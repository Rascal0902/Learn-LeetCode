class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        x = 1
        y = 2
        temp = 0

        for i in range(3, n+1):
            temp = x + y
            x = y
            y = temp

        return temp
        