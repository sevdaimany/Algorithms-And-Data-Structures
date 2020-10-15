def subSets(set , subSet, n ,k):
    if k == n :
        for i in range(n):
            if subSet[i] != -1:
                print(subSet[i] , end = ' ')
        print()
        return


    subSet[k] = -1
    subSets(set , subSet , n , k+1)

    subSet[k] = set[k]
    subSets(set , subSet , n , k+1)



setsMembers = [int(member) for member in input().split(' ')]

firstSubset = [-1 for _ in  range(len(setsMembers))]

subSets(setsMembers ,firstSubset , len(setsMembers),0 )
