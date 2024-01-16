import numpy as np
import random
import math
from ProjectivePlane import ProjectivePlane

class SimulatedAnnealing():
    def __init__(self, data, hyper_params):
        self._data = data
        

        self._T0 = hyper_params[0]
        self._alpha = hyper_params[1]
        self._iter_limit = hyper_params[2]
        self._resultsLog = []
        self._iter_number = 0

     
    def start(self):
        self._resultsLog = []
        self._current_state = self._data.get_data()
        self._iter_number = 0
        T = self._T0
        
        while T > 0.001 and self._iter_number < self._iter_limit:
            #print("in while", T, self._iter_number)
            next_state = self.generate_state()

            fitness_next_state = ProjectivePlane.getFitness(next_state,self._data._hyper_params)
            fitness_current_state = ProjectivePlane.getFitness(self._current_state, self._data._hyper_params)

            if fitness_next_state < fitness_current_state:  
                self.set_new_state(next_state, fitness_next_state)
            elif math.exp(-(fitness_current_state-fitness_next_state)/T) > random.random():
                self.set_new_state(next_state, fitness_next_state)

            if fitness_current_state == 0: return self._current_state

            T = self._T0*self._alpha**self._iter_number
            self._iter_number += 1
        print("T and iter: ", T, self._iter_number)
        return False




    def generate_state(self):
        next_state = self._current_state.copy()

        line_number = random.randint(0, len(self._current_state)-1)
        point1 = random.randint(0, len(self._current_state[line_number])-1)
        point2 = random.randint(0, len(self._current_state[line_number])-1)

        next_state[line_number][point1], next_state[line_number][point2] = next_state[line_number][point2], next_state[line_number][point1]

        return next_state

    
    def set_new_state(self, new_state, fitness_next_state):
        self._current_state = new_state
        self._resultsLog.append(fitness_next_state)
    
    






