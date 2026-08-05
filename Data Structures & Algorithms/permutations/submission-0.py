class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, path):
            if len(path) == len(nums):
                res.append(path[:])
                return
                
            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs(i + 1, path)
                    path.pop()

        dfs(0, [])
        return res