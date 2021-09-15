def find_duplicates(nums):
    # we can achieve O(N) linear running time where N=len(nums)
    for i in nums:
        if nums[abs(i)] >= 0:
            nums[abs(i)] = -nums[abs(i)]
        else:
            print("Repetition found: %s" % str(abs(i)))


if __name__ == '__main__':
    # Conditions for using this method:
    # List cannot have items < 0
    # Maximum item is smaller than the size of the list
    n = [2, 6, 5, 1, 4, 3, 2]
    find_duplicates(n)
