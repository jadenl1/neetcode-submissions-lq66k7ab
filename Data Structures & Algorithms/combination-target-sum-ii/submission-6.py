class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        state = []
        
        candidates.sort()

        def dfs(i, currSum):
            if currSum == target:
                result.append(state.copy())
                return
            
            for j in range(i, len(candidates)):
                num = candidates[j]

                if j > i and num == candidates[j - 1]:
                    continue

                if currSum + num > target:
                    return

                state.append(num)
                dfs(j + 1, currSum + num)
                state.pop()

        dfs(0, 0)

        return result