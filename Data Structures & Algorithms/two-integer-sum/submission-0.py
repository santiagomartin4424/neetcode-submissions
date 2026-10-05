class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        vect = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # it is important to start from i, until len(nums)
            
                if (nums[i] + nums[j]) == target:
                    vect = [i, j]

        return vect
        """
        # I'm gonna start saving each num in the hashmap (as the key, with the index of the number as value), and then, check if the difference
        # is in the hashmap. If no, continue. If yes, we have found our pair of numbers.
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashmap:
                return [hashmap[diff], i]
            
            hashmap[nums[i]] = i # for the dict, i'll say the KEY is the given number, and the VALUE the index of this number
        return
