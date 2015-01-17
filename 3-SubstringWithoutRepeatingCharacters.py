#s = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        temp_s=[]
        num=[]
        count=0
        for i in s:
            if i not in temp_s:
                temp_s.append(i)
            else:
                count = len(temp_s)
                num.append(count)
                temp_s = []
        return max(num)