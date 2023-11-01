class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # idea.
        # 1) if it is operand(number) add it to the stack
        # 2) if it is operator, 
        # then pop out the two data from stack
        # and do operation like second pop (/ + * 0) firsoperand
        # and after that also add this new expression to stack. 
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        operators = ["+", "-", "*", "/"]
        for data in tokens:
            if data not in operators:
                stack.append(data)
            else:
                first_popped = int(stack.pop())
                second_popped = int(stack.pop())

                if data == "+":
                    expression = second_popped + first_popped
                elif data == "-":
                    expression = second_popped - first_popped
                elif data == "*":
                    expression = second_popped * first_popped
                elif data == "/":
                    expression = second_popped / first_popped
                stack.append(expression)
        return int(expression)
# Time complexity - o(N)
# space complexity - o(N)
