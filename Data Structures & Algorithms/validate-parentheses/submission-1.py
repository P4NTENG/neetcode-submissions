class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}
        for bracket in s:
            if bracket in brackets:
                stack.append(brackets.get(bracket))
            else:
                if bracket != stack.pop():
                    return False

        return True