# I have written more than 1 approach to learn the reason why I wrote different approaches! (given short summary at end)


# nums = [int(x) for x in input("Enter elements separated by space: ").split()] -- one way to accept input

nums = list(map(int, input("Enter elements separated by space: ").split()))

# approach 1 - traditional
min,max=nums[0],nums[0]
for i in nums:
	if min >i :
		min = i
	elif max < i :
		max = i
print(min,max)

# approach 2
nums.sort()
print(nums[0],nums[-1])


# approach 3  - GFG (similar to approch 1, handling edge cases)
class pair: # our own data structure
	def __init__(self):
		self.min = 0
		self.max = 0

def getMinMax(arr:list,n:int)->pair:
	minmax = pair()

	if n == 1:
		minmax.min = arr[0]
		minmax.max = arr[0]
		return minmax
	# if n>1 we will intialize min and max (allocating space)
	if arr[0] > arr[1]:
		minmax.min = arr[1]
		minmax.max = arr[0]
	else :
		minmax.min = arr[0]
		minmax.max = arr[1]

	for i in range(2,n):
		if minmax.min > arr[i]:
			minmax.min = arr[i]
		if minmax.max < arr[i]:
			minmax.max = arr[i]
	return minmax


'''
Approach 1 is simple and doesn't modify the original list but has a time complexity of O(n).
Approach 2 is concise and efficient with a time complexity of O(n log n), but it modifies the original list.
Approach 3 is structured and handles edge cases well, but it's more complex and verbose.
'''