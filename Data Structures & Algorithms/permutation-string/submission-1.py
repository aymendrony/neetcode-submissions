class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        map1 = {}
        
        if len(s2) < len(s1):
            return False
        for x in alphabet:
            map1[x] = s1.count(x)
        k = len(s1)
        i = 0 
        j = k
        while j<len(s2)+1:
            map_window = {}
            for x in alphabet:
                map_window[x] = s2[i:j].count(x)
            if map_window == map1:
                return True 
            i+=1
            j+=1
        return False
