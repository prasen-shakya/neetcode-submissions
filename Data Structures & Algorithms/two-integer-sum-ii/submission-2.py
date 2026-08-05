class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            left_number = numbers[left_pointer]
            right_number = numbers[right_pointer]

            current_sum = left_number + right_number

            if current_sum > target:
                right_pointer -= 1
            elif current_sum < target:
                left_pointer += 1
            else:
                return [left_pointer + 1, right_pointer + 1]