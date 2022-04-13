import math

# def solution(n,a,b):
  
#   answer = 0
  
#   while 1:

#     if( a == b):
#       break
    
#     a = math.ceil(a / 2)
#     b = math.ceil(b / 2)    
#     answer += 1


def solution(n,a,b):
    return (a-1)^(b-1).bit_length()