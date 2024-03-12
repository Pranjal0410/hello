class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.dfs(nums, target, 4, [])

        return self.res


    def dfs(self, nums, target, k, curr):
        if k == 0 and target == 0:
            self.res.append(curr[:])
            return

        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                curr.append(nums[i])
                self.dfs(nums[i + 1:], target - nums[i], k - 1, curr)
                curr.pop()