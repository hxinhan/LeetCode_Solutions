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


'''
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        result = 0
        i = 0
        ptr = 0
        flag = True
        while i < len(s):
            if flag:
                while ptr < len(s):
                    if s[ptr] not in s[i:ptr]:
                        ptr += 1
                    else:
                        result = max(result, ptr-i)
                        flag = False
                        break
            if ptr == len(s):
                break
            if s[i] == s[ptr]:
                flag = True
            i += 1
        return max(result, ptr-i)
'''