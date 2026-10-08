class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_dict = {}

        for i, c in enumerate(s):
            my_dict[c] = my_dict.get(c, 0) + 1   # we register the key:value pairs as char:n_occurrences

        for i, c in enumerate(t):
            # if the character of t wasn't present in s, or the count is 0, not an anagram
            if my_dict.get(c, 0) == 0:
                return False

            my_dict[c] -= 1
        return True
        
















        mod_s = sorted(s)
        mod_t = sorted(t)

        if mod_s == mod_t:
            return True
        else:
            return False




        