class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=True
        if dividend==-2147483648 and divisor==-1:
            return 2147483647
        if dividend<0 and divisor<0:
            sign=True
        elif dividend<0 or divisor<0:
            sign=False
        dividend=abs(dividend)
        divisor=abs(divisor)
        res=0
        while dividend>divisor:
            pow_x=1
            temp=divisor
            while dividend>(temp<<1):
                temp<<=1
                pow_x<<=1
            dividend-=temp
            res+=pow_x
        if dividend==divisor:
            res+=1
        if sign==True:
            return res
        else:
            return -res
            