class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        resultSet = set()
        
        nums.sort()
        print(nums)

        # -4 -1 -1 0 1 2

        i = 0
        while nums[i] <= 0 and i < n-2:
            j = i + 1
            k = n - 1

            while j < k:
                tripletSum = nums[i] + nums[j] + nums[k]
                if tripletSum < 0:
                    j += 1
                elif tripletSum > 0:
                    k -= 1
                else:
                    resultSet.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1

            i += 1

        result = []
        for triplet in resultSet:
            result.append([triplet[0], triplet[1], triplet[2]])

        return result