# Given a string, check if it is a permutation of a palindrome
# Ex: tact coa
# Palindrome of string:  taco cat

def check_palindrome_permutation(s: str) -> bool:
    char_dict = {}
    for char in s:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    even_count = 0
    odd_count = 0
    for key,val in char_dict.items():
        if val % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if odd_count > 1:
        return False
    return True


if __name__ == "__main__":
    # string = "abcbacabda"
    string = "abcbacabdab"
    print(check_palindrome_permutation(string))
