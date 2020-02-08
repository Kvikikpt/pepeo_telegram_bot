from PIL import Image
import random

def photo_select():
    i = random.randint(1, 15)
    b = random.randint(16, 22)
    im1 = Image.open(f'cuted/firstpart/{i}.jpg')
    im2 = Image.open(f'cuted/secondpart/{b}.jpg')
    width = im2.width + im1.width
    final = Image.new(mode = "RGB", size = (width, 150), color = (255,255,255))
    bl_h1 = im1.height - 1
    width = im1.width  -3
    while (True):
        cordinates = width, bl_h1
        px = im1.getpixel(cordinates)
        bl_h1 -= 1
        if px < (30, 30, 30):
            break
    bl_h2 = im2.height - 1
    width = 3
    while (True):
        cordinates = width, bl_h2
        px = im2.getpixel(cordinates)
        bl_h2 -= 1
        if px < (30, 30, 30):
            break
    print(bl_h2)
    print(bl_h2 - bl_h1)
    final.paste(im1, (0, bl_h2 - bl_h1))
    final.paste(im2, (im1.width, 0))
    final.save("someshet.jpg")
    return(final)