#Ellie Dunham
import numpy as np


def GraphClear(graph,max_cycle_length):
    num_nodes = len(graph)

    #finding all cycles of up to max cycle length
    cycle = []
    all_cycles=[]
    for node in range(num_nodes):
        for length in range(2,max_cycle_length+1):
            cycle.append(node)
            all_cycles +=(findCycles(node,graph,[],cycle,length))
            cycle = []
        
   
    # removing same cycles, compare all the cycles
    no_duplicates = remove_cycles(all_cycles)
                    
   
    
    #determine all valid combos of cycles
    cycle_combos = get_cycle_combinations(no_duplicates)

 
    #determine which combo yields best weight
    max_weight = 0
    for combo in cycle_combos:
        combo_weight= 0
        for cycle in combo:
            combo_weight += get_cycle_weight(cycle,graph)
        if combo_weight > max_weight:
            max_combo = combo
            max_weight = combo_weight
    
            
   
    return max_weight,max_combo

def get_cycle_combinations(all_cycles):
    combination = np.zeros(len(all_cycles))
    combos = []
    while(combination !="done"):
        combo =[]
        for i in range(len(combination)):
            if combination[i] ==1:
                combo.append(all_cycles[i])

        #checking that the combination doesn't include duplicate nodes in the cycles
        include = True
        for i in range(len(combo)):
            for j in range(i+1,len(combo)):
                for k in combo[i]:
                    if k in combo[j]:
                        include = False
                        break
            if include == False:
                break
        if include:
            combos.append(combo)
                    
        
        combination = getNewCombination(combination)
    return combos

def getNewCombination(old_combo):
#function to determine the next combination based on the old combo
    left_one = getLeftMostOne(old_combo)
    right_zero = getRightMostZero(old_combo)
    right_one = getRightMostOne(old_combo, left_one)
    if right_one == "none":
        right_one = left_one
    
    #check that if number is not returned!!
    if right_zero == "none":
        return "done"
    elif left_one == "none":
        old_combo[right_zero]=1

    #checking if there is only one 1 on the board
    elif right_one == left_one:
    #checks if the zero is before the one, which means
        #1 needs to replace it and set all other 1's to zero
        if right_zero < left_one:
            old_combo[right_zero]=1
            for i in range(left_one, len(old_combo)):
                old_combo[i]=0
        else:
            old_combo[right_zero]=1
    elif right_one > right_zero:
        old_combo[right_zero]=1
        for i in range(right_zero+1,len(old_combo)):
            old_combo[i]=0
        
    else:
        old_combo[right_zero]=1
        for i in range(right_zero+1,right_one):
            old_combo[i]=0

    return old_combo

def getRightMostZero(combo):
#function that returns the position of rightmost 0 
    for i in range(len(combo)-1,-1,-1):
        if int(combo[i])==0:
            return i
    return "none"
def getRightMostOne(combo,left):
#function that returns the position of the rightmost 1
    for i in range(len(combo)-1,-1,-1):
        if int(combo[i])==1:
            if(i != left):
                return i
    return "none"
    
def getLeftMostOne(combo):
#function that returns the position of leftmost 1 
    for i in range(len(combo)):
        if int(combo[i])==1:
            return i
    return "none"

def get_cycle_weight(cycle,graph):
    weight= 0
    for i in range(len(cycle)-1):
        weight += graph[cycle[i]][cycle[i+1]]


    return weight              

def remove_cycles(all_cycles):
#function which filters out the duplicate cycles
    keep_cycles =[]
    for cycle_a in range(len(all_cycles)):
        keep = True
        for cycle_b in range(len(keep_cycles)):
            if len(keep_cycles[cycle_b]) == len(all_cycles[cycle_a]):
                j=0
                for i in range(len(all_cycles[cycle_a])):
                    if all_cycles[cycle_a][i] in keep_cycles[cycle_b]:
                        j+=1
                if j==len(all_cycles[cycle_a]):
                    keep = False
        if keep:
            keep_cycles.append(all_cycles[cycle_a])

    return keep_cycles

#recursive to find cycles
#maximum length of cycle will be length_cycle
def findCycles(curr_node,graph, cycles,cycle,length_cycle):
  
    num_nodes = len(graph)
   
    if len(cycle) == length_cycle:
        #check that the last node returns to the starting node
        if graph[cycle[length_cycle-1]][cycle[0]] != 0:
            #cycle is valid
            cycles.append(cycle)
                     
    else:
        for next_node in range(num_nodes):
            if graph[curr_node][next_node] != 0:
                if next_node not in cycle:
                    cycle.append(next_node)
                    hold_cycle = cycle.copy()
                    cycles = findCycles(next_node, graph, cycles, cycle, length_cycle)
                    cycle = hold_cycle[:len(hold_cycle)-1]
             

    return cycles   
        
def main():
    graph = [[0,2,12,0,0,0],
             [0,0,0,10,3,1],
             [0,0,0,5,0,0],
             [3,0,0,0,2,0],
             [0,0,0,0,0,10],
             [0,3,7,0,0,0]]
    
    print(GraphClear(graph,3))

main()
