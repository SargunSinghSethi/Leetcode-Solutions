class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x % 10 == 0 and x != 0:
            return False
        res = 0
        n1 = x
        while x > res:
            res = res * 10 + n1 % 10
            n1 //= 10
        return res == x
        
        
s1 = Solution()
x = 10
print(s1.isPalindrome(x))

# ANSWER = FALSE
