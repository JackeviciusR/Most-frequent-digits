# Most frequent digits

Method calculates the digits that accur the most number of times in the array, return the array of these digits in ascending order.

### Example

For `a = [25, 2, 3, 57, 38, 41]` the output should be  `mostFrequentDigits(a) = [2, 3, 5]`.

Here are the number of each digit appears in the array:

```
  0 -> 0
  1 -> 1
  2 -> 2  
  3 -> 2
  4 -> 1
  5 -> 2
  6 -> 0
  7 -> 1
  8 -> 1
```

The most number of times any number occurs in the array is `2`, and the digits which appear `2` times are `2`, `3` and `5`. So the answer is `[2, 3, 5]`.

### Input/Output
* [execution time limit] **4 seconds** (py3)
* [input] **array.integer a**.

*Guaranteed constraints:*

`1 <= s.length <= 10^5`
`1 <= a[i] < 100`

* [output] **array.integer**
The array of most frequently occurring digits, sorted in ascending order.

## Result
Method works good.
