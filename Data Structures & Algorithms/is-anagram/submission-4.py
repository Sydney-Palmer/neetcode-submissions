from collections import Counter
# counter function tracks the frequency of element in collction
# this works because the order of the chars don't matter only the frequency
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if Counter(s) != Counter(t):
            return False
        else: 
            return True

        
        
        
            