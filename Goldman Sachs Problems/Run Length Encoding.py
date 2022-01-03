def encode(arr):
    start = 0
    end = 0
    n = len(arr)
    count = 0
    s = arr[0]
    while (start < n and end < n):
        if (arr[end] != s[-1]):
            s += str(count)
            count = 0
            start = end
            s += str(arr[start])
        else:
            end += 1
            count += 1

    s += str(count)
    return s



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip()
        print(encode(arr))