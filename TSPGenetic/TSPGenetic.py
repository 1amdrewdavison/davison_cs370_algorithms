#Written by Andrew Davison for CSC 370: Design and Analysis of Algorithms for Programming Homework 4
#Interactively intakes a number of cities for TSP and a number of generations to run a genetic algorithm

import matplotlib.pyplot as plt
import numpy as np
import random

#Take inputs as constansts first
num_cities = int(input("Enter a number of cities:"))
num_generations = int(input("Enter a number of generations:"))
generation_size = 100

#Determines length of a path given a tour and city locations
def determine_fitness(tour, cities):
    total = 0.0
    for i in range(num_cities):
        if (i == len(tour) - 1):
            total += np.linalg.norm(cities[tour[i]]-cities[tour[0]])
        else:
            total += np.linalg.norm(cities[tour[i]]-cities[tour[i+1]])   
    return total   

#Generates children given two parents
def make_child(parent1, parent2, cities):
    #Choose a random starting vertex
    start_vertex = random.sample(range(num_cities),1)[0]
    
    child = []
    child.append(start_vertex)
    
    #Fill out the rest of the tour
    for i in range(1, num_cities):
        p1_next_vertex = parent1[(parent1.index(start_vertex) + 1) % num_cities]
        p2_next_vertex = parent2[(parent2.index(start_vertex) + 1) % num_cities]
        p1_edge = np.linalg.norm(cities[start_vertex] - cities[p1_next_vertex])
        p2_edge = np.linalg.norm(cities[start_vertex] - cities[p2_next_vertex])
        
        #Add the next shortest edge that is in the tour of the parents
        if (p1_edge > p2_edge and not p2_next_vertex in child):
            start_vertex = p2_next_vertex
            child.append(p2_next_vertex)
        elif (not p1_next_vertex in child):
            start_vertex = p1_next_vertex
            child.append(p1_next_vertex)
        else:
            #If both of the next possible vertices are already in the tour, randomly choose the next one
            next_vertex = random.sample(list(set(range(num_cities)).difference(set(child))), 1)[0]
            start_vertex = next_vertex
            child.append(next_vertex)
        
    return child
  
#This code from Professor Bailey

# Create a NumPy random generator object
rng = np.random.default_rng() 

# Create an array of random cities
cities = rng.normal(0, 1, (num_cities, 2))
    
#End Professor Bailey code

curr_generation = []
curr_fitness = []
best_fits = []

#Randomly generate first generation
for i in range(generation_size):
    curr_generation.append(random.sample(range(num_cities), num_cities))
    curr_fitness.append(determine_fitness(curr_generation[-1], cities))

#Add the best tour of that generation
best_fits.append(sorted(curr_fitness)[0])

#run genetic algorithm
for i in range(1, num_generations):
    #grab the indexes of the top 50% most fit
    best_tours = sorted(range(len(curr_fitness)), key=lambda i: curr_fitness[i])[:(int)(generation_size/2)]
    parent_pool = []
    
    #insert parents into pool
    for i in best_tours:
        parent_pool.append(curr_generation[i])
        parent_pool.append(curr_generation[i])
        parent_pool.append(curr_generation[i])
        parent_pool.append(curr_generation[i])
    
    #make next generation
    curr_generation = []
    curr_fitness = []
    while (parent_pool):
        parents = random.sample(parent_pool, 2)
        parent_pool.remove(parents[0])
        parent_pool.remove(parents[1])
        child = make_child(parents[0], parents[1], cities)
        curr_generation.append(child)
        curr_fitness.append(determine_fitness(child, cities))
    
    #Track the best solution of this generation
    best_fits.append(sorted(curr_fitness)[0])

#Output best tour weight
print("Best fit path weight:", best_fits[-1])

#Remaining code is adapted from Professor Bailey

x_data = range(num_generations)
y_data = best_fits

labels = ['Best Tour in Generation']

plt.plot(x_data, y_data, linestyle='-', marker='o')
plt.legend(labels)
plt.xlabel('Generation number ($N$)')
plt.ylabel('Total Tour Distance')
plt.title('Solution Quality over Time')
fig = plt.gcf() # In order to save, this line MUST be in the same cell as plt.plot()!

# If you wish to save the figure
fig.savefig('genetic_tsp_solutions_over_time_AndrewDavison.png')