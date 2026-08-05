class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        count = [[] for i in range(len(nums) + 1)]

        output = []

        for i in nums:
            freq[i] += 1
        
        for i in freq:
            count[freq[i]].append(i)

        for i in range(len(count) - 1, 0, -1):
            for j in count[i]:
                output.append(j)
                if (len(output) == k):
                    return output