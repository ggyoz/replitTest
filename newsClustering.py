import re
import math

# def solution(str1, str2):
#   answer = 0

#   str1 = "E=M*C^2"
#   str2 = "e=m*c^2"
  
#   str1 = str1.upper()
#   str2 = str2.upper()

#   arrStr1 = []
#   arrStr2 = [] 

#   # 차집합
#   intersection = arrStr1.copy()
  
#   for a in range(0, len(str1) - 1):
#     str = str1[a:a+2]    
#     if(str.isalnum() and re.search('\d', str) == None ):       
#       arrStr1.append(str1[a:a+2])   

#   print(arrStr1)
#   for a in range(0, len(str2) - 1):
#     str = str2[a:a+2]    
#     if(str.isalnum() and re.search('\d', str) == None ):       
#       arrStr2.append(str2[a:a+2])   
#   print(arrStr2)
  
#   # 합집합
#   union = arrStr1.copy()
  
#   for b in arrStr2:
#     if( b not in arrStr1):
#       union.append(b)
#     else:
#       arrStr1.remove(b)
#       intersection.append(b)

#   print(union)
#   print(intersection)   

#   if(len(intersection) == 0 and len(union) == 0):
#     answer = 1
#   else:
#     answer = len(intersection) / len(union)
  
#   return int(answer * 65536)



def solution(str1, str2):

  answer = 0
  # str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
  # str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

  # print(str1)
  # print(str2)
  
  list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
  list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

  print(list1)
  print(list2)

  gyo = set(list1) & set(list2)
  hap = set(list1) | set(list2)

  print(gyo)
  print(hap)

  # gyo = set(str1) & set(str2)
  # hap = set(str1) | set(str2)
  
  # print(gyo)
  # print(hap)

  # if len(hap) == 0 :
  #     return 65536

  gyo_sum = sum([min(list1.count(gg), list2.count(gg)) for gg in gyo])
  print(gyo_sum)
  
  hap_sum = sum([max(list1.count(hh), list2.count(hh)) for hh in hap])
  print(hap_sum)

  # return math.floor((gyo_sum/hap_sum)*65536)

  return answer