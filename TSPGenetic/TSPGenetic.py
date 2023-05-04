import matplotlib.pyplot as plt
import numpy as np
import random

def determine_fitness(tour):
    total = 0
    for i in tour:
        if (i == len(tour) - 1):
            total += np.linalg.norm(tour[i]-tour[0])
        else:
            total += np.linalg.norm(tour[i]-tour[i+1])   
    return total     

num_cities = int(input("Enter a number of cities:"))
num_generations = int(input("Enter a number of generations:"))
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

print(cities)
print(curr_generation[0])
print(curr_fitness[0])    

x_data = range(generation_size)
y_data = curr_fitness

# labels = ['First column description', 'Second column description']
labels = ['tours', 'fitness']

plt.plot(x_data, y_data, linestyle='-', marker='o')
plt.legend(labels)
plt.xlabel('Generation number ($N$)')
plt.ylabel('Total Tour Distance')
plt.title('Solution Quality over Time')
fig = plt.gcf() # In order to save, this line MUST be in the same cell as plt.plot()!

# If you wish to save the figure
fig.savefig('descriptive_file_name.png')