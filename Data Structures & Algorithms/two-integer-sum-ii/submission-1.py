class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            current_sum = numbers[L] + numbers[R]

            if current_sum == target:
                return [L + 1, R + 1]
            elif current_sum < target:
                L += 1
            else:
                R -= 1
            
            




        my_dict = {}

        for i, n in enumerate(numbers):
            if (target - n) in my_dict:
                return [my_dict[target - n] +1, i +1]

            my_dict[n] = i   # In the dict I'll save the number as KEY, and the index as VALUE.
 