class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0

        def backtrack(steps_taken: int):
            if steps_taken > n:
                return 

            if steps_taken == n:
                nonlocal res

                res += 1

            backtrack(steps_taken + 1)
            backtrack(steps_taken + 2)

        backtrack(0)

        return res