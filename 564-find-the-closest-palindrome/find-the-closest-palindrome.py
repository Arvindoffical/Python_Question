class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n)%2==0:
            half = n[:len(n)//2]
            flag = 0
        else:
            half = n[:1+ len(n)//2]
            flag= 1
        def build_p(half):
            if flag==0:
                tail1 = half[::-1]
                tail2 = str(int(half)-1)[::-1]
                tail3 = str(int(half)+1)[::-1]
                a = half+tail1
                b = str(int(half)-1)+tail2
                c = str(int(half)+1)+tail3
            else:
                tail1 = half[::-1]
                tail2 = str(int(half)-1)[::-1]
                tail3 = str(int(half)+1)[::-1]
                a = half+tail1[1:]
                b = str(int(half)-1)+tail2[1:]
                c = str(int(half)+1)+tail3[1:]
            # The a,b,c should be the most closed candidate to N except edge case
            return [int(a),int(b),int(c)]
        candidate = build_p(half)
        if n[0]=='1' and len(n)>1:
            candidate.append(int("9"*(len(n)-1)))
        if n[0]=="9":
            candidate.append(10**len(n)+1)
        if int(n) in candidate:
            candidate.remove(int(n))
        print(candidate)
        diff = [abs(c-int(n)) for c in candidate]
        min_diff = min(diff)
        res = []
        for i,d in enumerate(diff):
            if d==min_diff:
                if d!=0:
                    res.append(candidate[i])
        return str(min(res))