class Solution:
    # BruteForce time: O(n), space: O(n)
    def brute_force(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

        return s == ""
    

    # OPTIMAL SOLUTION
    # Stack time: O(n), space: O(n)
    def stack(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "]": "[", "}": "{"}

        for close_bracket in s:
            if close_bracket in close_to_open:
                if stack and stack[-1] == close_to_open[close_bracket]:
                    stack.pop()
                else: 
                    return False
                
            else:
                stack.append(close_bracket)

        return True if not stack else False


# Object "Solution" instance 
solution = Solution()

# Sample input for algorithm
s = "([{}])"

# All algo outputs
print(solution.brute_force(s))
print(solution.stack(s))




        