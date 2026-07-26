class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLetter = {"2":"abc", "3":"def", "4":"ghi", 
        "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans = []

        def dfs(index, temp):
            if index == len(digits):
                ans.append(temp)
                return

            for l in numToLetter[digits[index]]:
                dfs(index + 1, temp + l)

        if digits != "": dfs(0, "")
        return ans