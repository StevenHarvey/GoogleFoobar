#h is perfect tree height
#q is a list of positive integers representing different flux converters
def binary(top,num,under):
  under=under/2 
  right=top-1 
  left=top-1-under 
  if right==num or left==num:
    return top
  else:
    if num<=left:
      return binary(left, num, under)
    else:
      return binary(right,num,under)
def solution(h,q):
  head=(2**h)-1
  result=[]
  for i in range(len(q)):
    if q[i]<head and q[i]>=1:
      x=binary(head,q[i],head-1)
      result.append(x)
    else:
      result.append(-1)
  return result
  