def cost(i,j,arr,m,s):
    o_cost=99999999
    f_k=i
    for k in range(i,j):
        n_cost=m[i][k]+m[k+1][j]+(arr[i]*arr[k+1]*arr[j+1])
        #print("\nNew Cost for K= ",k," when [",i,",",j,"] is = ",n_cost)
        if n_cost<o_cost:
            o_cost=n_cost
            f_k=k
    s[i][j]=f_k+1
    return o_cost

arr=[30,35,15,5,10,20,25]
m=[[0 for i in range(6)] for j in range(6)]
s=[[0 for i in range(6)] for j in range(5)]

for i in range(0,6):
    j=i
    m[i][j]=0

for i in range(0,5):
    j=i+1
    m[i][j]=cost(i,j,arr,m,s)

for i in range(0,4):
    j=i+2
    m[i][j]=cost(i,j,arr,m,s)

for i in range(0,3):
    j=i+3
    m[i][j]=cost(i,j,arr,m,s)

for i in range(0,2):
    j=i+4
    m[i][j]=cost(i,j,arr,m,s)

for i in range(0,1):
    j=i+5
    m[i][j]=cost(i,j,arr,m,s)

print(m)
print(s)
