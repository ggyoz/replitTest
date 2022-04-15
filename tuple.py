from collections import Counter
import re

def solution(s):  
  
  answer = []

  # 문자열에서 정규식에 맞는 문자만 골라서 리스트로 출력
  # 리스트에 있는 문자의 개수를 출력
  s = Counter(re.findall('\d+', s))  

  # 사용된 문자수로 정렬 후 키값을 출력
  arr = [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]
  print(arr)

  answer = list(map(int, arr))
  print(answer)
  
  # 처음 풀었던 방법
  # s = s.replace("{{", "").replace("}}", "")  
  # arr = s.split("},{")

  # arr1 = [0] * len(arr)

  # for a in arr:
  #   k = a.split(",")
  #   arr1[len(k) - 1 ] = set(k)
  
  # answer.append(int(list(arr1[0])[0]))

  # for j in range(1, len(arr1)):    
    
  #   m = (arr1[j] - arr1[j - 1]).pop()
  #   answer.append(int(m))
    
  return answer