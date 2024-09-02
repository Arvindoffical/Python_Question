class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n=len(chalk)
        s=sum(chalk)
        rm=k%s
        for i in range(1,n):
            chalk[i]=chalk[i-1]+chalk[i]
        res=bisect.bisect(chalk,rm)
       
        return res