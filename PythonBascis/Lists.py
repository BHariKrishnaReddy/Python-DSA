#  interchange first and last elements in a list
l = list(input())
n = len(l)
l[0], l[n - 1] = l[n - 1], l[0]
print(l)


# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
l1 = [2,3,4,5,6,67,7,8,89,6,3,3]
