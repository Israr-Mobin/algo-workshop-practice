# Valid Palindrome

🔗 **LeetCode** (https://leetcode.com/problems/valid-palindrome/)

## Idea
Ignore anything that isn't a letter or digit, ignore case then check if it reads the same from both ends without building a cleaned-up copy first.

## Approach
- Set two pointers at the start and end of the string.
- Move each one inward skipping non-alphanumeric characters.
- Compare characters (case-insensitive) at both pointers.
- Mismatch -> `False`. Pointers cross -> `True`.

## Complexity
- **Time:** O(n)
- **Space:** O(1)

## Pattern
**Two Pointers** - reach for this when comparing a sequence against itself from both ends.

## Solution
See `solution.py`.