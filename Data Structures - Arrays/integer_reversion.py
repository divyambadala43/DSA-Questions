def reverse(num):
    reverse = 0
    remainder = 0
    while num > 0:
        remainder = num % 10
        reverse = reverse * 10 + remainder
        num = num // 10

    return reverse


if __name__ == '__main__':
    print(reverse(5634))
