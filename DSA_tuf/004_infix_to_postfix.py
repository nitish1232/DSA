# Infix expression is converted postfix expression.
# Operator priority is **(exponent), *, /, +, -.
# Logic:
# - Stack will always have only operators.
# - As and when operand is seen, append it to answer.
# - If it is operator, check if its priority is less than that of stack top.
# -   if yes, keep poping from stack top and append it to answer.
# -   if not, directly push it to stack.
# - If '(' then push it to stack.
# - If ')' then pop from stack until '(' is got and keep appending to answer.
# Complete explanation: youtube.com/watch?v=4pIc9UBHJtk&list=PLgUwDviBIf0pOd5zvVVSzgpo6BaCpHT9c&index=3

def infix_to_postfix(expr):
    st = []
    ans = []
    in_expr = expr.split(" ")
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
    return "".join(ans)

if __name__ == "__main__":
    print(infix_to_postfix("a + b * ( c ^ d - e )"))
