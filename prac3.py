def edit_distance(str1,str2):
    matrix = []
    for i in range(len(str2)+1):
        matrix.append([])
        for j in range(len(str1) + 1):
            matrix[i].append(0)
    for i in range(len(str2)+1):
        for j in range(len(str1)+1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif str1[j-1] == str2[i-1]:
                matrix[i][j] = matrix[i-1][j-1]
            elif str1[j-1] != str2[i-1]:
                matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+ 1
    print(f"Edit Distance: {matrix[-1][-1]}")
    for i in range(len(str2)+1):
        for j in range(len(str1)+1):
            print(matrix[i][j],end=" ")
        print()
edit_distance("SANDESH","SANDY")