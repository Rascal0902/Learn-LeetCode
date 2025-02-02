class Solution(object):
    def isValid(self, s):
        storage = ""

        for i in range(len(s)):
            if s[i] == ")" and len(storage) != 0 and storage[-1] == "(":
                storage = storage[:-1]
            elif s[i] == "}" and len(storage) != 0 and storage[-1] == "{":
                storage = storage[:-1]
            elif s[i] == "]" and len(storage) != 0 and storage[-1] == "[":
                storage = storage[:-1]
            else:
                storage += s[i]

        return True if storage == "" else False
        