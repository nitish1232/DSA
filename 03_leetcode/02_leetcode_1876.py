def substring(s:str) -> int:
    if len(s) < 3:
        return 0
    if len(s) == 3 and len(s) != len(set(s)):
        return 0
    count = 0
    for i in range(len(s)-2):
        if len(s[i:i+3]) == len(set(s[i:i+3])):
            count += 1
    return count

# length function, creation of set, slicing will take more memory and time.
# Hence, always try to use primitive data structures.
# Above function took 3ms in leetcode.
# In each window of size 3, compare each characters one by one directly.
# Below solution took almost 0ms in leetcode.
def substring_faster(s:str) -> int:
    count = 0
    for i in range(len(s)-2):
        a = s[i]
        b = s[i+1]
        c = s[i+2]
        if a != b and b != c and a != c:
            count += 1
    return count

print(substring("xyzzaz"))
print(substring("aababcabc"))
print(substring("abc"))
print(substring("ab"))
print(substring("abb"))


print(substring_faster("xyzzaz"))
print(substring_faster("aababcabc"))
print(substring_faster("abc"))
print(substring_faster("ab"))
print(substring_faster("abb"))
