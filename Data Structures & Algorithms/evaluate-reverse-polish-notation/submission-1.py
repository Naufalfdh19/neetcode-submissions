class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []

        for token in tokens:
            if token in "+-*/":
                # print("[START] stack: ", stack)
                second = stack.pop()
                first = stack.pop()
                stack.append(self.operate(first, second, token))
                # print("[END] stack: ", stack)
            
            else:
                stack.append(token)
        
        return int(stack[0])

        

    def operate(self, first, second, operation):
        first = int(first)
        second = int(second)
        # print("first: ", first, "second: ", second)
        if operation == "+":
            return str(first+second)
        elif operation == "-":
            return str(first-second)
        elif operation == "*":
            return str(first*second)
        
        division = first/second

        if division < 0:
            return str(math.ceil(division))

        return str(math.floor(first/second))