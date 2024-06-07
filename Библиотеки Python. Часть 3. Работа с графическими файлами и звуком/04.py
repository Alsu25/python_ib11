from PIL import Image, ImageFilter


def motion_blur(n):
    image = Image.open("image.jpg")
    image = image.transpose(Image.ROTATE_270)
    filtered = image.filter(ImageFilter.GaussianBlur(radius=n))
    filtered.save("res.jpg")
