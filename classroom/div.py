count=0
for i in range(10):
    for j in range(i+1,10):
        if (i+j)%5==0:
            print(i,j)
            count+=1
print("count=",count)
