#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ''
        for c in s:
            if c.isalnum():
                news += c.lower()
        return news == news[::-1]
    
        
# @lc code=end

