class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        x=int("".join(map(str,digits)))

        if x!=0:
            x=x+1
        else:
            x=1

        y=list(map(int,str(x)))
        
        return y
