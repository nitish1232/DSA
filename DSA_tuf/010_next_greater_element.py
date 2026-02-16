# When stack is sued to store element in some order then it is called, monotonic stack.
# NGE is one such stack.
# Answer stack should have element which is greater in the next right of the corresponding element in original stack.
# Ex: [6, 0, 8, 1, 3]
# Ans: [8, 8, -1, 3, -1]
# Traverse from right to left.
# If there are no element in the stack, add -1 to the ans, and push element to the stack.
# If element is less than stack top, push stack top to the asnwer, and push element to the stack.
# If element is greater than stack top, keep poping stack until an element greater is got, or stack is empty

def get_next_greater_element(elements):
    stack = []
    ans = []
    for i in range(len(elements)-1, -1, -1):
        if not stack:
            ans.append(-1)
            stack.append(elements[i])
        elif elements[i] < stack[-1]:
            ans.append(stack[-1])
            stack.append(elements[i])
        else:
            while stack and elements[i] >= stack[-1]:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(elements[i])
    return ans[::-1]


# Example usage:
if __name__ == "__main__":
    # elements = [6, 0, 8, 1, 3]
    elements = [4,12,5,3,1,2,5,3,1,2,4,6]
    print(get_next_greater_element(elements))  # Output: [8, 8, -1, 3, -1]
