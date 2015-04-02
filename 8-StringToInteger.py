class Solution:
    # @return an integer
    def atoi(self,str):
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+\D*',str)

        try:
            result = int(''.join(str))
            INT_MAX = 2147483647
            INT_MIN = -2147483648
            if result > INT_MAX:
                return INT_MAX
            elif result < INT_MIN:
                return INT_MIN
            else:
                return result
        except:
            return 0
