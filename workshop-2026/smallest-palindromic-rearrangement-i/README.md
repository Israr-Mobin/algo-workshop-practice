# Smallest Palindromic Rearrangement I

🔗 **LeetCode** (https://leetcode.com/problems/smallest-palindromic-rearrangement-i/)

## Idea
`s` is already a palindrome so its letter counts are "palindrome-friendly" (at most one odd count), build the smallest left half from those letters, mirror it and drop any leftover odd letter in the middle.

## Approach
- Count each character's frequency.
- Take half of each count (integer division), this is the pool for the left half.
- Sort that pool ascending to form the left half (the sorted arrangement of a fixed set of letters is always the lexicographically smallest one).
- If one character has an odd count, place it in the middle.
- Right half = reverse of the left half.

## Complexity
- **Time:** O(n)
- **Space:** O(n)

## Pattern
**Greedy / Frequency Counting** - reach for this when a rearrangement problem depends only on character counts, not original positions.

## Solution
See `solution.py`.