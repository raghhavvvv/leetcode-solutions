#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0] * (len(gain)+1)
        for i in range(1, len(gain) + 1):
            res[i] = gain[i-1] + res[i-1]
        return max(res)
# @lc code=end

