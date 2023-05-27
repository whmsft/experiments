// A trial to implement a GUI for this in DOMEENGINE

import "json" for Json
import "graphics" for Canvas, Color, Font

class main {
    construct new() {}
    init() {
        Canvas.resize(10, 10)
        Font.load("OpenSans", "./OpenSans.ttf", 5)
        Font["OpenSans"].print("A", 0, 0, Color.white)
        _nuisance = []
        for (y in 0..10) {
            _nuisance.add([])
            for (x in 0..10) {
                if (Canvas.pget(x, y).r == 0) {
                    _nuisance[y].add(0)
                }
                if (Canvas.pget(x, y).r == 255) {
                    _nuisance[y].add(1)
                }
            }
        }
        System.print(cutArray(_nuisance))
    }
    update() {}
    draw(alpha) {}
}

var Game = main.new()