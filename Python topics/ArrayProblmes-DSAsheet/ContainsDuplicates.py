# I have written more than 1 approach, Try to learn the reason why I wrote different approaches! (given short summary at end)

# A 1
def dups(arr:list[int])->bool:
    print(len(arr) , len(set(arr)))
    if len(arr) != len(set(arr)):
        return True
    return False
    ## return(len(set(nums))!=len(nums))

val = dups([1,2,3,4,5,6,7,3])
print(val)

# A 2
def cDups(arr:list[int])->bool:
    uval=set()
    for i in arr:
        if i not in uval:
            uval.add(i)
        else:
            return True
    return False

"""

Approach A1:    Time Complexity: O(n)
                Space Complexity: O(n) (due to the set)
Checks for duplicates in the list by converting it to a set and comparing the lengths.

Approach A2:    Time Complexity: O(n)
                Space Complexity: O(n) (due to the set)
Utilizes a set to store unique values encountered while iterating through the list and checks for duplicates.

Both are simliar but in A2 we will not iterate thru list unless in it unique

"""