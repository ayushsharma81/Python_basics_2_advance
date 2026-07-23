def missingRange(arr, low, high):
    res = []

    # Check every number in the given range
    for num in range(low, high + 1):

        found = False

        # Search current number in the array
        for x in arr:
            if x == num:
                found = True
                break

        # If not present, add to result
        if not found:
            res.append(num)

    return res


if __name__ == '__main__':
    arr = [1, 4, 11, 51, 15]
    low = 50
    high = 55

    res = missingRange(arr, low, high)

    print('[', end='')
    for i in range(len(res)):
        print(res[i], end='' if i == len(res) - 1 else ', ')
    print(']')
