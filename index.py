import random
import matplotlib.pyplot as plt
from ProjectivePlane import ProjectivePlane
from Statistics import Statistics

plane2 = Statistics.convertDecToBitMatrix([[1,2,4],[1,3,7],[2,6,7],[1,5,6],[4,5,7],[3,4,6],[2,3,5]],2)
print(plane2)
plane = ProjectivePlane([2], plane2)
plane.display_data()

#WA!r1609!&FA!ce&

#plane = ProjectivePlane([2])
#plane.display_data()

#x = [[1,1], [2,2], [3,3], [4,4], [5,5]]

#print(all(sum(num) %2 == 1 for num in x))

