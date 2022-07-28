# Problem

```
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
```


# Discussions
Nick
> The key to the problem is that there is ALWAYS only 1 pair of numbers that satisfy the condition of adding together to be the target value.
We can assume that for all the numbers in the list (x1, x2, ... xn) that there exists a pair such that xa + xb = target To solve this with a single pass of the list we can change the equation above to xa = target - xb and since we know the target as long as we maintain a record of all previous values in the list we can compare the current value (xa) to it's ONLY pair, if it exists, in record of all previous values (xb). To keep a record of the previous values and their indices I have used a dictionary. Commonly known as a map in other languages. This allows me to record each previous number in the dictionary alongside the indice as a key value pair (target-number, indice).

Gary 
> Since this problem require to output pair of indices instead of pair of values, so we need an array, let say arr to store their value with their respective indices.

## 3

## 4