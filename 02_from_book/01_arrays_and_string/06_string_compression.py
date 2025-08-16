# Compress string based on number of times a character has occurred. For ex: aaabbcddddaaa is compressed to
#  a3b2c1d4a3. If length of compressed string is same as that of given string, then return given string.

def get_compressed_string(s: str) -> str:
    count = 1
    compressed_string = ""
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_string += s[i-1] + str(count)
            count = 1
    compressed_string += s[-1] + str(count)
    if len(compressed_string) >= len(s):
        return s
    return compressed_string

if __name__ == "__main__":
    string = "aaabbcddddaaa"
    print(get_compressed_string(string))
