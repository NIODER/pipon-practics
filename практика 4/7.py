from PIL import Image


def makeanagliph(filename, delta):
    image = Image.open(filename)
    image_pixel = image.load()
    x, y = image.size
    new_image = Image.new("RGB", (x, y), (255, 255, 255))
    new_image_pixel = new_image.load()
    for i in range(x):
        for j in range(y):
            r, g, b = image_pixel[i, j]
            if i - delta >= 0:
                r1, g1, b2 = image_pixel[i - delta, j]
                new_image_pixel[i, j] = r1, g, b
            else:
                g, b = image_pixel[i, j][1:]
                new_image_pixel[i, j] = 0, g, b
    new_image.save("res.png", "PNG")


makeanagliph(input("filename: "), int(input("delta: ")))
