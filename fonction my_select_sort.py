def my_select_sort (t):
    res = [0]*len(t)
    for i in range (len(t)):
        j= index_of_the_smallest(t)
        res[i]=t[j
        remove(t,j)]
    return res