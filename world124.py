def solution(n):

  answer = ''  
  
  while n > 0:

    n, r = divmod(n - 1, 3)

    if(r == 0):
      r = 4

    answer = str(r) + answer

  return answer