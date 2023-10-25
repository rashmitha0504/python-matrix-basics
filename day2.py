'''
7.perimeter of matrix
input: 3 4
1 2 3 4
5 6 7 8
9 10 11 12 
output:


m,n=map(int,input().split())
matrix=[]
sum_peri=0 
for i in range(m):
    list_ele=list(map(int,input().split()))
    matrix.append(list_ele)

for i in range(m):#3 0,1,2 
    for j in range(n):#4 0,1,2,3 
        if(i==0 or i==(m-1)  or j==1 or j==(n-1)):
            sum_peri+=matrix[i][j]
print(sum_peri)


8.
Order of matrix
input :
3 4 
1 2 3 4
5 6 7 8
9 10 11 12 

output: 
1 2 3 4 8 7 6 5 9 10 11 12

m,n=list(map(int,input().split()))
matrix=[]
for i in range(m):
    x=list(map(int,input().split())) 
    matrix.append(x)

new_matrix=[]
for i in range(m):
    if(i%2==0):
        for j in range(n):
            new_matrix.append(matrix[i][j]) 
    else:
        for j in range(n-1,-1,-1):
            new_matrix.append(matrix[i][j])
print(new_matrix)
'''