class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(path, i, total):
            if total == 0:
                res.append(path[:])
                return
            
            if total < 0 or i >= len(nums):
                return
            
            path.append(nums[i])
            dfs(path, i, total - nums[i])
            
            path.pop()
            dfs(path, i + 1, total)

        dfs([],0,target)

        return res