# Get minimum amount in stack at any given point of time.
# You will be ding lot of push, pop operations on the stack.
# You need to return the minimum amount in the stack at any given point of time.
# Scanning entire stack to get minimum amount is not efficient. You need to do it in O(1) time complexity.
# Mathematical approach is:
# - while pushing if element is smaller than current minimum the push derived value on to the stack:
#   derived=2*val-cur_min
# while poping if stack top is smaller than the current minimum, then that means it is a derived value:
#   cur_min=2*cur_min-derived, then pop the stack top

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = 0

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.min = x
        elif x < self.min:
            self.stack.append(2 * x - self.min)
            self.min = x
        else:
            self.stack.append(x)

    def pop(self) -> None:
        if not self.stack:
            return None
        top = self.stack.pop()
        if top < self.min:
            old_min = 2*self.min - top
            self.min = old_min

    def top(self) -> int:
        if not self.stack:
            return None
        top = self.stack[-1]
        if top < self.min:
            return self.min
        return top

    def getMin(self) -> int:
        return self.min


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
