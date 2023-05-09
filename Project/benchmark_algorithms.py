import greedyheuristic as greedy
import bruteforce as bruteforce
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import multiprocessing
from multiprocessing import Queue


CONNECTION_PROB = 1
TIMEOUT = 900
NORMAL_STEP = 5
GREEDY_STEP = 100

def brute_wrapper(queue, graph):
    result = bruteforce.GraphClear(graph)
    queue.put(result)
    queue.close()

def greedy_wrapper(queue, graph):
    result = greedy.GraphClear(graph)
    queue.put(result)
    queue.close()

#Graphs are connected with a 60% chance with a weight from 1 to 100
def generateRandomGraph(numNodes: int) -> list:
    graph = []
    
    for i in range(numNodes):
        graph.append([])
        for j in range(numNodes):
            if (i == j):
                graph[i].append(0)
            else:
                if (random.random() < CONNECTION_PROB):
                    graph[i].append(random.sample(range(1, 100),1)[0])
                else:
                    graph[i].append(0)
    
    return graph

def testAlgorithms(n, timePerSizeBrute, timePerSizeGreedy, bestPathBrute, bestPathGreedy):
    timeElapsedBrute = 0
    timeElapsedGreedy = 0
    while (timeElapsedBrute < TIMEOUT or timeElapsedGreedy < TIMEOUT):
        curr_graph = generateRandomGraph(n)
        print(n)
        
        if (timeElapsedBrute < TIMEOUT):
            
            queue = multiprocessing.Queue()
            proc = multiprocessing.Process(target=brute_wrapper, args=(queue, curr_graph))
            proc.start()

            try:
                sol = queue.get(True, TIMEOUT)
            except:
                sol = None
            finally:
                proc.terminate()
            
            if (sol != None):
                start = time.time()
                sol = bruteforce.GraphClear(curr_graph)
                end = time.time()

                print("Finished Brute Force")

                timeElapsedBrute = end - start
                timePerSizeBrute.append(timeElapsedBrute)
                bestPathBrute.append(sol)
            else:
                timeElapsedBrute = float('inf')

        if (timeElapsedGreedy < TIMEOUT):
            
            queue = multiprocessing.Queue()
            proc = multiprocessing.Process(target=greedy_wrapper, args=(queue, curr_graph))
            proc.start()

            try:
                sol = queue.get(True, TIMEOUT)
            except:
                sol = None
            finally:
                proc.terminate()

            if (sol != None):
                start = time.time()
                sol = greedy.GraphClear(curr_graph)
                end = time.time()

                print("Finished Greedy")

                timeElapsedGreedy = end - start
                timePerSizeGreedy.append(timeElapsedGreedy)
                bestPathGreedy.append(sol)
            else:
                timeElapsedGreedy = float('inf')

        if (timeElapsedBrute < TIMEOUT):
            n += NORMAL_STEP
        elif (timeElapsedGreedy < TIMEOUT):
            n += GREEDY_STEP

    return n

if __name__ == '__main__':
    n = 2
    timePerSizeBrute = []
    timePerSizeGreedy = []
    bestPathBrute = []
    bestPathGreedy = []
    
    n = testAlgorithms(n, timePerSizeBrute, timePerSizeGreedy, bestPathBrute, bestPathGreedy)

    #Remaining code is adapted from Professor Bailey
    x_data_brute = list(range(2, len(timePerSizeBrute) + 2, NORMAL_STEP))
    x_data_greedy = list(range(2, len(timePerSizeBrute) + 2, NORMAL_STEP))
    y_data_brute = timePerSizeBrute
    y_data_greedy = timePerSizeGreedy[:len(x_data_greedy)]

    plt.plot(x_data_brute, y_data_brute, linestyle='-', marker='o', label = "Brute Force Algorithm")
    plt.plot(x_data_greedy, y_data_greedy, linestyle='-', marker='o', label = "Greedy Algorithm")
    plt.legend()
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title('Time Elapsed Per Input Size: Brute Force vs. Greedy')
    fig = plt.gcf() # In order to save, this line MUST be in the same cell as plt.plot()!

    # If you wish to save the figure
    fig.savefig('project_time_graph_both.png')

    plt.clf()

    #Remaining code is adapted from Professor Bailey
    x_data_greedy = list(range(2, len(timePerSizeBrute) + 2, NORMAL_STEP)) + list(range(len(timePerSizeBrute) + 2, n, GREEDY_STEP))
    y_data_greedy = timePerSizeGreedy

    plt.plot(x_data_greedy, y_data_greedy, linestyle='-', marker='o', label = "Greedy Algorithm")
    plt.legend()
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title('Time Elapsed Per Input Size: Greedy')
    fig = plt.gcf() # In order to save, this line MUST be in the same cell as plt.plot()!

    # If you wish to save the figure
    fig.savefig('project_time_graph_greedy.png')

