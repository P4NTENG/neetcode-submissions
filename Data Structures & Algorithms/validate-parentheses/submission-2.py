class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}
        for bracket in s:
            try:
                if bracket in brackets:
                    stack.append(brackets.get(bracket))
                else:
                    if bracket != stack.pop():
                        return False
            except IndexError:
                return False
        return True

        return True