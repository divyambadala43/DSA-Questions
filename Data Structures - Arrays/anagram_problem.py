def is_anagram(str1, str2):
    # if length differ - not anagrams
    if len(str1) != len(str2):
        return False

    # we have to sort the letters of the strings and then we have to
    # compare the letters with the same indexes
    # this is the bottleneck because it has O(NlogN)
    str1 = sorted(str1)
    str2 = sorted(str2)
    print(str1)
    print(str2)

    # check letters with same indexes
    # O(N) running time
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
        return True

# overall running time => O(NlogN) + O(N) = O(NlogN)

if __name__ == '__main__':
    s1 = ['f', 'l', 'u', 's', 't', 'e', 'r']
    s2 = ['r', 'e', 's', 't', 'f', 'u', 'l']
    print(is_anagram(s1, s2))
