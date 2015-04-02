class Solution:
    # @return a boolean
    def isPalindrome(self,x):
        isPalindrome = True
        x = str(x)
        length = len(x)

        if x[0] in "-":
            return False
        for i in xrange(0,length):
            if x[i] != x[length-i-1]:
                isPalindrome = False
        return isPalindrome 
