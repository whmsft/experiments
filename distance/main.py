import math
points1 = {
	0: (0,0,1),
	1: (20,0,0,2,3),
	2: (40,20,1,5),
	3: (40,-20,1,6),
	4: (50,50,5,7),
	5: (50,20,2,4),
	6: (50,-40,3,7),
	7: (100,0,4,6),
}
points2 = {
  0: (0,0,1,2),
  1: (10,10,0,2),
  2: (20,0,0,1,3),
  3: (40,0,2)
}

def findPath(dataset,start,end):
  points = dataset
  path = [start]
  distance = 0
  while path[-1]!=end:
    excludedPoints = []
    if len(path)>1:excludedPoints.append(path[-2])
    pointDistances = []
    reachablePoints = [item for item in points[path[-1]][2:] if item not in excludedPoints]
    for visitedPoint in path:
      if visitedPoint in reachablePoints: path = path[:path.index(visitedPoint)+1]+[path[-1]]
    if len(path)>1:excludedPoints.append(path[-2])
    reachablePoints = [item for item in points[path[-1]][2:] if item not in excludedPoints]  
    for point in reachablePoints:
      pointDistances.append(math.sqrt((points[path[-1]][0]-points[point][0])**2 + (points[path[-1]][1]-points[point][1])**2))
    nextPoint = reachablePoints[pointDistances.index(min(pointDistances))]
    path.append(nextPoint)
  for index in range(len(path)):
    if index!=0:distance+=math.sqrt(
      (points[path[index]][0]-points[path[index-1]][0])**2 + (points[path[index]][1]-points[path[index-1]][1])**2
    )
  return path, distance

print(findPath(points1,0,3))
