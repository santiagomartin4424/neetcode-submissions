class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_dict = {}

        for i, c in enumerate(s):
            my_dict[c] = my_dict.get(c, 0) + 1   # we register the key:value pairs as char:n_occurrences

        for i, c in enumerate(t):
            if my_dict.get(c, 0) == 0:      # if this condition is met, it means that the nº of 'a' in the first string, is > than the nº of 'a' in b, thus, they're not anagrams. 
                return False

            my_dict[c] -= 1
        return True
        
















        mod_s = sorted(s)
        mod_t = sorted(t)

        if mod_s == mod_t:
            return True
        else:
            return False




        