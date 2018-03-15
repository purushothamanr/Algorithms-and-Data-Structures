class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd_sum = 0
        even_sum = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                even_sum = max(even_sum + nums[i], odd_sum)
            else:
                odd_sum = max(odd_sum + nums[i], even_sum)

        return max(odd_sum, even_sum)

s1 = Solution()

print(s1.rob([2,1,1,8,5]))