class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = s.lower()
        rs = ls.replace(" ", "")

        if len(rs) == 0:
            return True

        pl = 0
        pr = len(rs)-1

        while pl != len(rs)-1:
            left = rs[pl]
            right = rs[pr]

            print('left pointer: ', left)
            print('right pointer: ', right)

            if not left.isalnum():
                pl += 1
                continue

            if not right.isalnum():
                pr -= 1
                continue
            
            if left.isalnum() and right.isalnum():
                if left != right:
                    return False
            
            pl += 1
            pr -= 1
        
        return True