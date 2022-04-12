
def solution(bridge_length, weight, truck_weights):
  
  answer = 0
  que = [0] * (bridge_length - 1)
  total_weight = 0

  print(que)

  while truck_weights:  
    # 트럭배열에서 트럭하나 가져옴    
    if( len(que) < bridge_length and total_weight + truck_weights[0] <= weight ):
      truck_weight = truck_weights.pop(0)      
      total_weight += truck_weight
      que.append(truck_weight)
      print(que)
      answer += 1
      print(answer)
      
    else:
      total_weight -= que.pop(0)      
      if( total_weight + truck_weights[0] <= weight):
        truck_weight = truck_weights.pop(0)
        total_weight += truck_weight
        que.append(truck_weight)
      else:
        que.append(0)        
      print(que)
      answer += 1
      print(answer)
      
  answer += len(que)

  return answer