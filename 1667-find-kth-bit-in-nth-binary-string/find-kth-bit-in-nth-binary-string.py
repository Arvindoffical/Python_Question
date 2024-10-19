def inverts(st):
        l=[s for s in st]
        for i in range(len(l)):
            if l[i]=='1':
                l[i]='0'
            elif l[i]=='0':
                l[i]='1'
        return ''.join(l)
class Solution:
    


    def findKthBit(self, n: int, k: int) -> str:
        a=['0']*n
        
        for i in range(1,n):
           a[i] =a[i-1]+ '1' + inverts(a[i-1])[::-1]
            
        b=a[n-1]
        return b[k-1]

        