def solution(rows, columns, queries):
  answer = []

  rows = 6
  columns = 6

  #queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]];
  queries = [[2,2,5,4],[3,3,6,6]];

  table = [[col for col in range(columns)] for row in range(rows)]
  
  for i in range(columns):
    for j in range(rows):      
      table[j][i] = (columns * j) + i + 1

  for query in queries:
    x1, y1, x2, y2 = query[0], query[1], query[2], query[3]
  
    x = table[x1-1][y1-1]
    y = table[x2-1][y2-1]

    print(x, y)
    
    #1, 2, 3
    for a in range(x1 - 1, x2 - 1):      
      table[a][y1 - 1] = table[a + 1][y1 - 1]    
      table[x2 - a][y2 - 1] = table[(x2 - a) - 1][y2 - 1]
  
    for b in range(y1, y2 - 1):    
      table[x1 - 1][b + 1] = table[x1 - 1][b]
      #table[x2 - 1][y2 - 1 - b] = table[x2 - 1][y2 - b]
  
    table[x1 - 1][y1] = x
    table[x2 - 1][y2 - 2] = y

    for a in table:
      print(a)

  return answer