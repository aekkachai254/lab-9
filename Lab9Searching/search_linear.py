arr = [7, 10, 12, 14, 16, 20, 29, 37]
# search 14,29
def search(arr, num, j):
    for i in range(len(arr)):
        j += 1
        if arr[i] == num:
            return i, j


def main():
    index, j = search(arr, 14, 0)
    print(f'number 14 in arr index {index}, find {j} times.')
    index, j = search(arr, 29, 0)
    print(f'number 29 in arr index {index}, find {j} times.')

if __name__ == "__main__":
    main()