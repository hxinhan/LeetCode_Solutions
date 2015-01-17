class Solution:
    def twoSum(self, nums, target):
        s = {}
        # second argument of enumerate indicates the starting index
        for i, num in enumerate(nums, 1):
            i1 = s.get(target-num)
            if i1 != None:
                # i1 should be smaller that i
                return i1, i
            else:
                s[num] = i