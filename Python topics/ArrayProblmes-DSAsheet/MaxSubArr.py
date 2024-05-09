# I have written more than 1 approach, Try to learn the reason why I wrote different approaches! (given short summary at end)

# A 1
def maxSubArray( nums: list[int]) -> int:
        m = 0
        stack = []
        for each in nums:
            if m + each < each:
                m = each
            else:
                m = each + m
            stack.append(m)
        return max(stack)

# A 2
def maxSubarr(arr:list,n:int)->list:
    if n == 1:
        return arr[0]
    else:
        max_sub = arr[0]
        cur_sum = arr[0]
        for i in arr[1:]:
            cur_sum = max(i,cur_sum+i)
            max_sub = max(max_sub,cur_sum)
    return max_sub
    
k = maxSubarr([1,2,-3,5,6],5)
print(k)

"""
Approach A1:    Time Complexity: O(n)
                Space Complexity: O(n) (due to the stack)
Utilizes a dynamic programming approach with a stack to keep track of maximum subarray sums.

Approach A2:    Time Complexity: O(n)
                Space Complexity: O(1) (constant space)
Implements Kadane's algo, which efficiently finds the max_subarray sum using constant space.
"""