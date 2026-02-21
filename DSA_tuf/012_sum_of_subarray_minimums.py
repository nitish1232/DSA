# Find sum of minimums of all subarrays of a given array.
# Example 1: [3, 1, 2, 4]
# All possible subarrays are and their minimums are:
# [3] -> 3
# [3, 1] -> 1
# [3, 1, 2] -> 1
# [3, 1, 2, 4] -> 1
# [1] -> 1
# [1, 2] -> 1
# [1, 2, 4] -> 1
# [2] -> 2
# [2, 4] -> 2
# [4] -> 4
# Sum of these minimums is 3 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 2 + 4 = 17
# For each element find how many times that has contributed to the minimum in the subarray.
# 3 has contributed to the minimum in 1 subarray, 1 has contributed to the minimum in 6 subarrays,
# 2 has contributed to the minimum in 2 subarrays, and 4 has contributed to the minimum in 1 subarray.
# So the answer is 3*1 + 1*6 + 2*2 + 4*1 = 17
# To find the sum of minimums of all subarrays, we can use the concept of "Next Smaller Element" and
# "Previous Smaller or Equal Element". For each element in the array, we can determine how many subarrays it is the
# minimum for by finding the distance to the next smaller element on the right and the previous smaller or equal
# element on the left. The contribution of each element to the total sum can be calculated as:
# element_value * (distance_to_previous_smaller_or_equal) * (distance_to_next_smaller)
# Link: https://www.youtube.com/watch?v=v0e8p9JCgRc&list=PLgUwDviBIf0pOd5zvVVSzgpo6BaCpHT9c&index=9
def get_next_smaller_element_indices(elements):
    stack = []
    n = len(elements)
    ans = [n] * n
    for i in range(n-1, -1, -1):
        while stack and elements[stack[-1]] >= elements[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans


def get_previous_smaller_or_equal_element_indices(elements):
    ans = []
    stack = []
    for i in range(len(elements)):
        while stack and elements[stack[-1]] > elements[i]:
            stack.pop()
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(i)
    return ans


def get_sum_of_subarray_minimums(elements):
    mod = 10**9 + 7
    next_smaller_indices = get_next_smaller_element_indices(elements)
    previous_smaller_or_equal_indices = get_previous_smaller_or_equal_element_indices(elements)

    total_sum = 0
    for i in range(len(elements)):
        left_count = i - previous_smaller_or_equal_indices[i]
        right_count = next_smaller_indices[i] - i
        total_sum += elements[i] * left_count * right_count
        total_sum %= mod
    return total_sum


if __name__ == "__main__":
    # elements = [4,12,5,3,1,2,5,3,1,2,4,6]
    # elements = [1, 1]
    # elements = [1, 4, 6, 7, 3, 7, 8, 1]
    elements = [3, 1, 2, 4]
    # print(get_next_smaller_element_indices(elements))  # Output: [-1, -1, 0, 0, 1]
    # print(get_previous_smaller_or_equal_element_indices(elements))  # Output: [-1, -1, 0, 0, 1]
    print(get_sum_of_subarray_minimums(elements))  # Output: 17
