class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def isconsec(self,nums):
            if nums!=sorted(nums):
                return False
            for i in range(len(nums)-1):
                if nums[i]+1!=nums[i+1]:
                    return False
            return True
        z=[]
        for i in range(len(nums)-k+1):
            x=nums[i:i+k]
            if isconsec(self,x):
                z.append(max(x))

            else:
                z.append(-1)
        return z