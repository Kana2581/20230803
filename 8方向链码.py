def freeman_chain_code(matrix):
    directions = [(0, 1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]
    chain_code=[];
    start_point = None
    current_poin = None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                start_point = (i, j)
                break
        if start_point:
            break
    current_point = start_point
    while True:
        for i in range(8, 0, -1):
            i=i%8
            temp_directions=(current_point[0]+directions[i][0],current_point[1]+directions[i][1])
            if(temp_directions[0]>=0 and temp_directions[0]<len(matrix) and temp_directions[1]>=0 and temp_directions[1]<len(matrix[0]) and matrix[temp_directions[0]][temp_directions[1]]):
                matrix[current_point[0]][current_point[1]]=0
                current_point=temp_directions
                chain_code.append(i)
                break
        if len(chain_code)>2:
            matrix[start_point[0]][start_point[1]]=1
        if current_point==start_point:
            break
    return chain_code
def get_differential(arr,n):
    for i in range(len(arr)):
        print((arr[(i+1)%len(arr)]-arr[i]+n) % n,end=' ')

contour = [
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

result = freeman_chain_code(contour)
print("链码")
print(result)
print("差分")
get_differential(result,8)
        

    

