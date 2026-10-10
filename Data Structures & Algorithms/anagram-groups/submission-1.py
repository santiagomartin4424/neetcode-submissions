class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list) # with defaultdict, get() is not needed

        for string in strs:
            count = [0] * 26  #every it we reset the vect
            
            for char in string:
                count[ord(char) - ord("a")] += 1

            result[tuple(count)].append(string)
            
        return list(result.values()) #we return just the strings, not the keys (which are, tuples of a-z count)

