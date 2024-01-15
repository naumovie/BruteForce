import matplotlib.pyplot as plt


class Statistics:
    @staticmethod
    def display_data(data):

        print("lines: {0}, columns: {1}".format(len(data), len(data[0])))
        for i in range(len(data)):
            print(f"{i+1}, " , end="")
        print("")
        for i in range(len(data)):
            print(data[i])

    @staticmethod
    def display_list(data):
        print("elements: {0}, lines: {1}, columns: {2}".format(len(data), len(data[0]), len(data[0][0])))
        for i in range(len(data)):
            Statistics.display_data(data[i])

    @staticmethod
    def convertDecToBitMatrix(matricDec, Q):
        q = Q
        N = q ** 2 + q + 1
        data = []
        for i in range(N):
            line = [0 for x in range(N)]
            data.append(line)

        for i in range(len(matricDec)):
            for j in range(len(matricDec[i])):
                data[i][matricDec[i][j]-1]=1
        return data

    @staticmethod
    def printChart(resultLog, time_exec, num_gen, q):
        print("Execution Time: ", time_exec)
        plt.title(
            "q = {0}, time = {1:.2f}sec, num_gen = {2}".format(q, time_exec, num_gen))
        plt.figure(1)
        plt.plot(resultLog)
        plt.grid(True)
        plt.xlabel("iteration")
        plt.ylabel("Fitness")
        plt.show()

