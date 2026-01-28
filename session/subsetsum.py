class Solution:
    def solve(self, arr, i, target, curr):
        
        if curr == target:
            return True

        
        if i >= len(arr) or curr > target:
            return False

        
        if self.solve(arr, i + 1, target, curr + arr[i]):
            return True

        
        return self.solve(arr, i + 1, target, curr)

    def isSubsetSum(self, arr, sum):
        return self.solve(arr, 0, sum, 0)
