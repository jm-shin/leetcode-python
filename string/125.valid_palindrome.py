import re


def is_palindrome1(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    # 펠린드롬 여부
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


def is_palindrome2(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]


print(is_palindrome1('A man, a plan, a canal: Panama'))
print(is_palindrome2('race a car'))
