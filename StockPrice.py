def solution(prices):
  
  answer = []

  for n in range(len(prices)):    
    answer.append(0)   
    for m in range(n + 1, len(prices)):      
      if( prices[n] <= prices[m] ):
        answer[n] += 1
      else:
        answer[n] = 1
        break
    
  return answer
  