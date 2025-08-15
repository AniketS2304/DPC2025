def sortColors(arr):
    n = len(arr)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if arr[mid] == 0:
            temp = arr[low]
            arr[low] = arr[mid]
            arr[mid] = temp
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
            high -= 1

if __name__ == "__main__":
    arr = [0, 1, 2, 1, 0, 2, 1, 0]
    sortColors(arr)
    print(arr)
