# Search methods

import search
import time

ab = search.GPSProblem('A', 'B'
                       , search.romania)
print(search.breadth_first_graph_search(ab).path(mode_extended=False))
print("--------")
print(search.depth_first_graph_search(ab).path(mode_extended=False))
print("--------")
print(search.branch_and_bound_search(ab, cuality=False).path(mode_extended=False))
print("--------")
print(search.branch_and_bound_search(ab, cuality=True).path(mode_extended=False))
print("--------")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
