class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length_nums = len(nums)
        new_list = [i for i in nums if i!=val]
        k = len(new_list)
        nums[:] = new_list + ['_']*(length_nums - k)
        print("k =",k,",", "nums =", nums[:])
        return k