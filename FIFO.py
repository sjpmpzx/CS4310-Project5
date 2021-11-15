import numpy as np
n=10
A=np.random.randint(1,50,(n+1,n+1))
A=np.mat(A)
AK=[]
AK.append(A)
for k in range(1,n):
    v=AK[-1][:,k]
    Mk=np.mat(np.zeros((n+1,n+1)))
    for i in range(n+1):
        Mk[i,i]=1
    for i in range(k+1,n+1):
        Mk[i,k]=-v[i]/v[k]
    temp = Mk*AK[-1]
    AK.append(temp)


