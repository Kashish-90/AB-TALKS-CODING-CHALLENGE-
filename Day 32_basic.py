def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        print(f"Left={left}, Mid={mid}, Right={right}")

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


vault = [5, 10, 15, 20, 25, 30, 35, 40, 45]

target = 30

result = binary_search(vault, target)

if result != -1:
    print("Code found at index:", result)
else:
    print("Code not found")
