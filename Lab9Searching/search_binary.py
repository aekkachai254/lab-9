arr = [7, 10, 12, 14, 16, 20, 29, 37]

def search(arr, num, start, last, j):
    j += 1
    mid = (last+start)//2
    if num == arr[mid]:
        return mid, j
    if num > arr[mid] :
        return search(arr, num, mid+1, last, j)
    elif num < arr[mid] :
        return search(arr, num, start, mid, j)

def main():
    index, j = search(arr, 14, 0, len(arr) - 1, 0)
    print(f'number 14 in arr index {index}, jump {j} times.')
    index, j = search(arr, 29, 0, len(arr) - 1, 0)
    print(f'number 29 in arr index {index}, jump {j} times.')

if __name__ == "__main__":
    main()