class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}

        if len(s) != len(t):
            return False

        for c in s:
            smap[c] = smap.get(c, 0) + 1
        
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1

        for key in smap.keys():
            if key not in tmap.keys():
                return False

            if smap[key] != tmap[key]:
                return False
        
        return True