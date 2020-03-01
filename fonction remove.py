def remove(t,j):
    res=[0]*(len(t))
    for j in range (len(t)):
        if j< i:
            res[j]=t[j]
        if j>i :
            res[j-1]=t[j]
    return res