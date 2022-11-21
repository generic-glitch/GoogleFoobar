# Credit for Dijkstra's algorithm: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html

class Graph:
  def __init__(self, nodes, init_graph):
    self.nodes = nodes
    self.graph = self.construct_graph(nodes, init_graph)
  def construct_graph(self, nodes, init_graph):
    graph = {}
    for node in nodes:
      graph[node] = {}
    graph.update(init_graph)
    for node, edges in graph.items():
      for adjacent_node, value in edges.items():
        if graph[adjacent_node].get(node, False) == False:
          graph[adjacent_node][node] = value
    return graph
  def get_nodes(self):
    return self.nodes
  def get_outgoing_edges(self, node):
    connections = []
    for out_node in self.nodes:
      if self.graph[node].get(out_node, False) != False:
        connections.append(out_node)
    return connections
  
  def value(self, node1, node2):
    return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}
    max_value = float("inf")
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
        unvisited_nodes.remove(current_min_node)
    return previous_nodes, shortest_path

import copy
import itertools
# Need to use Dijkstra's Shortest Path Algorithm
def solution(map):
  # Due to python's chr function, we use 97
  rows = [chr(index) for index in range(97, (97+getSize(map)[1]))]
  cols = [str(index) for index in range(getSize(map)[0])]
  nodes = [col+row for (col,row) in itertools.product(rows, cols)]
  walls = [(col*500)+1 for row in map for col in row]
  paths = []
  for i, weight in enumerate(walls):
    if weight > 500:
      removedWall = copy.deepcopy(walls)
      removedWall[i] = walls[i] - 500
      sPath = shortestPath(removedWall, nodes, map)
      # We add +1 because google foobar includes original node
      paths.append(sPath+1)
  smallestPath = float("inf")
  for path in paths:
    if path < smallestPath:
      smallestPath = path
  return smallestPath
    
# Our dijkstra's algorithm function
def shortestPath(walls, nodes, map):
  # init_graph based on dijkstra's algorithm code
  init_graph = {}
  for n in nodes:
    init_graph[n] = {}
  # loop through our map/nodes
  for index, n in enumerate(nodes):
    # if our node is not on the right, and it's not the last node in the loop, then 
    if index < len(nodes)-1:
      # if our next index is not the ends of the map
      if (index+1) % getSize(map)[0] != 0:
        if walls[index] > walls[index+1]:
          init_graph[n][nodes[index+1]] = walls[index]
        else:
          init_graph[n][nodes[index+1]] = walls[index+1]
    if index < len(nodes)-getSize(map)[0]:
      if walls[index] > walls[index+1]:
        init_graph[n][nodes[index+getSize(map)[0]]] = walls[index]
      else:
        init_graph[n][nodes[index+getSize(map)[0]]] = walls[index+getSize(map)[0]]
  graph = Graph(nodes, init_graph)
  shortest_path = dijkstra_algorithm(graph=graph, start_node=nodes[0])
  # w
  return shortest_path[1].get(nodes[-1])

def getSize(map):
  return [len(map[0]), len(map)]


print(solution([
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
 [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
 [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 ]))

print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))