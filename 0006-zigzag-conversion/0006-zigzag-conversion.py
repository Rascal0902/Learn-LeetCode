class Solution(object):
    def convert(self, s, numRows):
        result = ""

        if numRows == 1:
            return s

        for i in range(numRows):
            temp = i
            isEven = True

            if i == 0 or i == numRows - 1:
                while(True):
                    if temp < len(s):
                        result += s[temp]
                        temp += 2 * numRows - 2
                    else:
                        break

            else:
                while(True):
                    if temp >= len(s):
                        break

                    result += s[temp]
                    if isEven:
                        temp += 2 * numRows - 2 - 2 * i
                    else:
                        temp += 2 * i

                    isEven = not isEven

        return result




        