class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()
        def dfs(path, i, total):
            if total == 0:
                res.append(path[:])
                return
            
            if total < 0 or i >= len(candidates):
                return
            
            path.append(candidates[i])
            dfs(path, i + 1, total - candidates[i])

            path.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(path, i + 1, total)
        
        dfs([], 0, target)
        return res