def bubblesort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
    return arr

if __name__ == "__main__": 
    print(bubblesort([5, 4, 3, 2, 1]))
