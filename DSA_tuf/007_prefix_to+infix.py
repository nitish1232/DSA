# Convert prefix expression to infix expression
# Traverse prefix expression from right to left
# - If it is an operand, push it to stack
# - If it is an operator, pop top 2 elements from stack and apply operator in between
#   them(top1 operator top2) and push again to stack

def prefix_to_infix(expr):
    st = []
    in_expr = expr.split(" ")
    for i in range(len(in_expr)-1, -1, -1):
        if in_expr[i].isalnum():
            st.append(in_expr[i])
        else:
            op1 = st.pop()
            op2 = st.pop()
            st.append("(" + op1 + in_expr[i] + op2 + ")")
    return st.pop()


if __name__ == "__main__":
    print(prefix_to_infix("* + 12 5 3"))
    print(prefix_to_infix("+ 9 * 6 3"))
    # print(prefix_to_infix("/ - A B + D E * F"))