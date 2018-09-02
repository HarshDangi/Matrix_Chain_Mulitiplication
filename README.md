# Matrix_Chain_Mulitiplication
This is the Program to find best order for multiplication of matrices to reduce cost

What I have done here is that, i took the information of dimensions of matrices i.e. P values and stored it in 'arr'

now, I have applied the formula m[i,j]=m[i,k]+m[k+1,j] + P(i-1) * P(k) * P(j)

This formula have been adjusted accordingly as arrays start from 0

the cost are stored in 'm' matrix and k values are stored in 's' matrix

For now I've took the case for six matrices and later on I will adapt the code for any number.
