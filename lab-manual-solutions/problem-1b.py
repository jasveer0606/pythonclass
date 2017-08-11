L = []

# Example Input:
# 1,2,4 (\n) 3,6 ..

while True:
    q = raw_input("Enter numbers separated by commas (or q): ")
    if q == "q":
        break
    L.append(tuple(map(int,q.split(","))))
    
print "The inputted list of tuples is :", L
print "The sorted list is :",sorted(L ,key=lambda x:x[-1])

