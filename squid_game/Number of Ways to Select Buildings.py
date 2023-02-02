class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = defaultdict(int)
        for c in s:
            if c == '0':
                dp['0'] += 1
                dp['10'] += dp['1']
                dp['010'] += dp['01']
            else:
                dp['1'] += 1
                dp['01'] += dp['0']
                dp['101'] += dp['10']


        return dp['010'] + dp['101']
