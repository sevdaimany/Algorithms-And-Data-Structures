def bitMask(set):

    length = len(set)

    # 1 << n = 2**n
    for mask in  range(1 << length) :
        for i in range(length):

            if mask & (1 << i):
                print(set[i] , end = ' ')
        print()

setsMembers = [int(member) for member in input().split(' ')]
bitMask(setsMembers)