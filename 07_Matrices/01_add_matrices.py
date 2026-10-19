x=[[2,3,4],
   [2,3,4],
   [1,33,22]]
y=[[1,2,3],
   [3,4,5],
   [5,6,7]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
for r in result:
    print(r)