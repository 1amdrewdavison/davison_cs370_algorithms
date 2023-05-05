import matplotlib.pyplot as plt
import numpy as np
import random

num_cities = int(input("Enter a number of cities:"))
num_generations = int(input("Enter a number of generations:"))
generation_size = 100

def determine_fitness(tour, cities):
    total = 0.0
    for i in tour:
        if (i == len(tour) - 1):
            total += np.linalg.norm(cities[i]-cities[0])
        else:
            total += np.linalg.norm(cities[i]-cities[i+1])   
    return total   

def make_child(parent1, parent2, cities):
    start_vertex = random.sample(range(num_cities),1)[0]
    
    child = []
    child.append(start_vertex)
    
    for i in range(1, num_cities):
        p1_next_vertex = parent1[(parent1.index(start_vertex) + 1) % num_cities]
        p2_next_vertex = parent2[(parent2.index(start_vertex) + 1) % num_cities]
        p1_edge = np.linalg.norm(cities[start_vertex] - cities[p1_next_vertex])
        p2_edge = np.linalg.norm(cities[start_vertex] - cities[p2_next_vertex])
        
        if (p1_edge > p2_edge and not p2_next_vertex in child):
            start_vertex = p2_next_vertex
            child.append(p2_next_vertex)
        elif (not p1_next_vertex in child):
            start_vertex = p1_next_vertex
            child.append(p1_next_vertex)
        else:
            next_vertex = random.sample(list(set(range(num_cities)).difference(set(child))), 1)[0]
            start_vertex = next_vertex
            child.append(next_vertex)
        
    return child
  
# Create a NumPy random generator object
rng = np.random.default_rng() 

# Create an array of random cities
cities = rng.normal(0, 1, (num_cities, 2))
    
curr_generation = []
curr_fitness = []
best_fits = []

#Randomly generate first generation
for i in range(generation_size):
    curr_generation.append(random.sample(range(num_cities), num_cities))
    curr_fitness.append(determine_fitness(curr_generation[-1], cities))

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
        
    best_fits.append(sorted(curr_fitness)[0])

print("Best fit path weight:", best_fits[-1])

x_data = range(num_generations)
y_data = best_fits

# labels = ['First column description', 'Second column description']
labels = ['improvement']

plt.plot(x_data, y_data, linestyle='-', marker='o')
plt.legend(labels)
plt.xlabel('Generation number ($N$)')
plt.ylabel('Total Tour Distance')
plt.title('Solution Quality over Time')
fig = plt.gcf() # In order to save, this line MUST be in the same cell as plt.plot()!

# If you wish to save the figure
fig.savefig('descriptive_file_name.png')