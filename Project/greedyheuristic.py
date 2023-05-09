import copy

'''graph clearing problem with a greedy heuristic! by Mril and Andrew'''


#How is the Greedy Heuristic gonna work?

'''
1. we will start with an empty set of cycles,
2. we will find the biggest element in the matrix (highest weight edge)
3. & then repeatedly add the cycle which includes the edge of the highest weight
   and which does not conflict with any of the cycles that have already been added.

This heuristic will always find a feasible solution,
but it will not always find an optimal solution.

'''

#function that finds the optimal 2 or 3 length cycle given an edge (defined by its start and end node)
#returns a tuple of the form (path, total_weight) where path is a list of nodes visited in order by number
#   ex) ([0, 1, 2, 0], 20)
def find_best_cycle(startnode, endnode, adj_matrix):
    found_cycles = []
    
    #check 2-cycle
    if (adj_matrix[endnode][startnode] > 0):
        found_cycles.append((adj_matrix[startnode][endnode] + adj_matrix[endnode][startnode], [startnode, endnode, startnode]))
    
    #look at possible nodes for 3-cycle
    for node in range(len(adj_matrix[endnode])):
        if (adj_matrix[endnode][node] > 0 and adj_matrix[node][startnode] > 0):
            found_cycles.append((adj_matrix[startnode][endnode] + adj_matrix[endnode][node] + adj_matrix[node][startnode], [startnode, endnode, node, startnode]))
    
    #select best cycle
    if (len(found_cycles) > 0):
        return max(found_cycles, key = lambda item:item[0])
    else:
        return (0, [])

#function should iterate through the adjacency matrix and find the largest edge
def find_max_edge(adj_matrix):
    max_edge = 0
    max_nodes = []

    for row in range(len(adj_matrix)):
        for col in range(len(adj_matrix[0])):
            if (adj_matrix[row][col] > max_edge):
                max_edge = adj_matrix[row][col]
                max_nodes = [row, col]
    
    return (max_edge, max_nodes)

#function should modify adjacency matrix to exclude nodes
def delete_nodes(graph, path):
    for node in path:
        for i in range(len(graph)):
            graph[node][i] = 0
            graph[i][node] = 0

def to_tuple(graph):
    total_weight = 0
    cycle_set = []

    for cycle in graph:
        total_weight += cycle[0]
        cycle_set.append(cycle[1])

    return (total_weight, cycle_set)

#main graph clear function (incomplete)
def GraphClear(adj_matrix):
    graph = copy.deepcopy(adj_matrix)
    graph_covering = []

    max_edge = find_max_edge(graph)
    
    #should select cycles out of the graph according to the largest weights until there are no cycles left
    while (max_edge[0] > 0):
        new_cycle = find_best_cycle(max_edge[1][0], max_edge[1][1], graph)
        
        if (new_cycle[0] > 0):
            graph_covering.append(new_cycle)
            delete_nodes(graph, graph_covering[-1][1])
        else:
            graph[max_edge[1][0]][max_edge[1][1]] = 0

        max_edge = find_max_edge(graph)
        
    return to_tuple(graph_covering)

    
