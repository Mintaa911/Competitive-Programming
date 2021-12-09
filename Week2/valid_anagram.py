def isAnagram(s,t):
        if len(s) != len(t):
            return False
        str1 = [y for y in t]
        for c in s:
            j = 0
            while str1 and j < len(str1):
                if c == str1[j]:
                    str1.pop(j) 
                    break
                j += 1
        if str1:
            return False
        return True
