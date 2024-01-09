class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = ["" for i in range(2 * n)]
        result = []

        def helper(openPs, closedPs, parentheses, index):
            if openPs == n and closedPs == n: result.append("".join(parentheses))
            else:
                if openPs < n:
                    parentheses[index] = "("
                    helper(openPs + 1, closedPs, parentheses, index + 1)
                if openPs > closedPs:
                    parentheses[index] = ")"
                    helper(openPs, closedPs + 1, parentheses, index + 1)
        
        helper(0, 0, parentheses, 0)
        return result
