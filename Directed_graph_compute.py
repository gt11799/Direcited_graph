#!/usr/bin/env python
'''
There are three functions, all about the direct graph
'''
#define three graph to test the function
EX_GRAPH0 = {0:set([1,2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([0]), 4:set([1]), 
        5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 4:set([1]), 
        5:set([2]), 6:set([]), 7:set([3]), 8:set([1,2]), 9:set([0,3,4,5,6,7])}
        
        
def make_complete_graph(num_nodes):
    '''
    Takes the number of nodes num_nodes and returns a dictionary corresponding
    to a complete directed graph with specified number of nodes.
    '''
    try:
        num_nodes = int(num_nodes)
    except(ValueError, TypeError):
        print('Error! Only integer accepted')
        return
    
    nodes = range(num_nodes)
    graph = dict([])
    for node in nodes:
        temp = list(nodes)
        temp.remove(node)
        graph[node] = set(temp)
        
    return graph
    
def compute_in_degrees(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) and computes the indegrees
    for the nodes in the graph.
    The function return a dictionary with the same set of keys whose corresponding values 
    are the number of edges whose head matches a particular node.
    '''
    try:
        digraph = dict(digraph)
    except(ValueError, TypeError):
        print('Error! Only dict accepted')
        return
        
    degrees = dict([])
    for node in digraph:
        degree = 0
        for value in digraph.values():
            if node in value:
                degree += 1
        degrees[node] = degree
        
    return degrees
    
def in_degree_distribution(digraph):
    '''
    Takes a directed graph (represented as a dictionary) and computes the in-degree for the
    nodes in the graph. 
    The function return a dictionary whose keys correspond to in-degrees of nodes in the graph,
    the value associated with each particular in-degree is the number of nodes with that in-degree.
    '''
    degrees = compute_in_degrees(digraph)
    distribution = dict([])
    values = degrees.values()
    for value in values:
        distribution[value] = values.count(value)
        
    return distribution
        
        
def test():
    'test the above functions'
    #for i in range(4,6):
    #    print(" num_nodes: %s, the graph is: %s" %(i, make_complete_graph(i)))
    #for i in ['a', '5.44', 9.77, [9, 8]]:
    #    print(" num nodes: %s, the graph is: %s" %(i, make_complete_graph(i)))
    for digraph in ['EX_GRAPH0', 'EX_GRAPH1', 'EX_GRAPH2']:
        print('%s in_degrees is: %s\n in_degrees_distribution is %s' %(digraph, compute_in_degrees(eval(digraph)),
            in_degree_distribution(eval(digraph))))
        
#test()
        

        
