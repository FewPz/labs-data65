class ArrayStack:
    
    def __init__(self) -> None:
        self.data = []
        
    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, e):
        self.data.append(e)
        
    def pop(self):
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
        else:
            return self.data.pop()

    def stackTop(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]
        
    def printStack(self):
        print(self.data)
    
def is_parentheses_matching(expression: str):
    stack = ArrayStack()
    for char in expression:
        if char in ["(", "{", "["]:
            stack.push(char)
        elif char in [")", "}", "]"]:
            if stack.is_empty():
                return False
            if char == ")" and stack.stackTop() == "(":
                stack.pop()
            elif char == "}" and stack.stackTop() == "{":
                stack.pop()
            elif char == "]" and stack.stackTop() == "[":
                stack.pop()
            else:
                return False
    return stack.is_empty()

def copyStack(stack1: ArrayStack(), stack2: ArrayStack()):
    for i in range(stack2.size()): stack2.pop()
    temp = [stack1.pop() for i in range(stack1.size())]
    for i in range(temp.size()):
        value = temp.pop()
        stack1.push(value)
        stack2.push(value)
    
def infixToPostfix(expression: str):
    priority = {}
    priority["*"] = 3
    priority["/"] = 3
    priority["+"] = 2
    priority["-"] = 2
    priority["("] = 1
    opStack = ArrayStack()
    postfix_list = []
    token_list = list(expression)

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfix_list.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and (priority[opStack.stackTop()] >= priority[token]):
                  postfix_list.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfix_list.append(opStack.pop())
    return "".join(postfix_list)