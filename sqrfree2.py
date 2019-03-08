n=input()
R=range(n)
A=[1]*n
for i in R[2:]:
 for x in R[::i*i]:A[x]=0
print sum(A)
