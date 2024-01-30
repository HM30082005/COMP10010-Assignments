def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = []
n = input("""
I heard u wanted to sort an array, huh?
Well look I can do this, u'll pay me later dw about it.
Type in the number of elements in the array man..
          """)
n = int(n)
for i in range(n):
    el = input("give me element of the array, cuz like u gotta stay by what u say. \n")
    el = int(el)
    arr.append(el)
heapSort(arr)
print("Sorted array is")
for i in range(len(arr)):
    print("%d" % arr[i]),
