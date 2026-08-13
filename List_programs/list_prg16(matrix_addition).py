m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[9,8,7],[6,5,4],[3,2,1]]
result=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append(m1[i][j]+m2[i][j])
    result.append(row)
for row in result:
    print(row)
