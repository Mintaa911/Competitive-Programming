class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        start,end = 0,len(people)-1
        people.sort()
        boat = 0
        
        while start < end:                
            weight_sum = people[start] + people[end]
            
            if weight_sum <= limit:
                boat += 1
                start += 1
                end -= 1
            elif weight_sum > limit:
                end -= 1

        boat = len(people) - boat
        
        return boat
