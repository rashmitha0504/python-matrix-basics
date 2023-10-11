'''
Input 
3 3 
1 2 3
4 5 6 
7 8 9 

3 3 
1 2 3
4 5 6
7 8 9


1.Addition and subtraction of matrix
1.output 
2 4 6
8 10 12 
14 16 18

row,col=list(map(int,input().split()))
result_list_1=[]
for i in range(row):
    values=list(map(int,input().split()))
    result_list_1.append(values)

row,col=list(map(int,input().split()))
result_list_2=[]
for i in range(row):
    values=list(map(int,input().split()))
    result_list_2.append(values)

for i in range(row):
    result=[]
    for j in range(col):
        add=result_list_1[i][j]+result_list_2[i][j]
        result.append(add)
    print(result)

2.indexing chnageing
2.Output 
1 4 7
2 5 8
3 6 9

row,col=list(map(int,input().split()))
result_list_1=[]
for i in range(row):
    values=list(map(int,input().split()))
    result_list_1.append(values)

for i in range(row):
    result=[]
    for j in range(col):
        result.append(result_list_1[j][i])
    print(result)

    
3.diagonal -1 
3.Output
1 5 9

row,col=list(map(int,input().split()))
result_list_1=[]
for i in range(row):
    values=list(map(int,input().split()))
    result_list_1.append(values) 

for i in range(row):
    result=[]
    for j in range(col):
        if (i==j):
            result.append(result_list_1[i][j])
    print(result)


4.diagonal-2 
4.Output 
3 5 7

row,col=list(map(int,input().split()))
result_list_1=[]
for i in range(row):
    values=list(map(int,input().split()))
    result_list_1.append(values) 

for i in range(row):
    result=[]
    for j in range(col):
        if (i+j==(col-1)):
            result.append(result_list_1[i][j])
    print(result)


5.diagonal of numbers
5.Output 
1
2 4
3 5 7
6 8
9

row,col=list(map(int,input().split()))
result_list_1=[]
for i in range(row):
    values=list(map(int,input().split()))
    result_list_1.append(values) 

for i in range(row+col-1):
    result=[]
    for j in range(row):
        for k in range(col):
            if(i==j+k):
                result.append(result_list_1[j][k]) 
    print(result)


6.daigonal opposite 
6.output 
1
4 2
3 5 7
8 6
9

row,col=list(map(int,input().split()))
result_list=[]
for i in range(row):
    values=list(map(int,input().split()))
    result_list.append(values)

for i in range(row+col-1):
    result=[]
    for j in range(row):
        for k in range(col):
            if(i==j+k):
                result.append(result_list[k][j])
    print(result)

'''
