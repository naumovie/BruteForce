from ProjectivePlane import ProjectivePlane

class BruteForce():
    def __init__(self, data):
        self._data = data

    def start():
        return False
    
    @staticmethod
    def find_projective_plane(order):
        q = order - 1

        # Generate all possible binary matrices of order x (2^x combinations)
        for i in range(2**(q*q)):
            matrix = [[int(x) for x in bin(i)[2:].zfill(q*q)[j]] for j in range(q)]
            
            if ProjectivePlane.isProjectivePlane(matrix, [q]):
                return matrix

        return None

   
   
        
