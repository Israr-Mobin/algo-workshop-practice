# Permutations II

🔗 **LeetCode** (https://leetcode.com/problems/permutations-ii/)

## Idea
Standard backtracking, but the array can contain duplicates - so you need a rule to stop the same permutation from being generated twice.

## Approach
- Sort the array so equal values sit next to each other.
- Backtrack: at each position, try every unused number.
- Skip a number if it equals the previous one and the previous one hasn't been used yet, this is what blocks duplicates.
- Save the permutation once it reaches full length.

## Complexity
- **Time:** O(n · n!)
- **Space:** O(n) recursion depth

## Pattern
**Backtracking** (with duplicate-skipping) - reach for this when you need every arrangement and have to build a choice, recurse, then undo it.

## Solution
See `solution.py`.