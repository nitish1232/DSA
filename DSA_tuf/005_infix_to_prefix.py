# Infix expression is converted prefix expression.
# Operator priority is **(exponent), *, /, +, -.
# Logic:
# - Reverse the given expression
# - Swap "(" to ")" and vice versa
# - Run same as infix to postfix logic and get postfix expression
# - Reverse the postfix expression to get prefix expression.
# Complete explanation: youtube.com/watch?v=4pIc9UBHJtk&list=PLgUwDviBIf0pOd5zvVVSzgpo6BaCpHT9c&index=3

def infix_to_prefix(expr):
    in_expr = expr.split(" ")
    in_expr.reverse()
    for i in range(len(in_expr)):
        if in_expr[i] == "(":
            in_expr[i] = ")"
        elif in_expr[i] == ")":
            in_expr[i] = "("
    st = []
    ans = []
    priority_map ={
        "^": 3,
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
        "(": 0
    }
    i = 0
    while i<len(in_expr):
        if in_expr[i] == "(":
            st.append(in_expr[i])
        elif in_expr[i].isalnum():
            ans.append(in_expr[i])
        elif in_expr[i] == ")":
            while st and st[-1] != "(":
                ans.append(st.pop())
            st.pop()
        else:
            while st and priority_map[in_expr[i]] < priority_map[st[-1]]:
                ans.append(st.pop())
            st.append(in_expr[i])
        i+=1
    while st:
        ans.append(st.pop())
    ans.reverse()
    return "".join(ans)


if __name__ == "__main__":
    print(infix_to_prefix("( a + b ) * c - d + f"))