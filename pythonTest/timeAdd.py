
import datetime

def solution():
  
  h, m = input().split()
  addmin = input()

  date = datetime.datetime(1999, 1, 1, int(h), int(m), 0)  
  d = datetime.timedelta(minutes = int(addmin))

  date = date + d

  print(date.hour, date.minute)


# def solution():
#   H, M = map(int, input().split())
#   timer = int(input()) 
  
#   H += timer // 60
#   M += timer % 60
  
#   if M >= 60:
#       H += 1
#       M -= 60
#   if H >= 24:
#       H -= 24
  
#   print(H,M)
