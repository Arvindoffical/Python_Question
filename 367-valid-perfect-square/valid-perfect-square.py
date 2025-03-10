class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        while l<= r:
            m = (l+r)//2
            m_s = m*m
            if num == m_s:
                return True
            elif m_s < num:
                l = m+1
            else:
                r = m-1
        return False