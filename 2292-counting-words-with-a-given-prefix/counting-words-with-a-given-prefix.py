class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        l = len(pref)  # Length of the prefix
        ans = 0  # Counter for words with the prefix
        for word in words:
            if len(word) >= l and word[:l] == pref:  # Check if the word starts with the prefix
                ans += 1
        return ans