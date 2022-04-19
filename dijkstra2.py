from queue import PriorityQueue

def solution():

  # 입력받아야함
  n = 5
  r = 8  
  root = [[1, 2, 2],[1, 3, 3],[1, 4, 1],[1, 5, 10]
         ,[2, 4, 2],[3, 4, 1],[3, 5, 1],[4, 5, 3]]
  s, e = 1, 5 
  
  dist = dijkstra(s, n, root)
  
  print(dist[e])
  

def dijkstra(s, n, root):

  dist = [100000] * (n + 1)
  dist[s] = 0
  pq = PriorityQueue()
  pq.put([1, 0])

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
  
  