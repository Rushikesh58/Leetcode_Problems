class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        https://leetcode.com/problems/subarray-product-less-than-k/description/
        """
        if k <= 1:
            return 0
        prod = 1
        l = 0
        ans = 0
        for r in range(len(nums)):
            prod *= nums[r]
            while prod >= k:
                prod //= nums[l]
                l += 1
            ans += r - l + 1
        return ans