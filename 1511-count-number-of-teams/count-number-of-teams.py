# class Solution:
#     def numTeams(self, rating: List[int]) -> int:
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        greater_left, greater_right = [0] * n, [0] * n

        def merge(left, right):
            if left >= right: return [left]

            mid = left + right >> 1
            l_vals = merge(left, mid)
            r_vals = merge(mid + 1, right)
            merged = []
            p_l, p_r = 0, 0

            while p_l < len(l_vals) or p_r < len(r_vals):
                if p_r == len(r_vals) or (p_l < len(l_vals) and rating[l_vals[p_l]] < rating[r_vals[p_r]]):
                    greater_right[l_vals[p_l]] += p_r
                    merged.append(l_vals[p_l])
                    p_l += 1
                else:
                    greater_left[r_vals[p_r]] += p_l
                    merged.append(r_vals[p_r])
                    p_r += 1
            
            return merged
        
        merge(0, n - 1)

        total = 0
        for i in range(n):
            lower_left, lower_right = i - greater_left[i], n - 1 - i - greater_right[i]
            total += greater_left[i] * lower_right + lower_left * greater_right[i]
        
        return total        