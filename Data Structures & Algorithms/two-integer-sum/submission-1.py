class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fin = {}

        for i in range(len(nums)):
            fin[nums[i]] = i


        for j in range(len(nums)):
            if(target - nums[j] in fin and fin[target-nums[j]] !=j):
                return[j,fin[target-nums[j]]]
