class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        aset = set(["a"])
        for _ in range(n):
            n_set = set()
            for string in aset:
                all_indices = [i for i, char in enumerate(string) if char == "a"]
                new_chars = "a(a)a"
                for index_to_replace in all_indices:
                    stprime = string[:index_to_replace] + new_chars + string[index_to_replace + 1:]
                    n_set.add(stprime)
            aset = n_set
        
        return [s.replace('a', '') for s in aset]

