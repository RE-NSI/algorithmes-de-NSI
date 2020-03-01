def tri_ins(t):
    for k in range(1,len(t)):
        temp=t[k]
        j=k
    while j>0 and temp<t[j-1]:
        t[j]=t[j-1]
        j-=1
        t[j]=temp
    return t