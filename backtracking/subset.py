class Solutions():
    def subset(self, l1):
        res = []
        subset = []
        def dfs(i):
            if i >= len(l1):
                res.append(subset.copy())
                return
            subset.append(l1[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
    
if __name__ == "__main__":
    l1 = [1, 2, 3]
    sol = Solutions()
    res = sol.subset(l1)
    print(res)
