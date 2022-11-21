class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {')':'(', ']':'[', '}':'{'}

        for bracket in s:
            if bracket in check:
                if stack and stack[-1] == check[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False
