from itertools import combinations
from itertools import permutations
import random
from ProjectivePlane import ProjectivePlane
from Statistics import Statistics

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

#print(for i in range(3): sum([matrix[j][i] for j in range(3)]) % 2 == 0)

#print([matrix[i][j]] for i in range(3) for j in range(3))
"""
print(
    all([
        sum(
            [matrix[i][j] for i in range(3)
             ]
             ) < 19 for j in range(3)])
    )


#print([[matrix[i]*matrix[j]] for i in range(3) for j in range(3) if i != j])


for pair in combinations(range(rows), 2):
        common_points = sum(matrix[pair[0]][j] * matrix[pair[1]][j] for j in range(cols))
        if common_points != 1:
            return False


binmatrix = [
   [1,0,1],
   [1,1,1],
   [1,1,0]
]
#print([i for i in combinations(range(3), 2)])
for pair in combinations(range(3), 2):
   common_points = (sum(binmatrix[pair[0]][j] * binmatrix[pair[1]][j] for j in range(3)))

def f():
    binmatrix = [
        [1,0,1],
        [0,1,1],
        [1,1,0]
                ]
    for pair in combinations(range(3), 2):
        common_points = (sum(binmatrix[pair[0]][j] * binmatrix[pair[1]][j] for j in range(3)))
        if common_points != 1: return False
    return True
    
print(f())"""
"""
print([i for i in combinations(range(3), 2)])
binmatrix = [
   [1,0,1],
   [1,1,1],
   [1,1,0]
]

for pair in combinations(range(3), 2):
   # sum(binmatrix[i][pair[0]]*binmatrix[i][pair[1]]) for i in range(3)
    sum_col = 0
    for i in range(3):
        sum_col += (binmatrix[i][pair[0]]*binmatrix[i][pair[1]])
   # print(sum_col)
"""
"""
for pair in combinations(range(3), 2):
    common_lines = sum(matrix[i][pair[0]] * matrix[i][pair[1]] for i in range(3))
    if common_lines != 1:
        1
"""

"""
for pair in combinations(range(3), 2):
    print(sum(binmatrix[i][pair[0]]*binmatrix[i][pair[1]] for i in range(3)))

   """


"""

q = 2
first_row = [1] * (q + 1) + [0] * (q * (q - 1))
first_col = [1] + [0] * (q - 1) + [1] + [0] * (q * (q - 1))
#print(first_row, first_col) 

for i in range(2**(q * (q - 1) // 2)):
    remaining_matrix = [[int(x) for x in bin(i)[2:].zfill(q * (q - 1) // 2)[j]] for j in range(q - 1)]

    print(remaining_matrix)

    # Reflect the remaining matrix to exploit symmetry
    reflected_matrix = [row[::-1] for row in remaining_matrix]



    # Construct the full matrix
    matrix = [first_row] + [[first_col[j]] + remaining_matrix[j] for j in range(q - 1)]

    print(matrix)

    # Check if the generated matrix satisfies projective plane properties
    #if is_projective_plane(matrix, q):
        #return matrix

    # Check if the reflected matrix satisfies projective plane properties
    #matrix_reflected = [first_row] + [[first_col[j]] + reflected_matrix[j] for j in range(q - 1)]
    #if is_projective_plane(matrix_reflected, q):
        #return matrix_reflected

        """
"""
q = 2
first_row = [0]*4 + [1]*3
random.shuffle(first_row)
#print(first_row)

for i in permutations(first_row,7):
    #rint(i)
"""

"""
m = [1,0,0]

all_row_perm = set(permutations(m))
for i, permutation in enumerate(all_row_perm, start=1):
    print(i, " ", permutation)


def display_permutations(matrix):
    matrix_size = len(matrix)
    row_size = len(matrix[0])

    for i in range(matrix_size):
        row = matrix[i]
        all_permutations = list(permutations(row))

        print(f"Row {i + 1} Permutations:")
        for perm in all_permutations:
            print(list(perm))
        print()

# Example usage:
matrix = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]
]

display_permutations(matrix)
"""
print("test")
row = [1] * 3 + [0] * 4

#all_perm = list(set(permutations(row)))
#print(all_perm)
# print(len(all_perm[0:10]))

#print(all_perm[0:10]
"""
matrix = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]
]

list1 = [1,2,3,4,5,6]
list1[0], list1[2] = list1[2], list1[0]
print(list1)
"""
print(sum([True, True, False]))

plane2 = Statistics.convertDecToBitMatrix([[1,2,4],[1,3,7],[2,6,7],[1,5,6],[4,5,7],[3,4,6],[2,3,5]])
plane = ProjectivePlane([2])
plane.display_data()
print(plane.getFitness_LineIntersection(plane.get_data(), [2]), plane.getFitness_LinesPerPoint(plane.get_data(), [2]), plane.getFitness_PointsCollinear(plane.get_data(), [2]))
