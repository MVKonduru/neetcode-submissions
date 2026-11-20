class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = {}
        for i in nums:
            if i in new_dict:
                new_dict[i]+=1
            else:
                new_dict[i]=1
        sorted_nums = sorted(new_dict, key=lambda x:new_dict[x],reverse = True)
        return sorted_nums[:k]
