from PIL import Image, ImageDraw


def gradient(color):
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    if str(color).upper() == "R":
        for i in range(256):
            draw.line((i * 2, 0, i * 2, 200), fill=(i, 0, 0), width=2)
    elif str(color).upper() == "G":
        for i in range(256):
            draw.line((i * 2, 0, i * 2, 200), fill=(0, i, 0), width=2)
    elif str(color).upper() == "B":
        for i in range(256):
            draw.line((i * 2, 0, i * 2, 200), fill=(0, 0, i), width=2)
    new_image.save("gradient.png", "PNG")


gradient("b")
