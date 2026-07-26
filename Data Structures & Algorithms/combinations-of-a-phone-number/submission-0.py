class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLetter = {"2":"abc", "3":"def", "4":"ghi", 
        "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans = []
        temp = []
        if len(digits) == 0: return []
        def dfs(index):
            if index == len(digits):
                ans.append("".join(temp))
                return

            for l in numToLetter[digits[index]]:
                temp.append(l)
                dfs(index + 1)
                temp.pop()

        
        dfs(0)
        return ans