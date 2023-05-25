import "dome" for Window, Process
import "graphics" for Canvas, Color, Font, ImageData

var MAZE = ImageData.load("./maze.png")

class PathFinder {
	originalMaze {_om}
	initialPoint {_u}
	finalPoint {_v}

	// A simple algorithm to get net-displacement (and points)
	pointDisplaced(u, v) {
		_slope = (v[1] - u[1]) / (v[0] - u[0])
    	_y_intercept = u[1] - (_slope * u[0])
    	_pointsCovered = []
    	_x_min = [u[0], v[0]].sort()[0]
    	_x_max = [u[0], v[0]].sort()[1]
    	for (x in _x_min..._x_max+1) {
	        _y = _slope * x + _y_intercept
        	_pointsCovered.add([x.round, _y.round])
		}			
	    return _pointsCovered
	}

	construct init() {
		_om = []
		// Create a blank 2D array for both Mazes
		for (y in 0...MAZE.height) {
			_om.add([])
			for (x in 0...MAZE.width) {
				_om[y].add("")
			}
		}
		
		// Add MAZE's map to originalMaze and points respective variables
		for (y in 0...MAZE.height) {
			for (x in 0...MAZE.width) {
				_color = MAZE.pget(x, y)
				if (_color.r == 0 && _color.g == 0 && _color.b == 0) _om[y][x] = "#"
				if (_color.r == 0 && _color.g == 132 && _color.b == 255) if (initialPoint == null) _u = [x, y] else _v = [x, y]
			}			
		}
		System.print(_u)
		System.print(_v)
	}
}

class main {
  construct new() {}
  init() {
	_pathFinder = PathFinder.init()
	Canvas.resize(MAZE.width, MAZE.height)
  }
  update() {}
  draw(alpha) {
	MAZE.draw(0,0)
	for (point in _pathFinder.pointDisplaced([1, 14], [10, 10])) {
		Canvas.pset(point[0], point[1], Color.red)
	}
  }
}

var Game = main.new()
