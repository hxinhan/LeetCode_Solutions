class Solution:
    # @return an integer
    def reverse(self,x):
        revx = int(str(abs(x))[::-1])
        return 0 if revx > math.pow(2,31) else revx * cmp(x,0)
