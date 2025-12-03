# Expression is given in the form of character list.
# Input is a postfix expression:
# ex: 9+6*3 = 963*+
# Logic is scan the expression from left to right:
# If it is an operand push to stack. If it is an operator,
# pop top 2 elements from stack, apply operation and push again to stack

def evaluate(op1, op2, op):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op2 - op1
    elif op == "*":
        return op1 * op2
    else:
        return op2 // op1

def evaluate_postfix_expression(expression):
    l = expression.split(" ")
    st = []
    i = 0
    while i<len(l):
        if l[i].isdigit():
            st.append(int(l[i]))
        else:
            op1 = st.pop()
            op2 = st.pop()
            st.append(evaluate(op1, op2, l[i]))
        i += 1
    return st.pop()


if __name__ == "__main__":
    print(evaluate_postfix_expression("12 5 3 * + 8 -"))
    # print(evaluate_postfix_expression("9 6 3 * +"))
