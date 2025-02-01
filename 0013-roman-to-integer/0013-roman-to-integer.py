class Solution(object):
    def romanToInt(self, s):
        result = 0
        Pass = False
        for i in range(len(s)):
            if Pass:
                Pass = False
                continue
            if s[i] == 'I':
                if i+1 < len(s) and s[i+1] == 'V':
                    result += 4
                    Pass = True
                elif i+1 < len(s) and s[i+1] == 'X':
                    result += 9
                    Pass = True
                else:
                    result += 1
            elif s[i] == 'V':
                result += 5
            elif s[i] == 'X':
                if i+1 < len(s) and s[i+1] == 'L':
                    result += 40
                    Pass = True
                elif i+1 < len(s) and s[i+1] == 'C':
                    result += 90
                    Pass = True
                else:
                    result += 10
            elif s[i] == 'L':
                result += 50
            elif s[i] == 'C':
                if i+1 < len(s) and s[i+1] == 'D':
                    result += 400
                    Pass = True
                elif i+1 < len(s) and s[i+1] == 'M':
                    result += 900
                    Pass = True
                else:
                    result += 100
            elif s[i] == 'D':
                result += 500
            elif s[i] == 'M':
                result += 1000
    
        return result