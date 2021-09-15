# Binary Search is a searching algorithm for finding an element's position in a sorted array.
# In this approach, the element is always searched in the middle of a portion of an array.
# Binary search can be implemented only on a sorted list of items. If the elements are not sorted already, we need to sort them first.

def binary_search(nums, key, low, high):
    while low <= high:
        # finding mid index
        mid = (low + high) // 2
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    n = [3, 4, 5, 6, 7, 8, 9]
    low = 0
    high = len(n) - 1
    key = 9

    result = binary_search(n, key, low, high)

    if result != -1:
        print("Element is present at index: ", str(result))
    else:
        print("Element not Found")
