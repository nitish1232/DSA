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

print(substring("xyzzaz"))
print(substring("aababcabc"))
print(substring("abc"))
print(substring("ab"))
print(substring("abb"))
