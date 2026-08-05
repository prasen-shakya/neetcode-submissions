class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        freq_array = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        print(freq)
        print(freq_array)
        for num, count in freq.items():
            freq_array[count].append(num)

        output = []
        for i in range(len(freq_array) - 1, 0, -1):
            if k == 0:
                break
            if freq_array[i]:
                for n in freq_array[i]:
                    output.append(n)

                    k -= 1
            

        return output