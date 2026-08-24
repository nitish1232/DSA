# Finding the previous smaller element for every element in a list
# Ex: [6, 0, 8, 1, 3]
# Ans: [-1, -1, 0, 0, 1]
# Traverse from left to right.
# If stack is empty, add -1 to the ans, and push element to the stack.
# If element is greater than stack top, push stack top to the asnwer, and push element to the stack.

def get_previous_smaller_element(elements):
    stack = []
    ans = []
    for i in range(len(elements)):
        if not stack:
            ans.append(-1)
            stack.append(elements[i])
        elif elements[i] > stack[-1]:
            ans.append(stack[-1])
            stack.append(elements[i])
        else:
            while stack and elements[i] <= stack[-1]:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(elements[i])
    return ans


if __name__ == "__main__":
    # elements = [6, 0, 8, 1, 3]
    elements = [4,12,5,3,1,2,5,3,1,2,4,6]
    print(get_previous_smaller_element(elements))  # Output: [-1, -1, 0, 0, 1]
