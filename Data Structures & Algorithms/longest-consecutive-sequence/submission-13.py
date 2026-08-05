class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        hash_set = set()

        longest = 0

        for num in nums:
            hash_set.add(num)

        for num in hash_set:
            prev_num = num - 1

            if prev_num not in hash_set:
                next_num = num + 1
                cur_longest = 1

                while next_num in hash_set:
                    cur_longest += 1
                    next_num += 1
                
                longest = max(cur_longest, longest)

        return longest