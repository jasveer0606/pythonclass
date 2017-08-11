L=[]
while True:
    q = raw_input("Enter a number:")
    if q == "end":
        break
    L.append(int(q))

def bubble(L):
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i]<L[j]:
                L[i],L[j] = L[j],L[i]

    return L

def ins_sort(k):
    for i in range(1, len(k)):
        j = i
        while j > 0 and k[j] < k[j-1]: 
            k[j], k[j-1] = k[j-1], k[j]
            j = j - 1
    return k

print "The entered list is :",L
print "The bubblesorted list is :",bubble(L)
print "The insertion sorted list is :",ins_sort(L)
