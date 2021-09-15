# Linear search is a sequential searching algorithm where we start from one end and check every element of the list
# until the desired element is found. It is the simplest searching algorithm.

def linear_search(nums, n, key):
    for i in range(0, n):
        if nums[i] == key:
            return i
    return -1


if __name__ == '__main__':
    nums = [2, 4, 0, 1, 9]
    n = len(nums)
    key = 5
    result = linear_search(nums, n, key)

    if result == -1:
        print("Element not found")
    else:
        print("Element found at index: ", result)
