class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/?envType=problem-list-v2&envId=sliding-window
        """
        l = 0
        arr = [0] * 26
        res = 0
        for r in range(len(s)):
            arr[ord(s[r]) - ord('a')] +=1

            while arr[ord(s[r]) - ord('a')] == 3:
                arr[ord(s[l]) - ord('a')] -=1
                l+=1
            if max(arr) <= 2:
                res = max(res, r-l+1)
                print(r,l)
        return res