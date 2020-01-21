# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):

    for i in range(0, len(arr)):
        
        # # save element to sort
        smallest_index = i

        # iterate to the left of the element to find the smallest list element        
        for x in range(i+1, len(arr)):

            if arr[smallest_index] > arr[x]:
                smallest_index = x
        
        # switch the current and smallest elements
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    sorts = 1

    while sorts > 0:
        temp_sorts = 0

        for i in range(0, len(arr)-1):

            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                temp_sorts += 1
        sorts = temp_sorts

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
   