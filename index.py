import random
import matplotlib.pyplot as plt
from ProjectivePlane import ProjectivePlane
from Statistics import Statistics
from BruteForce import BruteForce
from SimulatedAnnealing import SimulatedAnnealing
import time

#plane2 = Statistics.convertDecToBitMatrix([[1,2,4],[1,3,7],[2,6,7],[1,5,6],[4,5,7],[3,4,6],[2,3,5]],2)
#print(plane2)
#plane = ProjectivePlane([2], plane2)
#plane.display_data()

#print(ProjectivePlane.isProjectivePlane(plane2,[2]))

#init_plane = ProjectivePlane([2])
#Statistics.display_data(init_plane.get_data())
#print(ProjectivePlane.isProjectivePlane(init_plane.get_data(), [2]))

#WA!r1609!&FA!ce&

#plane = ProjectivePlane([2])
#plane.display_data()

#x = [[1,1], [2,2], [3,3], [4,4], [5,5]]

#print(all2(sum(num) %2 == 1 for num in x))
q = 3
SA = SimulatedAnnealing(ProjectivePlane([q]), [10000000, 0.999, 100000])
k = 0
while True:
    k += 1
    print(k)
    time1 = time.time()
    res = SA.start()
    
    if res != False:
        print(res, ProjectivePlane.getFitness(res, [q]))
        Statistics.printChart(SA._resultsLog, time.time()-time1, SA._iter_number,  q)





