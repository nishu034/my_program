class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uni = []

        for i in range(len(nums)):
            if nums[i] not in uni:
                uni.append(nums[i])

        for i in range(len(uni)):
            nums[i] = uni[i]

        return len(uni)
