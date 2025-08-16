# 2 strings are said to be anagrams if re-arrangement of characters of one string will give the other.

def check_anagram_with_dictionary(s1: str, s2: str) -> bool:
    characters_dict = {}
    for char in s1:
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    for char in s2:
        if char in characters_dict:
            characters_dict[char] -= 1
        if characters_dict[char] == 0:
            del characters_dict[char]
    if characters_dict:
        return False
    else:
        return True

def check_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    s1 = "abcdef"
    s2 = "cbafd"
    print(f"String 1: {s1}, String 2: {s2} are ", end="")
    ans1 = check_anagram_with_dictionary(s1, s2)
    ans2 = check_anagram(s1, s2)
    if ans1 and ans2:
        print("anagrams")
    else:
        print("not anagrams")
