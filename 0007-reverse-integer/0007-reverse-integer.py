class Solution(object):
    def reverse(self, x):
        sign = True
        result = 0

        if x < 0:
            sign = False
            x *= -1

        while(True):
            if x == 0:
                break
            else:
                result *= 10
                result += x % 10
                x /= 10

        if sign is False:
            result *= -1

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return result if INT_MIN <= result <= INT_MAX else 0



        
        