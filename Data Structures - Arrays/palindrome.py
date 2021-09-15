# naive solution
# def palindrome(s):
#     if s == s[::-1]:
#         return True
#     return False


# if __name__ == '__main__':
#     print(palindrome('madam'))


# Solution with linear time complexity

# It has O(s) so basically linear running time complexity as far as the number
# of letters in the string is concerned
def is_palindrome(s):
    orignal_str = s
    reversed_str = reverse(s)

    if orignal_str == reversed_str:
        return True
    return False

# O(N) linear running time where N is the number of letters in the string 's'
# N = len(s)
def reverse(str):
    # converts a string into a list of characters
    str = list(str)
    # pointing at the first item
    start_index = 0

    # pointing at the last item
    end_index = len(str) - 1

    while end_index > start_index:
        # swapping of letters
        str[start_index], str[end_index] = str[end_index], str[start_index]
        start_index += 1
        end_index -= 1

    # transform the list of letters into a string
    return ''.join(str)


if __name__ == '__main__':
    print(is_palindrome('kevin'))
