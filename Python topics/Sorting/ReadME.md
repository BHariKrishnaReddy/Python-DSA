<h1 align = 'center'>Sorting in Python</h1>

* Sorting is defined as arranging data in a specific order and sorting methods are used to arrange data (usually numerical) in ascending or decreasing order. 
* With bigger amounts of data, we want to maximize efficiency and speed. If the methods we use to sort the data are inefficient, sorting a huge amount of data can use a significant amount of computational resources. We will now go over the various sorting algorithms and compare them in terms of time complexity.


>  sorted() 

*  This method sorts the given sequence, set, and dictionary (which is not a sequence) in ascending or descending order and always returns a sorted list. The original sequence is unaffected by this procedure.

    ```
    Syntax: sorted(iteraable, key, reverse=False)
    Return Type: Returns a sorted list. 
    ```

>  sort() 

*  The sort() function is quite similar to the sorted() function, however unlike sorted, it returns nothing and modifies the original sequence. Furthermore, sort() is a list class method that can only be used with lists.

    ```
    Syntax: List_name.sort(key, reverse=False)
    Return Type: None 
    ```




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

#### Heap Sort

* Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for remaining elements.

* Binary Heap is a Complete Binary Tree, it can be easily represented as array and array based representation is space efficient. If the parent node is stored at index I, the left child can be calculated by 2 * I + 1 and right child by 2 * I + 2 (assuming the indexing starts at 0).

* Heap Sort Algorithm for sorting an array in increasing order:

    1. Build a max heap from the input data.
    2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing  the size of heap by 1. Finally, heapify the root of tree.
        * Heapify procedure can be applied to a node only if its children nodes are heapified. So the heapification must be performed in the bottom up order.
        * The heapify procedure calls itself recursively to build heap
        in top down manner.
    3. Repeat above steps while size of heap is greater than 1.