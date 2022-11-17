def insertion_sort(arr: list) -> list:
    n = len(arr)
    sorted_part = 0
    while sorted_part < n:
        j = sorted_part
        while arr[j] < arr[j - 1] and j > 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        sorted_part += 1
    return arr

if __name__ == "__main__":
    print(insertion_sort([5,4,3,2,1]))

