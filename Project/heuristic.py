#function that finds the optimal 2 or 3 length cycle given an edge (defined by its start and end node)
#returns a tuple of the form (path, total_weight) where path is a list of nodes visited in order by number
#   ex) ([0, 1, 2, 0], 20)
def find_best_cycle(startnode, endnode, adj_matrix):
    found_cycles = []
    
    #check 2-cycle
    if (adj_matrix[endnode][startnode] < float('inf')):
        found_cycles.append(([startnode, endnode, startnode], adj_matrix[startnode][endnode] + adj_matrix[endnode][startnode]))
    
    #look at possible nodes for 3-cycle
    for node in range(len(adj_matrix[endnode])):
        if (adj_matrix[endnode][node] < float('inf') and adj_matrix[node][startnode] < float('inf')):
            found_cycles.append(([startnode, endnode, node, startnode], adj_matrix[startnode][endnode] + adj_matrix[endnode][node] + adj_matrix[node][startnode]))
    
    #select best cycle
    if (len(found_cycles) > 0):
        return max(found_cycles, key = lambda item:item[1])
    else:
        return 0

#function should iterate through the adjacency matrix and find the largest (non-infinite) edge
def find_max_edge(adj_matrix):
    return 0

#function should modify adjacency matrix to exclude nodes
def delete_nodes(graph, *nodes):
    return graph

#main graph clear function (incomplete)
def graph_clear(adj_matrix):
    graph = adj_matrix.copy()
    max_edge = find_max_edge(graph)
    graph_covering = []
    
    #should select cycles out of the graph according to the largest weights until there are no cycles left
    while (max_edge > 0):
        graph_covering.append(find_best_cycle)
        #delete nodes
        max_edge = find_max_edge(graph)
        
    return graph_covering
    
#example adjacency matrix
adj_matrix = [[float('inf'), 2, 12, float('inf'), float('inf'), float('inf')],
              [float('inf'), float('inf'), float('inf'), 10, 3, 1],
              [float('inf'), float('inf'), float('inf'), 5, float('inf'), float('inf')],
              [3, float('inf'), float('inf'), float('inf'), 2, float('inf')],
              [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 10],
              [float('inf'), 3, 7, float('inf'), float('inf'), float('inf')]]

#shows example of find_best_cycle
print(find_best_cycle(0, 2, adj_matrix))