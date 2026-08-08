class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def dfs(i, total, path):
            if total == target:
                res.append(path[:])
                return
            
            if i >= len(candidates) or total > target:
                return
            
            path.append(candidates[i])
            dfs(i + 1, total + candidates[i], path)
            path.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            
            dfs(i + 1, total, path)
    
        dfs(0, 0, [])
        return res