# Valid Parentheses

🔗 **LeetCode** (https://leetcode.com/problems/valid-parentheses/)

## Idea
Every closing bracket has to match the *most recently* opened bracket that "most recent" behavior is exactly what a stack gives you for free.

## Approach
- Create an empty stack.
- Opening bracket -> push it.
- Closing bracket -> check the top of the stack pop and continue if it matches, otherwise return `False`.
- After the loop, return `True` only if the stack is empty.

## Complexity
- **Time:** O(n)
- **Space:** O(n)

## Pattern
**Stack** - reach for this with nested structures, matching pairs or anything needing undo/LIFO behavior.

## Solution
See `solution.py`.