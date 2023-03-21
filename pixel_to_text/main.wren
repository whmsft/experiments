// A trial to implement a GUI for this in DOMEENGINE

import "graphics" for Canvas, Color

class Pixel_to_text {
    static splitize(characters) {
        var split_list = []
        characters.each{|char| split_list.add(char)}
        return [split_list, split_list.count.sqrt]
    }
    static match_value(v1, v2) {
        var common_characters = []
        v1[0].each{|char| 
            if (v2[0].indexOf(char) > -1) {
                common_characters.add(char)
            }
        }
	    return ((common_characters.count)/v1[1]/v2[1])
    }
}

class main {
    construct new() {}
    init() {
        _vec01 = Pixel_to_text.splitize("abcdeimnop")
        _vec02 = Pixel_to_text.splitize("bcdeinop")
        System.print(Pixel_to_text.match_value(_vec01, _vec02))
    }
    update() {}
    draw(alpha) {}
}

var Game = main.new()