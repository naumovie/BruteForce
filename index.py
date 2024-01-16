import random
import matplotlib.pyplot as plt
from ProjectivePlane import ProjectivePlane
from Statistics import Statistics
from BruteForce import BruteForce

plane2 = Statistics.convertDecToBitMatrix([[1,2,4],[1,3,7],[2,6,7],[1,5,6],[4,5,7],[3,4,6],[2,3,5]],2)
print(plane2)
plane = ProjectivePlane([2], plane2)
plane.display_data()

print(ProjectivePlane.isProjectivePlane(plane2,[2]))

init_plane = ProjectivePlane([2])
#Statistics.display_data(init_plane.get_data())
#print(ProjectivePlane.isProjectivePlane(init_plane.get_data(), [2]))

#WA!r1609!&FA!ce&

#plane = ProjectivePlane([2])
#plane.display_data()

#x = [[1,1], [2,2], [3,3], [4,4], [5,5]]

#print(all2(sum(num) %2 == 1 for num in x))


order = int(input("Enter the order of the projective plane (q): "))
projective_plane = BruteForce.find_projective_plane(order)

if projective_plane:
    print("Found a projective plane:")
    for row in projective_plane:
        print(row)
else:
    print("No projective plane found for the given order.")