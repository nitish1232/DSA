# Problem: Check if a string has all unique characters or not. Try to come up with
# time and space optimized code

def check_string_brute_force(s: str) -> bool:
    """
    This approach uses extra dictionary space. But time complexity is O(n)
    """
    count_dict = {}
    for i in s:
        if i in count_dict:
            return False
        else:
            count_dict[i] = 0
    return True

def check_string_with_set(s: str) -> bool:
    """
    This approach takes extra space for set.
    """
    return len(set(s)) == len(s)

# def check_string_by_sorting(s: str) -> bool:
#     """
#     This approach takes O(n*log n) time because of sort methos
#     """
#     sorted_s = sorted(s)
#     print(f"Sorted s is {sorted_s}")
#     for i in range(1, len(sorted_s)):
#         print(f"Comparing {sorted_s[i]} to {sorted_s[i - 1]}")
#         print(f"types are {type(sorted_s[i])} and {type(sorted_s[i - 1])}")
#         if s[i] is s[i-1]:
#             print(f"{i} is equal to {s[i]}")
#             return False
#     return True


if __name__ == "__main__":
    str1 = "abcdef"
    str2 = "abcdafj"
    for s in [str1, str2]:
        if not check_string_with_set(s):
            print(f"Given string {s} has duplicate characters")
        else:
            print(f"Given string {s} has all unique characters")
