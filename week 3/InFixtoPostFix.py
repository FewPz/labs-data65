"IG: few.pz"
def infix_to_postfix(expression):
    """ Infix to postfix conversion using the Shunting-yard algorithm. """
    operator_precedence = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }
    operator_stack = []
    postfix_expression = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or token.isalpha():
            postfix_expression.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            top_token = operator_stack.pop()
            while top_token != "(":
                postfix_expression.append(top_token)
                top_token = operator_stack.pop()
        else:
            while operator_stack and operator_precedence[operator_stack[-1]] >= operator_precedence[token]:
                postfix_expression.append(operator_stack.pop())
            operator_stack.append(token)

    while operator_stack:
        postfix_expression.append(operator_stack.pop())

    return " ".join(postfix_expression)

def main():
    """ Main function """
    print(infix_to_postfix("A + B * C"))
main()