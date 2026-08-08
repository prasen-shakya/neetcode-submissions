class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(visited, path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num in visited:
                    continue
                
                path.append(num)
                visited.add(num)
                dfs(visited,path)
                path.pop()
                visited.remove(num)

        dfs(set(), []) 

        return res