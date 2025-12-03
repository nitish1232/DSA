# There can be 3 operations done on a string. insert a character, delete a character or replace a character. Given 2
# strings, verify if they are one edit of one another.
# For ex: pale, ple -> True,
#         pale, bale -> True,
#         pale, bake -> False
#         pale, ile -> False

def are_one_away_strings(string1: str, string2: str) -> bool:
    l1 = len(string1)
    l2 = len(string2)
    if abs(l1 - l2) > 1:
        return False
    char_count_dict = {}
    for char in string1:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    for char in string2:
        if char in char_count_dict:
            char_count_dict[char] -= 1
            if char_count_dict[char] == 0:
                del char_count_dict[char]
        else:
            char_count_dict[char] = 1
    print(char_count_dict)
    return len(char_count_dict) <= 2


if __name__ == "__main__":
    string1 = "palle"
    string2 = "pale"
    print(f"Given 2 strings are: {are_one_away_strings(string1, string2)}")
