class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        for i in range(len(x)):
            l = i
            r = len(x) - 1 - i

            if x[l] != x[r]:
                return False
            
        return True