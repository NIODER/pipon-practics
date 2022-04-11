from PIL import Image, ImageDraw


def board(num, size):
    side = num * size
    board_img = Image.new("RGB", (side, side), (0, 0, 0))
    draw = ImageDraw.Draw(board_img)
    is_black = True
    point1 = 0, 0
    point2 = size, size
    for i in range(num):
        for j in range(num):
            if is_black:
                fill = 0, 0, 0
            else:
                fill = 255, 255, 255
            draw.rectangle((point1, point2), fill=fill, width=0)
            point1 = point1[0], point1[1] + size
            point2 = point2[0], point2[1] + size
            is_black = not is_black
        point1 = point1[0] + size, 0
        point2 = point2[0] + size, size
        is_black = not is_black
    board_img.save("rectangle.png", "PNG")


board(1000, 50)
