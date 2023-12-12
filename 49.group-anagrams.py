#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letterWord = defaultdict(list)
        for word in strs:
            letterWord[tuple(sorted(word))].append(word)
        return list(letterWord.values())
# @lc code=end
