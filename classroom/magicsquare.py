import sys

def formingMagicSquare(s):
    
    min2=lambda l1,l2: [[abs(l1[i][j]-l2[i][j]) for j in range(3)] for i in range(3)]

    sqs = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]
    
    lowestcost = [min2(x,s) for x in sqs]
    sums = [[sum(i) for i in x] for x in lowestcost]

    for i in range(8):
        print(lowestcost[i],sums[i],sum(sums[i]))
    
    minsum = min([sum(sums[i]) for i in range(8)])
    return minsum

if __name__ == "__main__":
    s = [[4,8,2],[4,5,7],[6,1,6]]
    s2 = [[2,2,7],[8,6,4],[1,2,9]]
    formingMagicSquare(s2)
    #print("Result =",result)
