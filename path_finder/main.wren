import "dome" for Window, Process
import "graphics" for Canvas, Color, Font, ImageData

var MAZE = [
	[1,1,1,1],
	[1,0,2,1],
	[1,0,0,1],
	[1,0,0,1],
	[1,0,0,1],
	[1,0,0,1],
	[1,3,0,1],
	[1,1,1,1]
]

var COLORS = ["ffffff","000000","ff0000","0000ff"]
class PathFinder {
	_maze = []
	_startPosition = [0,0]
	_endPosition = [0,0]
	_paths = []
	
	nextstep(pathpos) {
		x = pathpos[0]
		y = pathpos[1]
		returnobj = []
		if (_maze[y][x+1] != 1) returnobj.add([x+1,y])
		if (_maze[y][x-1] != 1) returnobj.add([x-1,y])
		if (_maze[y+1][x] != 1) returnobj.add([x,y+1])
		if (_maze[y-1][x] != 1) returnobj.add([x,y-1])
		return returnobj
	}
	
	construct new(maze) {
		_maze = maze
		for (y in 0..._maze.count) for (x in 0..._maze[y].count) if (_maze[y][x] == 3) _startPosition = [x,y]
		for (y in 0..._maze.count) for (x in 0..._maze[y].count) if (_maze[y][x] == 2) _endPosition = [x,y]
	}
	
	update() {
		while 
	}
}

class main {
  construct new() {}
  init() {
		_pathFinder = PathFinder.new(MAZE)
		Canvas.resize(MAZE[0].count, MAZE.count)
  }
  update() {
		_pathFinder.update()
	}
  draw(alpha) {
		for (y in 0...MAZE.count) {
			for (x in 0...MAZE[y].count) {
				Canvas.pset(x, y, Color.hex(COLORS[MAZE[y][x]]))
			}
		}
	}
}

var Game = main.new()
