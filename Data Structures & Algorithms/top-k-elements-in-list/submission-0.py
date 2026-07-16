class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        temp = dict()
        count = 1
        for i in range(len(nums) - 1):
            if(nums[i] == nums[i+1]):
                count+=1
            else:
                temp[nums[i]] = count
                count = 1
        temp[nums[len(nums) - 1]] = count
        print(temp)
        fin = []
        for j in range(k):
            val = max(temp, key=temp.get)
            fin.append(val)
            temp.pop(val)

        return fin
