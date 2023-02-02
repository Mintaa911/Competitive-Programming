class Solution:
    def numberToWords(self, num: int) -> str:
        num_dict = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',
                    10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',
                    17:'Seventeen',18:'Eighteen',19:'Nineteen',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',
                    60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}
        num = str(num)
        n = len(num)
        q = deque([])
        for i in range(n-1,-1,-1):
            dig = (n-i)
       
            if dig == 4:
                if q[-1] == 'Hundred':
                    q.pop()
                q.append('Thousand')
                if num[i] != '0':
                    val = num_dict[int(num[i])]
                    q.append(val)
            elif dig == 7:
                while q and q[-1] in ['Hundred','Thousand']:
                    q.pop()
                q.append('Million')
                if num[i] != '0':
                    val = num_dict[int(num[i])]
                    q.append(val)
            elif dig == 10:
                while q and q[-1] in ['Hundred','Million']:
                    q.pop()
                  
                q.append('Billion')
                if num[i] != '0':
                    val = num_dict[int(num[i])]
                    q.append(val)
            elif (dig%3) == 2 and num[i] == '1':
                if num[i+1] != '0':
                    q.pop()
                val = num_dict[int(num[i:i+2])]
                q.append(val)
            elif (dig%3) == 2:
                if num[i] != '0':
                    val = num_dict[int(num[i]+'0')]
                    q.append(val)
            elif (dig % 3) == 0:
                q.append('Hundred')
                if num[i] != '0':
                    val = num_dict[int(num[i])]
                    q.append(val)
            else:
                if num[i] != '0':   
                    val = num_dict[int(num[i])]
                    q.append(val)
        if num == '0':
            q = ["Zero"]
        return " ".join(reversed(q))

