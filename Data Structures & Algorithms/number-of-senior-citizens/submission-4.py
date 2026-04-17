class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        numOldPeople = 0
        for serializedSttring in details:
            if int(serializedSttring[11:13]) > 60:
                numOldPeople += 1
        
        return numOldPeople