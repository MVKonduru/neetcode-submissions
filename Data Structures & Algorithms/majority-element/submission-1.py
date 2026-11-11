class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        print(n)
        counts = {}
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i] = 1
            if counts[i]>n/2:
                print(i)
                return i

        