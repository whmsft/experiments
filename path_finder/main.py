maze = [
	[1,1,1,1],
	[1,0,2,1],
	[1,0,0,1],
	[1,0,0,1],
	[1,0,0,1],
	[1,0,0,1],
	[1,3,0,1],
	[1,1,1,1]
]

_startPosition = [0,0]
_endPosition = [0,0]
_paths = []
	
def nextstep(pathpos):
	x = pathpos[0]
	y = pathpos[1]
	returnobj = []
	if maze[y][x+1] != 1: returnobj.append([x+1,y])
	if maze[y][x-1] != 1: returnobj.append([x-1,y])
	if maze[y+1][x] != 1: returnobj.append([x,y+1])
	if maze[y-1][x] != 1: returnobj.append([x,y-1])
	return returnobj

for y in range(len(maze)):
	for x in range(len(maze[y])):
		if maze[y][x] == 3: _startPosition = [x,y]
for y in range(len(maze)):
	for x in range(len(maze[y])):
		if maze[y][x] == 2: _endPosition = [x,y]
_paths.append(_startPosition)

print(_startPosition)
if True:
	nxt = nextstep(_paths[0])
	for i in nxt:
		_paths.append(i)
	print(len(_paths))
	print(_paths)
print("Found!")
