class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            print("searching for row")
            print(matrix[lo:hi+1])
            midi = lo + ((hi-lo) // 2)
            mid = matrix[midi]

            if mid[0] > target:
                hi = midi - 1
            elif mid[0] < target:
                #check the next rows first index
                if midi == hi or matrix[midi + 1][0] > target:
                    print(f"found row: {mid}")
                    # then we bin search the row
                    l = 0
                    h = len(mid) - 1
                    while l <= h:
                        m = l + ((h-l) // 2)
                        print(f"row mid: {mid[m]}")
                        if mid[m] == target:
                            return True
                        elif mid[m] < target:
                            l = m + 1
                        elif mid[m] > target:
                            h = m - 1
                # move lo up 
                lo = midi + 1
            else:
                return True
        
        return False
