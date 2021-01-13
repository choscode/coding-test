def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def find_index(n, target, array):
    result = binary_search(array, target, 0, n - 1)
    if result == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(result + 1)

n = 10
target = 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
find_index(n, target, array) # expected 4

n = 10
target = 7
array = [1, 3, 5, 6, 11, 13, 15, 17, 19]
find_index(n, target, array) # expected 원소가 존재하지 않습니다.
