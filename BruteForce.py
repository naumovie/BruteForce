from ProjectivePlane import ProjectivePlane
from itertools import combinations
from itertools import permutations

class BruteForce():
    def __init__(self, data):
        self._data = data

    @staticmethod
    def start(hyper_params):
        q = hyper_params[0]
        row = [1]*(q+1)+[0]*(q**2)
        all_row_permutations = list(set(permutations(row)))
        all_plane_combinations = list(combinations(all_row_permutations, q**2+q+1))

        for plane in all_plane_combinations:
           if  ProjectivePlane.isProjectivePlane(list(plane), [q]): return list(plane)


        return False
    
    

   
   
        
