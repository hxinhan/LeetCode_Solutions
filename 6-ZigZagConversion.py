class Solution:
    # @return a string
    def convert(self, s, nRows):

        if len(s)<nRows or nRows==1:
            return s

        zigSize=nRows*2-2 # number of characters in each zig (down-going and up-going combined).
        zigNum=len(s)/zigSize # number of such whole zigs needed.
        hangover=len(s)%zigSize #number of leftover characters in the last incomplete zig
        secHang=hangover-nRows if hangover > nRows else 0 #number of leftover characters in the last incomplete zig that belong to the up-going arm

        result=''
        for i in xrange(nRows):
            for j in xrange(zigNum):
                result+=s[zigSize*j+i]+(s[zigSize*(j+1)-i] if (i!=0 and i!=nRows-1) else '')
            if i < hangover:
                result+=s[zigSize*zigNum+i]
                if i >=nRows-1-secHang and i < nRows-1:
                    result+=s[len(s)-1-secHang+nRows-1-i]
        return result