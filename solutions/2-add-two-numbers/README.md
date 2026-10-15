# 2. Add Two Numbers

- Difficulty: **Medium**
- Language: **python3**
- Topics: Linked List, Math, Recursion
- LeetCode: https://leetcode.com/problems/add-two-numbers/

## Problem

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 

Constraints:

	
- The number of nodes in each linked list is in the range [1, 100].
	
- 0 <= Node.val <= 9
	
- It is guaranteed that the list represents a number that does not have leading zeros.

## Approach

We traverse both linked lists simultaneously, adding corresponding digits along with any carry from the previous step. For each pair of nodes (or None), we compute the sum, create a new node with value sum%10, and propagate carry=sum//10. We continue until both lists are exhausted and no carry remains. A dummy head simplifies list construction.

## Complexity

- Time: O(max(n, m)) where n and m are the lengths of the input lists.
- Space: O(max(n, m)) for the resulting linked list (excluding input nodes).

## Hints

No hints provided.
