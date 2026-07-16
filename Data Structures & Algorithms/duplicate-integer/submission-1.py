class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tst = set()
        for num in nums:
            if num in tst:
                return True
            else:
                tst.add(num)
        return False