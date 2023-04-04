class Stack():
    def __init__(self):
        self._stack = []

    def push(self, parenthesis):
        self._stack.append(parenthesis)

    def pop(self):
        return self._stack.pop()

    def len(self):
        return len(self._stack)


class Solution:
    PARENTHESIS = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    def is_valid(self, s: str) -> bool:
        stack = Stack()

        for parenthesis in s:
            if parenthesis in self.PARENTHESIS:
                stack.push(parenthesis)
            else:
                if stack.len() == 0:
                    return False
                last_open_parenthesis = stack.pop()
                if self.PARENTHESIS[last_open_parenthesis] != parenthesis:
                    return False

        return stack.len() == 0
