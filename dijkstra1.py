from queue import PriorityQueue

def solution():
  
  node_cnt, root_cnt = map(int, input().split())
  
  start_node = int(input())
  
  root = [[] for i in range(node_cnt + 1)]
  
  for r in range(root_cnt):

    a, b, c = map(int, input().split())    
    root[r] = [a, b, c] 

  dist = dijkstra(root, node_cnt, start_node)  
  
  for a in range(len(dist)):  
    if a == 0:
      continue
    else:
      print("INF" if dist[a] == 10e9 else dist[a] )      

def dijkstra(root, node_cnt, start_node):
  
  dist = [10e9] * (node_cnt + 1)  
  pq = PriorityQueue()
  dist[start_node] = 0
  pq.put([start_node, 0])

  while not pq.empty():    
    here, cost = pq.get()
    if(cost > dist[here]):
      continue
      
    for r in range(len(root)):
      if (root[r][0] == here):
        here2 = root[r][1]
        cost2 = root[r][2] + cost

        if cost2 < dist[here2]:
          dist[here2] = cost2
          pq.put([here2, cost2])        
  
  return dist
      

    
