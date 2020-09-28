def bubble_sort():
    for i in range(n - 1):
        for j in range(i+1 , n):
            if arr[i] > arr[j]:
                arr[i] , arr[j] = arr[j] , arr[i]


n = int(input())
arr = [int(num) for num in input().split(" ")]

bubble_sort()

[print(num ,end = " ") for num in arr]
