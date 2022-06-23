from typing import List

input = ["h", "e", "l", "l", "o"]


def reverse_string1(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_string2(s: List[str]) -> None:
    s.reverse()
