#### [组合总和 III](https://leetcode-cn.com/problems/combination-sum-iii/)

> 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
>
> 说明：
>
> 所有数字都是正整数。
> 解集不能包含重复的组合。 
> 示例 1:
>
> 输入: k = 3, n = 7
> 输出: [[1,2,4]]
> 示例 2:
>
> 输入: k = 3, n = 9
> 输出: [[1,2,6], [1,3,5], [2,3,4]]
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/combination-sum-iii
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        def backtrack(index, tmp_sum, track):
            if tmp_sum == n and k == len(track):
                res.append(track[:])
                return
            for i in range(index, 10):
                if tmp_sum + i > n:
                    break
                
                backtrack(i + 1, tmp_sum + i, track + [i])
        backtrack(1, 0, [])
        return res
```

