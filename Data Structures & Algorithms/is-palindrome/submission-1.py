class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set, tuple, dict, list
        L, R = 0, len(s) - 1

        while L < R:
            while L < R and not self.alphaNum(s[L]):    # skip non alphaNum
                L += 1
            while R > L and not self.alphaNum(s[R]):    # skip non alphaNum
                R -= 1

            if s[L].lower() != s[R].lower():
                return False
            
            L, R = L+1, R - 1
        return True

        """
        my_str = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]  #reversed
        """


    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))