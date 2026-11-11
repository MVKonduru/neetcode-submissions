# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         sorted_strs = ["".join(sorted(word)) for word in strs]
#         result = []
#         visited = set()
#         print(sorted_strs)
#         for i in range(len(sorted_strs)):
#             if i in visited:
#                 continue
#             group = [strs[i]]
#             visited.add(i)
#             for j in range(i+1, len(sorted_strs)):
#                 if sorted_strs[i] == sorted_strs[j]:
#                     group.append(strs[j])
#                     visited.add(j)
#             result.append(group)
#         return result

                    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            sorted_strs = "".join(sorted(word))
            if sorted_strs not in result:
                result[sorted_strs] = []
            result[sorted_strs].append(word)
        return list(result.values())