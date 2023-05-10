#### Bubble Sort
* Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

    > time complexity of O(n^2) in the average

#### Selection Sort
* Algorithm sorts an array by repeatedly finding the minimum element (considering ascending order or viceversa) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

* The subarray which is already sorted. Remaining subarray which is unsorted. In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

* Selection sort is an in-place sorting algorithm. Sorts without requiring additional memory.

    > time complexity of O(n^2)

#### Insertion Sort
* Algorithm that works by dividing the list into two parts: a sorted part and an unsorted part. It iterates through the unsorted part and inserts each element into its correct position within the sorted part. 
* Performs well on small lists or partially sorted lists and has an advantage of being an in-place sorting algorithm (it doesn't require extra memory space)

    > best O(n) worst-case time complexity of O(n^2)


#### Merge Sort:
* Think of it as a recursive algorithm continuously splits the array in half until it cannot be further divided.
* If the array becomes empty or has only one element left, the dividing will stop,
    * It is the base case to stop the recursion. 
    * If the array has multiple elements, split the array into halves and recursively invoke the merge sort on each of the halves.
    
* Finally, when both halves are sorted, the merge operation is applied. Merge operation is the process of taking two smaller sorted arrays and combining them to eventually make a larger one.



#### Quick Sort
* Lomuto’s Partition Scheme:

    This algorithm works by assuming the pivot element as the last element. If any other element is given as a pivot element then swap it first with the last element. Now initialize two variables i as low and j also low,  iterate over the array and increment i when arr[j] <= pivot and swap arr[i] with arr[j] otherwise increment only j. After coming out from the loop swap arr[i] with arr[hi]. This i stores the pivot element.

* Hoare’s Partition Scheme:

    Hoare’s Partition Scheme works by initializing two indexes that start at two ends, the two indexes move toward each other until an inversion is (A smaller value on the left side and greater value on the right side) found. When an inversion is found, two values are swapped and the process is repeated.

 



