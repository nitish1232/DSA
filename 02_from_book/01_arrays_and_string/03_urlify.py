# Given a string check for spaces and replace spaces with '%20" like in any web URL

def urlify(s: str) -> str:
    return s.replace(" ", "%20")

if __name__ == "__main__":
    s = "I am Nitish Ugru"
    url = urlify(s)
    print(f"URLification of string: {s} is {url}")
