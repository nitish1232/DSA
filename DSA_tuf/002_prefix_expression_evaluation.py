# Expression is given in the form of character list.
# Input is a prefix expression:
# ex: 9+6*3 = +9*63
# Logic is scan the expression from right to left:
# If it is an operand push to stack. If it is an operator,
# pop top 2 elements from stack, apply operation and push again to stack

def evaluate(op1, op2, op):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    else:
        return op1 // op2

def evaluate_prefix_expression(expression):
    l = expression.split(" ")
    st = []
    i = len(l)-1
    while i>=0:
        if l[i].isdigit():
            st.append(int(l[i]))
        else:
            op1 = st.pop()
            op2 = st.pop()
            st.append(evaluate(op1, op2, l[i]))
        i -= 1
    return st.pop()


if __name__ == "__main__":
    # print(evaluate_prefix_expression("* + 12 5 3"))
    print(evaluate_prefix_expression("+ 9 * 6 3"))
