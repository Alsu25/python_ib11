from PIL import Image, ImageDraw


def board(d, pix):
    image = Image.new("RGB", (d * pix, d * pix))
    draw = ImageDraw.Draw(image)
    for i in range(d):
        for ai in range(d):
            if (ai % 2 == 0 and i % 2 == 1) or (ai % 2 == 1 and i % 2 == 0):
                draw.rectangle(((ai * pix, i * pix),
                                (ai * pix + pix, i * pix + pix)), "white")
            else:
                draw.rectangle(((ai * pix, i * pix),
                                (ai * pix + pix, i * pix + pix)), "black")
    image.save("res.png")