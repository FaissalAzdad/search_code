# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
al = search.GPSProblem('A', 'L', search.romania)
fc = search.GPSProblem('F', 'C', search.romania)

print search.breadth_first_graph_search(ab).path()
print search.depth_first_graph_search(ab).path()
#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()
print search.branch_and_bound_graph_search(ab).path()
print search.branch_and_bound_with_underestimation(ab).path()
print search.branch_and_bound_graph_search(fc).path()
print search.branch_and_bound_with_underestimation(fc).path()


#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
