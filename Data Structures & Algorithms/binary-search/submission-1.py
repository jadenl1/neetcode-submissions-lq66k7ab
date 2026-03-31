class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 2 ptr solution
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            print(nums[mid])
            print(nums[lo:hi])
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1

        return -1            