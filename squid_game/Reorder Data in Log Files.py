class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig = []
        lett = []
        ans = []
        for log in logs:
            if log[-1].isdigit():
                dig.append(log)
            else:
                lett.append(log)

        let_dict = defaultdict(list)
        for lt in lett:
            identifier = " ".join(lt.split(" ")[1:])
            let_dict[identifier].append(lt)
        
        lst = []
        for ky,val in let_dict.items():
            for lt in val:
                lst.append((ky,lt.split(" ")[0],lt))
        lst.sort()
        for _,_,log in lst:
            ans.append(log)
        ans.extend(dig)
        return ans
        
