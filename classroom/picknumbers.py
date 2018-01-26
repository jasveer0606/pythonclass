def probs(n):
    return [n-1,n,n+1]

def vortexMap(listed):
    start,vMap=listed[0],[]
    probables=probs(start)
    for number in listed:
        if number in vMap:
            vMap.append(number)
            continue
        if number in probables and sum([x in vMap for x in probs(number)]):
            vMap.append(number)
            probables.remove(number)
    return vMap
    
print(vortexMap([4,6,5,3,3,1]))
