# PROJECT
# BRUTE FORCE GRAPH CLEARING

matrix = [
	    [0, 2, 12, 0, 0, 0],
	    [0, 0, 0, 10, 3, 1],
	    [0, 0, 0, 5, 0, 0],
	    [3, 0, 0, 0, 2, 0],
	    [0, 0, 0, 0, 0, 10],
            [0, 3, 7, 0, 0, 0]
	]

cycles = []


def graphclear_helper(adjmat):
    for _i in range(len(adjmat)):
        for _j in range(len(adjmat)):
            c = [_i]
            graphclear(adjmat, _i, _j, c )

def graphclear(adjmat, i, j, cycle):
    #print("i: ", i)
    #print("j: ", j)
    #print("cycle: ", cycle)
    if adjmat[i][j] != 0:
        if len(cycle) > 1 and j == cycle[0]:
            temp = cycle.copy()
            temp.append(j)
            if temp not in cycles:
                cycles.append(temp)
            for _j in range(j+1, len(adjmat), 1):
                graphclear(adjmat, i, _j, cycle)
        elif j not in cycle and j != cycle[0]:
            cycle.append(j)
            for k in range(len(adjmat)):
                graphclear(adjmat, j, k, cycle)


def total_w(adjmat, c):
    totalweight = 0
    #print(c)
    for i in c:
        for j in range(len(i)-1):
            totalweight+= adjmat[i[j]][i[j+1]]
    return totalweight



def viable(c_list):
    v = True
    if len(c_list) < 2:
        v = False
        return v
    else:
        if len(c_list) == 2:
            a = set(c_list[0])
            b = set(c_list[1])
            if not(a.isdisjoint(b)):
                v = False
                #print(c_list)
                #print("v: ", v)
                return v
        elif len(c_list) == 3:
            a = set(c_list[0])
            b = set(c_list[1])
            c = set(c_list[2])
            if not(a.isdisjoint(b) and a.isdisjoint(c) and c.isdisjoint(b)):
                v = False
                #print(c_list)
                #print("v: ", v)
                return v
    return v




combos = []
def bin(c):
    b = [-1, -1, -1]
    b1 = [len(c)-1, len(c)-1, len(c)-1]
    #print(b1)
    t = []
    while b != b1:
        for i in range(len(b)-1,-1,-1):
            if b[i] != len(c)-1:
                b[i]+= 1
                #print("b: ", b)
                for x in range(3):
                    if b[x] != -1 not in b and cycles[b[x]] not in t:
                        t.append(cycles[b[x]])
                    _t = t.copy()
                        #print(t)
                if (len(_t) > 1) and (viable(_t)) and (_t not in combos):
                    #print(_t)
                    combos.append(_t)
                if len(t) == 3:
                    t = []
                break
            else:
                b[i] = 0
                #print("b: ", b)
                for x in range(3):
                    if b[x] != -1 and cycles[b[x]] not in t:
                        t.append(cycles[b[x]])
                    _t = t.copy()
                        #print(t)
                if len(_t) > 1 and viable(_t) and (_t not in combos):
                    #print(_t)
                    combos.append(_t)
                if len(t) == 3:
                    t = []



def optimal(adjmat, com):
    largest = 0
    opt = []
    for i in com:
        z = total_w(adjmat, i)
        if z > largest:
            largest = z
            opt = i
    return opt, largest

graphclear_helper(matrix)
#print(cycles)
#print(viable(t))
bin(cycles)
print(combos)
#print(len(cycles))
#print(total_w(matrix, cycles[0]))
print("optimal: ", optimal(matrix, combos))
