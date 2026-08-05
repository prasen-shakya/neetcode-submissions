class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_list = {}
        
        buckets = [[] for _ in range(len(nums) + 1)]

        output = []

        for num in nums:
            if num in frequency_list:
                frequency_list[num] += 1
            else:
                frequency_list[num] = 1
        
        for num in frequency_list:
            count = frequency_list[num]
            buckets[count].append(num)

        for i in range(len(buckets) - 1, -1, -1):
            while k > 0 and len(buckets[i]) != 0:
                output.append(buckets[i].pop())
                k -= 1
        
        return output
        
        

        