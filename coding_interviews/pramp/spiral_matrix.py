'''
leftmost,
rightmost,
upmost,
botmost,



left->right, upmost = upmost -1 
up -> bottom, rightmost = rightmost - 1
right->left, botmost = botmost + 1
bottom -> up, leftmost = leftmost+1
'''

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1) ]

def spiral_copy(inputMatrix):
  
  leftmost = 0
  rightmost = len(inputMatrix[0]) - 1 
  upmost = 0
  botmost = len(inputMatrix) - 1
  
  
  cur_idx = 0
  res = []
  
  element_counts = len(inputMatrix) * len(inputMatrix[0])
  
  counter = 0
  
    
    
    
    
  while 1:   
    for i in range(leftmost, rightmost+1):
      counter+= 1
      res.append(inputMatrix[upmost][i])
    upmost += 1
    
    if counter == element_counts:
      return res
    
    for i in range(upmost, botmost+1):
      counter+= 1
      res.append(inputMatrix[i][rightmost])

    rightmost -= 1
     
    if counter == element_counts:
      return res
    
    for i in range(rightmost, leftmost-1, -1):
      counter+= 1
      res.append(inputMatrix[botmost][i])

    botmost -= 1

    if counter == element_counts:
      return res


    for i in range(botmost, upmost-1, -1):
      counter+= 1
      res.append(inputMatrix[i][leftmost])

    leftmost += 1

    if counter == element_counts:
      return res

 