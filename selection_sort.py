def selection_sort():

    for i in range(n -1):

        min_index  = i

        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i] , arr[min_index] = arr[min_index] , arr[i]
     


n = int(input())
arr = [int(num) for num in input().split(" ")]

selection_sort()

[print(num ,end = " ") for num in arr]