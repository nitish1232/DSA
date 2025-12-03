# Convert postfix expression to infix expression
# Traverse postfix expression from left to right
# - If it is an operand, push it to stack
# - If it is an operator, pop top 2 elements from stack and apply operator in between them and push again to stack

def postfix_to_infix(expr):
    st = []
    in_expr = expr.split(" ")
    for i in range(len(in_expr)):
        if in_expr[i].isalnum():
            st.append(in_expr[i])
        else:
            op1 = st.pop()
            op2 = st.pop()
            st.append("(" + op2 + in_expr[i] + op1 + ")")
    return st.pop()


if __name__ == "__main__":
    # print(postfix_to_infix("a b c d e - ^ * + f +"))
    # print(postfix_to_infix("a b c * + d f + -"))
    print(postfix_to_infix("A B - D E + F * /"))
