import sys
from os import path

class Solution:
    def solve(self, nums: list[int], k: int) -> list[int]:
        return 10000


if __name__ == "__main__":
    # FOR ONLINE JUDGE
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    else:
        sys.stdin = open("input.txt", "r+")
        sys.stdout = open("output.txt","w")
    #ENDS HERE

    arr = eval(input())
    k = int(input())
    sol = Solution()
    ans = sol.solve(arr, k)
    print(ans)


        