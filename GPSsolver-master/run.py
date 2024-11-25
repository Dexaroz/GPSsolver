# Search methods

import search

id = int(input("¿Qué camino desea ejecutar?"))
if id == 1:
    ab = search.GPSProblem('A', 'B'
                           , search.romania)

    print(search.breadth_first_graph_search(ab).path(mode_extended=False))
    print("--------")

    print(search.depth_first_graph_search(ab).path(mode_extended=False))
    print("--------")

    print(search.branch_and_bound_search(ab, cuality=False).path(mode_extended=False))
    print("--------")

    print(search.branch_and_bound_search_with_subestimation(ab, search.romania.locations).path(mode_extended=False))
elif id == 2:
    oe = search.GPSProblem('O', 'E'
                           , search.romania)
    print("BFS")
    print(search.breadth_first_graph_search(oe).path(mode_extended=False))
    print("--------")

    print("DFS")
    print(search.depth_first_graph_search(oe).path(mode_extended=False))
    print("--------")

    print("B&B")
    print(search.branch_and_bound_search(oe, cuality=False).path(mode_extended=False))
    print("--------")

    print("B&B with subestimation")
    print(search.branch_and_bound_search_with_subestimation(oe, search.romania.locations).path(mode_extended=False))
elif id == 3:
    gz = search.GPSProblem('G', 'Z'
                           , search.romania)
    print("BFS")
    print(search.breadth_first_graph_search(gz).path(mode_extended=False))
    print("--------")

    print("DFS")
    print(search.depth_first_graph_search(gz).path(mode_extended=False))
    print("--------")

    print("B&B")
    print(search.branch_and_bound_search(gz, cuality=False).path(mode_extended=False))
    print("--------")

    print("B&B with subestimation")
    print(search.branch_and_bound_search_with_subestimation(gz, search.romania.locations).path(mode_extended=False))
elif id == 4:
    nd = search.GPSProblem('N', 'D'
                           , search.romania)
    print("BFS")
    print(search.breadth_first_graph_search(nd).path(mode_extended=False))
    print("--------")

    print("DFS")
    print(search.depth_first_graph_search(nd).path(mode_extended=False))
    print("--------")

    print("B&B")
    print(search.branch_and_bound_search(nd, cuality=False).path(mode_extended=False))
    print("--------")

    print("B&B with subestimation")
    print(search.branch_and_bound_search_with_subestimation(nd, search.romania.locations).path(mode_extended=False))
elif id == 5:
    mf = search.GPSProblem('M', 'F'
                           , search.romania)
    print("BFS")
    print(search.breadth_first_graph_search(mf).path(mode_extended=False))
    print("--------")

    print("DFS")
    print(search.depth_first_graph_search(mf).path(mode_extended=False))
    print("--------")

    print("B&B")
    print(search.branch_and_bound_search(mf, cuality=False).path(mode_extended=False))
    print("--------")

    print("B&B with subestimation")
    print(search.branch_and_bound_search_with_subestimation(mf, search.romania.locations).path(mode_extended=False))

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
