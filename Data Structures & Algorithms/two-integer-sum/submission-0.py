class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fin = []
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if(i == j):
                    continue
                if(nums[i] + nums[j] == target):
                    fin.append(i)
                    fin.append(j)
                    fin.sort()
                    return fin