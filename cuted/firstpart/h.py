from PIL import Image

for i in range(1, 16):
    filename = "%s.jpg" % i
    im = Image.open(filename)
    heigth = 0
    width = 138
    while (True):
        cordinates = width, heigth
        px = im.getpixel(cordinates)
        heigth += 1
        if px < (30, 30, 30):
            break
    
    print("in %s height = %s" % (i, heigth))
