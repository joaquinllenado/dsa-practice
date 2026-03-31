class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if (t == '+'):
                stack.append(stack.pop() + stack.pop())
            elif (t == '-'):
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 - num2)
            elif (t == '*'):
                stack.append(stack.pop() * stack.pop())
            elif (t == '/'):
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(float(num1) / num2))
            else:
                stack.append(int(t))
        return stack[0]