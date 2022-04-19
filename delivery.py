import sys
from collections import deque

def bfs(g, graph, K, N):
  
    q = deque([g])    
    table = [sys.maxsize]*(N+1)    
    table[1] = 0
    
    while q:
        temp = q.popleft()
        print(temp)
        start_point = temp[0]
        cost = temp[1]

        for i in graph[start_point]:
            end_point, new_cost = i[0], i[1]
            
            if cost + new_cost <= K and cost + new_cost < table[end_point]:
                table[end_point] = cost + new_cost
                q.append([end_point, cost+new_cost])
      
    return table

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]    
    
    for i, j, cost in road:
        graph[i].append([j, cost])
        graph[j].append([i, cost])    

    print(graph)
        
    answer = 0
    
    lst = bfs([1, 0], graph, K, N)
  
    for i in lst:
        if i != sys.maxsize:
            answer += 1

    print(answer)
            
    return answer




from queue import PriorityQueue

def dijkstra(road, N):
    dist = [1000000] * (N + 1)
    dist[1] = 0 #시작노드 1은 0
    pq = PriorityQueue()
    pq.put([0,1])
    
    while not pq.empty():
        cost, here = pq.get()
        if cost > dist[here]: continue
        
        for i in range(len(road)):
            if road[i][0] == here:
                cost2, there = road[i][2] + cost, road[i][1]
                if cost2 < dist[there]:
                    dist[there] = cost2
                    pq.put([cost2, there])
            elif road[i][1] == here:
                cost2, there = road[i][2] + cost, road[i][0]
                if cost2 < dist[there]:
                    dist[there] = cost2
                    pq.put([cost2, there])
    return dist
    
def solution(N, road, K):
    answer = 0
    dist = dijkstra(road, N)
    for i in dist:
        if i <= K:
            answer += 1
    return answer