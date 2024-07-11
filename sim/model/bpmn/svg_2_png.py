from cairosvg import svg2png

svg_path = "sim/model/bpmn/diagram.svg"
png_path = "sim/model/bpmn/diagram.png"


def convert():
    svg2png(url=svg_path, write_to=png_path)


if __name__ == "__main__":
    convert()
