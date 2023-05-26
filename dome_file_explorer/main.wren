import "io" for FileSystem
import "graphics" for Canvas, Color
import "ui/ui" for Label, Button

class game {
	construct new() {
		_buttons = []
		_absolute = FileSystem.basePath()
		_dir = "//./C:/Windows"
		_h = -25
	}
	makeview() {
		Canvas.cls()
		_buttons = []
		_h = -25
		System.print(_dir)
		for (dir in FileSystem.listDirectories(_dir)) {
			if (dir != ".") {
				_buttons.add(Button.new(dir, [0, _h+25, 200, 25]))
				_buttons[-1].onMouseClick {
					_dir = _dir+"/"+dir+"/"
					Canvas.print(">>", 0,0, Color.white)
      				makeview()
    			}
    			_h = _h+25
			}
		}
	}
	init() {
		makeview()
	}
	update() {
		_buttons.each {|bt| bt.update()}
	}
	draw(alpha) {
		_buttons.each {|bt| bt.draw()}
	}
}
var Game = game.new()
