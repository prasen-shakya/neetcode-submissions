class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        count_arr = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for num, freq in freq_map.items():
            count_arr[freq].append(num)
        
        res = []

        for i in range(len(count_arr) - 1, 0, -1):
            if count_arr[i] != []:
                for val in count_arr[i]:
                    res.append(val)
                    k -= 1

                    if k == 0:
                        return res