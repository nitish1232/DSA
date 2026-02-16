# Get minimum amount in stack at any given point of time.
# You will be ding lot of push, pop operations on the stack.
# You need to return the minimum amount in the stack at any given point of time.
# Scanning entire stack to get minimum amount is not efficient. You need to do it in O(1) time complexity.
# One approach is to store pair values in stack. Value and minimum till that point.

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            min_so_far = self.stack[-1][1]
            self.stack.append((x, min(x, min_so_far)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None


# Example usage:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Returns -3
min_stack.pop()
print(min_stack.top())     # Returns 0
print(min_stack.getMin())  # Returns -2
print(min_stack.stack)      # Returns [(-2, -2), (0, -2)]
