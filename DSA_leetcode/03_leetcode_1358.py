# This is not the complete final solution for the given problem, but a part of the solution.


def generate_substrings(s:str) -> list:
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.append(s[i:j])
    return substrings

def generate_substrings_with_yield(s:str):
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            yield s[i:j]

def generate_substrings_of_length_k(s:str, k:int) -> list:
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            if j - i == k:
                substrings.append(s[i:j])
    return substrings

def generate_substrings_of_length_minimum_k(s:str, k:int) -> list:
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            if j - i >= k:
                substrings.append(s[i:j])
    return substrings

def counter(s:str) -> int:
    count = 0
    substrings = generate_substrings_of_length_minimum_k(s,3)
    for substr in substrings:
        if "a" in substr and "b" in substr and "c" in substr:
            count += 1
    return count




# print(generate_substrings_with_yield("abcdefghi"))
# print(list(generate_substrings_with_yield("abcdefghi")))
# print(generate_substrings_of_length_minimum_k("abcdefghi", 3))


print(counter("abc"))
print(counter("aaacb"))
