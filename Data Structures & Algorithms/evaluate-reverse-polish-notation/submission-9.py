from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = [int(tokens[0]), int(tokens[1])]

        for token1 in tokens[2:]:
            if token1 == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif token1 == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif token1 == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif token1 == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))  # truncate immediately
            else:
                stack.append(int(token1))

        return stack[0]