class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_max = 0
        curr_max = 0

        for value in nums:
            curr_max, prev_max = max(value+prev_max, curr_max), curr_max

        return curr_max
