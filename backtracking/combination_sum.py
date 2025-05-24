class Solution(object):
    def combination_sum(self,nums,target):
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
    

if __name__ == "__main__":
    lists = [2,5,6,9]
    sol = Solution()
    print(sol.combination_sum(lists,9))