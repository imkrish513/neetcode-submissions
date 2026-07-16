class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tst = []
        for num in nums:
            if num in tst:
                return True
            else:
                tst.append(num)
        return False