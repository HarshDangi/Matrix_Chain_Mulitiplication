def cost(i,j,arr,m,s):
    if(i==j):
        return 0
    o_cost=99999999
    f_k=i
    for k in range(i,j):
        n_cost=m[i][k]+m[k+1][j]+(arr[i]*arr[k+1]*arr[j+1])
        #print("\nNew Cost for K= ",k," when [",i,",",j,"] is = ",n_cost) #This Line is for debugging purposes
        if n_cost<o_cost:
            o_cost=n_cost
            f_k=k
    s[i][j]=f_k+1
    return o_cost

arr=input("Enter the Dimensions : ").split()
arr=[int(x) for x in arr]
size=len(arr)-1
m=[[0 for i in range(size)] for j in range(size)]
s=[[0 for i in range(size)] for j in range(size-1)]

for l in range(size):
    for i in range(size-l):
        j=i+l
        m[i][j]=cost(i,j,arr,m,s)

print("M matrix is : \n",m)
print("S matrix is : \n",s)
