class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)
        candidates.sort()

        def dfs(i, curSum):
            if curSum == target:
                res.append(sol[:])
                return
            if curSum>target:
                return

            for j in range(i, n):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                
                sol.append(candidates[j])
                dfs(j+1, candidates[j]+curSum)
                sol.pop()

        dfs(0,0)
        return res
            
            