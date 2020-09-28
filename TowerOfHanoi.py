def TowerOfHanoi(n , from_rod, to_rod, aux_rod): 
    global round
    if n == 1: 
        #Base condition !!there is only one ring!!
        print (round,from_rod ,to_rod )
        round += 1
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print (round,from_rod,to_rod) 
    round += 1
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 
          
# A variable for count the step of transmission of rings
round = 1

# number of disks
n  = int(input())
TowerOfHanoi(n, 'A', 'B', 'C')  
# A, C, B are the name of rods 
   