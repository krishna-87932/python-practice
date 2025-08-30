# r_lenth, c_lenth = int(input("Enter row length: ")), int(input("Enter column length: "))
#
# matrix = []
# for i in range(r_lenth):
#     row = list(map(int, input(f"Enter row {i+1}: ").split()))
#     while len(row) != c_lenth:
#         print(f"Row must have exactly {c_lenth} elements. Try again.")
#         row = list(map(int, input(f"Enter row {i+1}: ").split()))
#     matrix.append(row)  # This should be outside the while loop
#
# print(f"The matrix is:")
# for row in matrix:
#     print(row)
#
#
# temp = 0
# for index, i in enumerate(matrix):
#     temp += i[index]
#
# print(temp)


r_lenth, c_lenth = int(input('Enter length of Row: ')), int(input('Enter length of column: '))

matrix = []
i=0
while len(matrix) != r_lenth :
        a = list(map(int,input(f"Enter row {i+1}: ").split()))
        if len(a)!=c_lenth:
            print("Invalid input")
        else:
            matrix.append(a)
            i+=1

for i in matrix:
    print(i)

result = 0
for index, i in enumerate(matrix):
    result += i[index]
print(result)