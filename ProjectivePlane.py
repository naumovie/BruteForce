import random as rnd
import numpy as np
from itertools import combinations


class ProjectivePlane():
    def __init__(self, hyper_params, data=None):
        self._hyper_params = hyper_params
        self._q = self._hyper_params[0]

        if data is None:
            self._data = self.constructPlane()
        else:
            self._data = data

        

    def generate(self):
        return ProjectivePlane(self._hyper_params)

    def constructPlane(self):
        q = self._q
        N = q ** 2 + q + 1
        data = []
        for i in range(N):
            line = [0 for x in range(N)]
            points = rnd.sample(range(0, N), q + 1)
            for j in range(q + 1):
                line[points[j]] = 1
            data.append(line)
        return data

    def display_data(self):
        print("lines: {0}, columns: {1}".format(len(self._data), len(self._data[0])))
        for i in range(len(self._data)):
            print(self._data[i], " ", sum(self._data[i]))

    def get_data(self):
        return self._data

    def set_data(self, input_data):
        self._data = input_data

    @staticmethod
    def isProjectivePlane(matrix, hyper_params):
        q = hyper_params[0]
        n = q**2 + q + 1
        result = True

        """
        1. Every line contains q + 1 points
        2. Every point lies on q + 1 lines
        3. Any two distinct lines intersect in a unique point
        4. Any two distinct points lie on a unique line.
        """

        #1
        if not all(sum(row) == q+1 for row in matrix): return False
        #2
        if not all([sum([matrix[i][j] for i in range(n)]) == q+1 for j in range(n)]): return False
        #3 
        for pair in combinations(range(n), 2):
            common_points = (sum(matrix[pair[0]][j] * matrix[pair[1]][j] for j in range(n)))
            if common_points != 1: return False
        #4 
        for pair in combinations(range(n), 2):
            common_lines = (sum(matrix[i][pair[0]]*matrix[i][pair[1]] for i in range(n)))
            if common_lines != 1: return False
        

        return True
    
    

    @staticmethod
    def getFitness(matrix, hyper_params):
        fitness = None
        q = hyper_params[0]
        fitness = ProjectivePlane.getFitness_PointPerLine(matrix, q) + ProjectivePlane.getFitness_LineIntersection(
            matrix, q)
        # print("fitness:{0}, pointperline:{1}, lineinter:{2}".format(fitness,ProjectivePlane.getFitness_PointPerLine(matrix, q),ProjectivePlane.getFitness_LineIntersection(
        #     matrix, q)))
        return fitness

    @staticmethod
    def getFitness_PointPerLine(matrix, q):
        count = 0
        np_matrix = np.array(matrix)
        for i in range(len(matrix[0])):
            if (sum(np_matrix[:, i])) != q + 1:
                count += 1
        return count

    @staticmethod
    def getFitness_LineIntersection(matrix, q):
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i != j:
                    res = (np.sum(np.array(matrix[i]) * np.array(matrix[j])))
                    if res > 1 or res == 0:
                        count += 1

        return count

    def get_params(self):
        return self._hyper_params
