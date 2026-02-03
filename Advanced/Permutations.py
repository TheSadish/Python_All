# generate list of all permutations of (i,j,k) where i+j+k != n

x = int(input("Enter x :"))
y = int(input("Enter y :"))
z = int(input("Enter z :"))
n = int(input("Enter n :"))
    
permutations = []

for i in range(0,x):
    for j in range(0,y):
        for k in range(0,z):
            temp = []
            if (i+j+k != n):
                temp.extend([i,j,k])
                permutations.append(temp)
               
                
# print(permutations)