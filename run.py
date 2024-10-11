# Search methods

import search
import time

ab = search.GPSProblem('A', 'B'
                       , search.romania)
print(search.breadth_first_graph_search(ab).path(mode_extended=False))
print(search.depth_first_graph_search(ab).path(mode_extended=False))

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
