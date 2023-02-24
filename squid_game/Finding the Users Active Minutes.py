class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UAMs = collections.defaultdict(set)
        ans = [0] * k
        for ID, time in logs:
            UAMs[ID].add(time)
        for UAM in UAMs.values():
            ans[len(UAM)-1] += 1
        return ans
