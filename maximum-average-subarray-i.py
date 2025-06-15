class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_s = max_s = sum(nums[:k])
        for i in range(len(nums) - k):
            curr_s += nums[i + k] - nums[i]
            max_s = max(max_s, curr_s)
        return float(max_s) / k  # Ensure float division
