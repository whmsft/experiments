// A trial to implement a GUI for this in DOMEENGINE

import "json" for Json
import "graphics" for Canvas, Color, Font

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
    static determine(pixeldata, dataset) {
        var matchdata = {}
        for (char in dataset) {
            matchdata[char.key] = match_value(pixeldata, splitize(char.value[0]))
        }
        for (finding in matchdata) {
            if (finding.value >= 0.8) {
                System.print(finding.value)
                return finding.key
            }
        }
    }
}

class main {
    construct new() {}
    init() {
        Font.load("OpenSans", "./OpenSans.ttf", 16)
        Font["OpenSans"].print("A", 0, 0, Color.white)
    }
    update() {}
    draw(alpha) {}
}

var Game = main.new()