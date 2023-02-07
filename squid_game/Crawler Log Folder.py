class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dict = defaultdict(lambda: 1)
        dict[".."] = -1
        dict["."] = 0
        cnt = 0
        for log in logs:
            s = log.split('/')
            if cnt == 0 and dict[s[0]] == -1:
                continue
            cnt += dict[s[0]]

        return cnt
            
