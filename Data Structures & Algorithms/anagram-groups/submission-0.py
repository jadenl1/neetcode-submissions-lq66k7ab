class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        allcounts = [] # list of maps
        
        # loop through strs
        for string in strs:
            # we count the strings characters
            countmap = {}
            for c in string:
                countmap[c] = countmap.get(c, 0) + 1
            # ex. countmap: {a:1, c:1, t:1}
            # if countmap is in allcounts already, add string to result @ countmaps_index (mylist.index(elem))
            if countmap in allcounts:
                ind = allcounts.index(countmap)
                result[ind].append(string)
            # else append [string] to result and append countmaps to allcounts
            else:
                result.append([string])
                allcounts.append(countmap)
        
        return result #?

 
                    
