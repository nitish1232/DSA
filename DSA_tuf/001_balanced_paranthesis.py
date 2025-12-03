# If a list of parenthesis are given check if it is balanced or not
# example ([{}()]) -> this is balanced.
#         ([{}(])) -> not balanced
from sqlalchemy import false


def is_balanced(brackets):
    matching_map = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    open_brackets = "({["
    closed_brackets = ")}]"
    stack = []
    for br in brackets:
        if br in open_brackets:
            stack.append(br)
        if br in closed_brackets:
            top = stack.pop()
            if top != matching_map[br]:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    brackets = input("Give list of brackets")
    if is_balanced(brackets):
        print("Yes, this is balanced.")
    else:
        print("No, this is not balanced.")
