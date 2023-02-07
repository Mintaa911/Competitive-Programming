class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        strt = 0
        n = len(words)
        prefix = [0]
        group = []
        ans = []
        for i in range(n):
            prefix.append(len(words[i]) + prefix[-1])

        for end in range(1,n+1):
            if (prefix[end] - prefix[strt] + (end-strt-1)) > maxWidth:
                group.append(words[strt:end-1])
                strt = end-1
        if strt <= n:
            group.append(words[strt:])
        
        for j in range(len(group)):
            g = group[j]
            l = len("".join(g))
            even_gap = (maxWidth-l)//(len(g)-1) if len(g) > 1 else (maxWidth-l)
            rm = (maxWidth-l)%(len(g)-1) if len(g) > 1 else (maxWidth-l)
            if j == len(group) -1:
                even_gap = 1
                rm = 0
            lst = []
            for i in range(len(g)):
                lst.append(g[i])
                if len(g) == 1:
                    lst.append(str(rm*" "))
                elif rm > 0:
                    lst.append(str(" "))
                    rm -= 1
                if i < (len(g)-1):
                    lst.append(str(even_gap*" "))
            if j == len(group) - 1:
                l = maxWidth - len("".join(lst))
                lst.append(str(l*" "))

            ans.append("".join(lst))
        
        
        return ans 
