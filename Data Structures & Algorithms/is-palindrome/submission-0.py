class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        alpha ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for x in s:
            if x in alpha:
                s_new += x
        s_new = s_new.lower()
        n = len(s_new)
        i = 0
        j = n-1
        while i < j:
            if s_new[i] != s_new[j]:
                return False
            i+=1
            j-=1
        return True