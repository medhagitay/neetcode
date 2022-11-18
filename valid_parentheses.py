class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict_arr={"]":"[",")":"(","}":"{"}
        for chars in s:
            if chars in dict_arr:
                firstele=stack.pop() if stack else '#'
                if dict_arr[chars]!=firstele:
                    return False
            else:
                stack.append(chars)
        return not stack
