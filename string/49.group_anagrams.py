from typing import List
import collections

input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


print(group_anagrams(input_data))
