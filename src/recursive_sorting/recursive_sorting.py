# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
   
    if len(arr) <= 1:
        return arr

    half = len( arr ) // 2

    first_half = merge_sort(arr[:half])
    second_half = merge_sort(arr[half:])

    arr =[]

    while first_half and second_half:
      if first_half[0] < second_half[0]:
        arr.append(first_half.pop(0))
      else:
        arr.append(second_half.pop(0))
    
    while first_half:
      arr.append(first_half.pop(0))
    while second_half:
      arr.append(second_half.pop(0))

    return( arr)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
