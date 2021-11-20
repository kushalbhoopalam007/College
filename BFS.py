"""
Task 3. Write a python program to implement Breadth First Search Traversal
"""

graph={'A':['B','C','E'],
       'B':['A','D','E'],
       'C':['A','F','G'],
       'D':['B'],
       'E':['A','B','D'],
       'F':['C'],
       'G':['C']}

visited = []#List to keep track of visited nodes.
queue = []#Initialize a queue

def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)

  while queue:
    s=queue.pop(0)
    print(s,end=" ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

bfs(visited,graph,'A')

