#Practice_Data-Structures_Arrays_Dynamic-Array
def dynamicArray(n, queries):
    lastNumber = 0
    seqList=[];
    for i in range(n):
        seqList.append([])
    res = [];
    for k, x, y in queries:
        index = (x^lastNumber)%n
        if k==1:
            seqList[index].append(y)
           # print(seqList)
        else:
            size = len(seqList[index])
           # print(seqList)
           # print(size)
            lastNumber = seqList[index][y%size]
            print(lastNumber)
            res.append(lastNumber)
            
    return res 
nq = input().rstrip().split()
n = int(nq[0])
q = int(nq[1])
queries = []
for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))
result = dynamicArray(n, queries)
