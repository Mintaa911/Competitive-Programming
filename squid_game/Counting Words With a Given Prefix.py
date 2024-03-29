class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        n = len(pref)
        for word in words:
            if word[:n] == pref:
                cnt += 1

        return cnt
