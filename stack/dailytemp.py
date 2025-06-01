from typing import *
class Solution():
    def dailytemp(self,lil: List[int]):
        stack = []
        res = [0] * len(lil)


        for i , t in enumerate(lil):
            while stack and t>stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t,i))
        return res

if __name__ == '__main__' :
    sol = Solution()
    lil = [73,74,75,71,69,72,76,73]
    print(sol.dailytemp(lil))
