class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for  i in range(2,n):
            a=n//i
            b=n-a
            c=str(a)+str(b)
            d=a+b
            if d==n and '0' not in c:
                return [a,b]
        
