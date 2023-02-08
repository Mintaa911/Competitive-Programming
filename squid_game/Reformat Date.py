class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        lst = []
        date_lst = date.split(" ")
        lst.append(date_lst[2])
        lst.append(month[date_lst[1]])
        lst.append(date_lst[0][:len(date_lst[0])-2])

        if len(lst[-1]) == 1:
            lst[-1] = '0'+lst[-1]
        return "-".join(lst)
        
