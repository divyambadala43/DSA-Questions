def reverse(array):
    start_index = 0
    end_index = (len(array) - 1)

    while end_index > start_index:
        array[start_index], array[end_index] = array[end_index], array[start_index]
        start_index += 1
        end_index -= 1

if __name__ == '__main__':
    n = [1,2,3,4,5]
    reverse(n)
    print(n)