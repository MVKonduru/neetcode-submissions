class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        characters_nested = [list(s) for s in strs]
        print(characters_nested)
        prefix = []
        for i in zip(*characters_nested):
            if len(set(i)) == 1:
                prefix.append(i[0])
            else:
                break
        result = "".join(prefix)
        return result




        