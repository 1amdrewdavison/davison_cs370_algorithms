import matplotlib.pyplot as plt
import numpy as np
import random

def determine_fitness(tour):
    total = 0
    for i in tour:
        total += np.linalg.norm(tour[i]-tour[i+1])   
    return total     

num_cities = input("Enter a number of cities:")
num_generations = input("Enter a number of generations:")
generation_size = 100

# Create a NumPy random generator object
rng = np.random.default_rng(seed=42) 
# ^^ Set seed to 42, for repeatability when testing. Remove when debugging is complete

# Create an array of random cities
cities = rng.normal(0, 1, (num_cities, 2))
    
curr_generation = []
curr_fitness = []

#Randomly generate first generation
for i in range(generation_size):
    curr_generation.append(random.sample(range(num_cities), num_cities))
    curr_fitness.append(determine_fitness(curr_generation[-1]))
    

#for i in range(num_generations):
    

x_data = [5, 10, 20, 50]
y_data = [[1, 2], 
           [2, 4], 
           [3, 6], 
           [4, 8]]
# ^^ You do NOT need to plot the performance on multiple city sizes for this 
# assignment, but it may be useful for the technical report of your final Project.

# labels = ['First column description', 'Second column description']
labels = ['$100$ cities', '$20$ cities']

plt.plot(x_data, y_data, linestyle='-', marker='o')
plt.legend(labels)
plt.xlabel('Generation number ($N$)')
plt.ylabel('Total Tour Distance')
plt.title('Solution Quality over Time')
plt.ylim(0, 25)
fig = plt.gcf() # In order to save, this line MUST be in the same cell as plt.plot()!

# If you wish to save the figure
fig.savefig('descriptive_file_name.png')