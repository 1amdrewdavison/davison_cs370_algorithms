'''graph clearing problem with a greedy heuristic! by Mril'''


#How is the Greedy Heuristic gonna work?

'''
1. we will start with an empty set of cycles,
2. we will find the biggest element in the matrix (highest weight edge)
3. & then repeatedly add the cycle which includes the edge of the highest weight the highest weight
   and which does not conflict with any of the cycles that have already been added.

This heuristic will always find a feasible solution,
but it will not always find an optimal solution.

'''

def max_weight_cycle(G):
    n = len(G)
    max_edge_weight = 0
    max_edge = None
    
    #Being greedy and finding the edge with the maximum weight
    for i in range(n):
        for j in range(n):
            if G[i][j] > max_edge_weight:
                max_edge_weight = G[i][j]
                max_edge = (i, j)

    if max_edge_weight == 0:
        return [], 0
    
    #print(max_edge_weight)
    #print(max_edge)
    
    # Initializing start vertex and max weight edges list
    start_vertex = max_edge[0]
    max_weight_edges = [max_edge]
    visited = [False] * n
    visited[start_vertex] = True
    stack = [(start_vertex, [start_vertex], 0)]
    
    #Perform DFS to find complete cycle
    while stack:
        curr_vertex, path, total_weight = stack.pop()
        for neighbor in range(n):
            if G[curr_vertex][neighbor] > 0:
                # If neighbor is the start vertex, we complete & return the cycle
                if neighbor == start_vertex:
                    cycle_weight = total_weight + G[curr_vertex][neighbor]
                    cycle_path = path + [start_vertex]
                    if max_edge_weight in [G[cycle_path[i]][cycle_path[i+1]] for i in range(len(cycle_path)-1)]:
                        return cycle_path, cycle_weight
                    else:
                        continue
                
                if not visited[neighbor] or neighbor == max_edge[0]:
                    visited[neighbor] = True
                    new_path = path + [neighbor]
                    new_weight = total_weight + G[curr_vertex][neighbor]
                    stack.append((neighbor, new_path, new_weight))
                    
                    # Update max weight edges if a new edge with higher weight is found
                    if G[curr_vertex][neighbor] > max_edge_weight:
                        max_edge_weight = G[curr_vertex][neighbor]
                        max_weight_edges = [(curr_vertex, neighbor)]
                    elif G[curr_vertex][neighbor] == max_edge_weight:
                        max_weight_edges.append((curr_vertex, neighbor))
        '''
        Still working on this:
        
        #If the stack is empty and there are still edges with max weight, use them as start vertex
        if not stack and max_weight_edges:
            max_weight_edge = max_weight_edges.pop()
            new_start_vertex = max_weight_edge[1]
            visited = [False] * n
            visited[new_start_vertex] = True
            stack = [(new_start_vertex, [new_start_vertex], 0)]
        '''
            
    return [], 0



def main():
    G = [[0,2,12,0,0,0],
    [0,0,0,10,3,1],
    [0,0,0,5,0,0],
    [3,0,0,0,2,0],
    [0,0,0,0,0,10],
    [0,3,7,0,0,0]]
    
    all_cycles = []
    no_cycles = 0
    total_weight = 0
    
    max_cycle_and_weight = ()
    while True:
        max_cycle_and_weight = max_weight_cycle(G)        
        
        #stopping the loop when we are finding unproductive cycles
        if max_cycle_and_weight[1] == 0:
            break
        
        #stopping the loop when we have reached the limit of 3 cycles
        if no_cycles == 3:
            break
        
        else:
            #print(max_weight_cycle(G))
            curr_cycle = max_cycle_and_weight[0]
            all_cycles.append(curr_cycle)
            no_cycles += 1
            
            total_weight += max_cycle_and_weight[1]
            for i in range(len(curr_cycle) - 1):
                for j in range(len(G)):
                    G[curr_cycle[i]][j] = 0
                    G[j][curr_cycle[i]] = 0
                
            #print(G)

        
    print("The cycles: (grouped by vertices): ", all_cycles)
    print("Total weight: ",total_weight)
    print("Number of cycles generated",no_cycles)  


main()


    
