from typing import List
import re
import collections

input_paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
input_banned = ["hit"]


def most_common_word(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split()
             if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


print(most_common_word(input_paragraph, input_banned))
