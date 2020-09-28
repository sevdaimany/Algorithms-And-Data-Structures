def grayCode(n,arr1,arr2):
    if n == 0:
        return
    else:
        for i in range(len(arr1)):
            arr1[i] = "0"+arr1[i]
        for i in range(len(arr2)):
            arr2[i] = "1"+arr2[i]
        arr1.extend(arr2)
        arr2 = arr1[::-1]
        grayCode(n-1,arr1,arr2)

    



n  = int(input())

arr1 = [""]
arr2 = [""]

grayCode(n,arr1,arr2)

[print(num) for num in arr1]

