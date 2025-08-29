example_str1 = "YazaAaabyyYyyyzzzZz"
example_str2 = "bB"
# print(chr(ord('A') - 32))


def longestNiceSubstringBruteForce(s: str) -> str:
    ans = ""
    for i in range(len(s)):
        for ii in range(i + 1, len(s) + 1):
            if all(s[k].swapcase() in s[i:ii] for k in range(i, ii)):
                ans = max(ans, s[i:ii], key=len)
    return ans

def longestNiceSubstringOptimized(s: str) -> str:
    if not s: return ""  # boundary condition
    ss = set(s)
    for i, c in enumerate(s):
        if c.swapcase() not in ss:
            s0 = longestNiceSubstringOptimized(s[:i])
            s1 = longestNiceSubstringOptimized(s[i + 1:])
            return max(s0, s1, key=len)
    return s

def testing(s):
    n = len(s)
    i = 0
    while i < n - 1:
        if s[i] != s[i + 1] and s[i].lower() == s[i + 1].lower():
            s = s[:i] + s[i + 2:]
            n -= 2
            i = max(i - 1, 0)
        else:
            i += 1
    return s

print(longestNiceSubstringBruteForce(example_str1))
print(longestNiceSubstringOptimized(example_str2))
print(longestNiceSubstringBruteForce(example_str1))
print(longestNiceSubstringOptimized(example_str2))
print(testing(example_str1))
print(testing(example_str2))
