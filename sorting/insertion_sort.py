def insertionSort():
   for i in range(1,n):
       p = i
       while  p > 0 and arr[p] < arr[p-1]:
           arr[p], arr[p -1] = arr[p-1] , arr[p]
           p -= 1 



n = int(input())
arr = [int(num) for num in input().split(" ")]

insertionSort()

[print(num ,end = " ") for num in arr]