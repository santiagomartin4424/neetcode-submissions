class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        R, L = 0, 0
        my_dict = {}

        for i, n in enumerate(numbers):
            if (target - n) in my_dict:
                return [my_dict[target - n] +1, i +1]

            my_dict[n] = i   # In the dict I'll save the number as KEY, and the index as VALUE.
