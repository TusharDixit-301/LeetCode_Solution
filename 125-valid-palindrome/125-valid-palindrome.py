class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l=[]
        for i in s:
            if i.isalnum():
                l.append(i)
        s = "".join(l)
        print(s)
        if s == s[::-1]:
            return True
        else:
            return False