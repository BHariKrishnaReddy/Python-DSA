# I have written more than 1 approach, Try to learn the reason why I wrote different approaches! (given short summary at end)

"""
GFG:
Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

Each student gets one packet.
The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.

basic idea :

We have len(arr) packets of chocolates and we need to pick M packets for M students.
we should pick M packets to get the minimum difference between maximum and minimum packet sizes from the picked ones.
"""

# A 1

def minDiff(arr:list[int],m:int)->int:
    if m == 0 or len(arr) == 0:
        return 0
        
    arr.sort()

    # Number of students cannot be more than number of packets
    if (len(arr) < m):
        return -1
    
    min_diff = arr[-1] - arr[0]

    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff,  arr[i + m - 1] - arr[i])
 
    return min_diff

# A 2 - Sliding window approch ffrom start

def min_diff_chocolates(packets, m):
    if len(packets) < m:
        return -1  

    min_diff = float('inf')

    curr_sum,n = sum(packets[:m]),len(packets)
    min_val,max_val = min(packets[:m]),max(packets[:m])
    min_diff = min(min_diff, max_val - min_val)

    # Slide the window and update the minimum difference
    for i in range(m, n):
        curr_sum -= packets[i - m]
        if packets[i - m] == min_val:
            min_val = min(packets[i - m + 1:i + 1])
        elif packets[i - m] == max_val:
            max_val = max(packets[i - m + 1:i + 1])
        curr_sum += packets[i]
        min_val = min(min_val, packets[i])
        max_val = max(max_val, packets[i])
        min_diff = min(min_diff, max_val - min_val)

    return min_diff

"""
Approach A1:    Time Complexity: O(n log n) due to sorting
                Space Complexity: O(1)
Sorts the array of chocolate packets and then utilizes a sliding window approach to find the minimum difference between the maximum and minimum packet sizes.

Approach A2:    Time Complexity: O(n)
                Space Complexity: O(1)
Utilizes a sliding window approach directly without sorting the array. It maintains a running sum of packet sizes and dynamically updates the minimum difference as the window slides.
"""