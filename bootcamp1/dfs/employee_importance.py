"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        eDict = dict()
        
        for employee in employees:
            eDict[employee.id] = employee
            
        
        def importance(id):
            
            if not eDict[id].subordinates:
                return eDict[id].importance
            
            imp = 0
            for subordinate in eDict[id].subordinates:
                imp += importance(subordinate)
                
            return imp + eDict[id].importance
        
        
        return importance(id)
