class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        count = {}
        #count nums
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        #count ex. {1: 1, 2: 2, 3: 3}

        # find the max value, append key, remove pair, repeat
        for i in range(k):
            maxKey = -1
            maximum = -1
            # loop through count
            for key in count.keys():
                if count[key] > maximum:
                    maximum = count[key]
                    maxKey = key
            result.append(maxKey)
            del count[maxKey]
                
        return result