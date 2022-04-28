import math
 
def minimax (curDepth, nodeIndex, maxTurn, scores, targetDepth, x):
    if (curDepth == targetDepth):
        return scores[nodeIndex]

    elif (x % 2) == 0:
      if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2,     False, scores, targetDepth, x),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth, x))
      else:
        return min(minimax(curDepth + 1, nodeIndex * 2,     True, scores, targetDepth, x),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth, x))
    else:
      if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 3,     False, scores, targetDepth, x),
                   minimax(curDepth + 1, nodeIndex * 3 + 1, False, scores, targetDepth, x),
                   minimax(curDepth + 1, nodeIndex * 3 + 2, False, scores, targetDepth, x))
      else:
        return min(minimax(curDepth + 1, nodeIndex * 3,     True, scores, targetDepth, x),
                   minimax(curDepth + 1, nodeIndex * 3 + 1, True, scores, targetDepth, x),
                   minimax(curDepth + 1, nodeIndex * 3 + 2, True, scores, targetDepth, x))

scores = []
curDepth=0
nodev=0
maxTurn=True
x=int(input("Enter total number of leaf nodes = "))
for i in range(x):
    y=int(input("Enter leaf values: "))
    scores.append(y)

if (x % 2)==0: 
  treeDepth = math.log(len(scores), 2)
else:
  treeDepth = math.log(len(scores), 3)
 
print("The optimal value is : ", end = "")
print(minimax(curDepth, nodev, maxTurn, scores, treeDepth, x))