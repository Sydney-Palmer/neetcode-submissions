class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTableForS = {}
        hashTableForT = {}
        if len(s) != len(t):
            return False
        for char in s:
            hashTableForS[char] = hashTableForS.get(char, 0) + 1
        for char in t:
            hashTableForT[char] = hashTableForT.get(char, 0) + 1

        if hashTableForS == hashTableForT:
            return True
        else:
            return False

        
        
        
            