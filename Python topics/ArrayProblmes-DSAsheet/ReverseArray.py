# I have written more than 1 approach to learn the reason why I wrote different approaches! (given short summary at end)

# A 1

nums = list(map(int,input("Enter array with space as sep char").split()))

newNums = nums[::-1] # nums.reverse()
print(newNums)

# A 2
n = len(nums)
for i in range(0,n):
    newNums[i] = nums[n-1-i] # newNums is alredy intilized so i'm not re-init it
print(newNums)

# A 3 Using list comprehension
reversed_nums = [nums[i] for i in range(len(nums)-1, -1, -1)]

"""
Approach A1 (using list slicing) is generally considered the best among the provided options. It's concise, clear, Pythonic, and efficient. It directly expresses the intention to reverse the list using a well-known Python feature. It's also easier to read and understand compared to the loop-based approach in A2. 

Approach A3 is also clear and Pythonic but less efficient due to creating a new list.
"""