def binary_search_using_recursion(nums, key, low, high):
    if low <= high:
        mid = (low + high) // 2

        if nums[mid] == key:
            return mid
        elif nums[mid] > key:
            return binary_search_using_recursion(nums, key, low, (mid-1))
        else:
            return binary_search_using_recursion(nums, key, (mid+1), high)
    else:
        return -1


if __name__ == '__main__':
    n = [3, 4, 5, 6, 7, 8, 9]
    key = 3

    result = binary_search_using_recursion(n, key, 0, (len(n)-1))

    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("Element not found")
