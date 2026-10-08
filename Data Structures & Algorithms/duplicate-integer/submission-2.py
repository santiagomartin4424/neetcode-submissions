class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for i, n in enumerate(nums):
            if n in dict:
                return True

            dict[n] = dict.get(n, 0) + 1
        return False

