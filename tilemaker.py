import sys
from PIL import Image
import os

def maketiles(im, cropheight, cropwidth, foldername):
    """"Loops through image and crops frames of given size."""
    imheight = im.size[1]
    imwidth = im.size[0]
    x = 0
    y = 0
    i1 = 0
    i2 = 0
    while y < imheight:
        i1 += 1
        while (x < imwidth):
            i2 += 1
            print(x, y, x+cropwidth, y+cropheight)
            horizontalcrop(x, y, x+cropwidth, y+cropheight, i1, i2, foldername)
            x += cropwidth
        x = 0
        i2 = 0
        y += cropheight
    y = 0

def horizontalcrop(x1, y1, x2, y2, i1, i2, foldername):
    """"Crops a single frame"""
    box = (x1, y1, x2, y2)
    region = im.crop(box)
    filename = "_" + str(i1).zfill(2) + '_' + str(i2).zfill(2)+'.png'#"_{0}_{1}.png" % str("{:02d}".format(i1)), str("{:02d}".format(i2))  #
    try:
        os.mkdir(foldername)
    except:
        pass
    region.save(foldername+'/'+filename, 'PNG')

def subsmall(im, size):
    outfile = str(size)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(outfile+'.jpeg', "JPEG")
    return outfile+'.jpeg'

#infiles = ["zoom__1.jpg", "zoom__2.jpeg", "zoom__3.jpeg", "zoom__4.jpeg"]
infiles = ["zoom__3.jpeg", "zoom__4.jpeg"]

for infile in infiles:
    with Image.open(infile) as im:
        print(im.format, "%d x %d" % im.size, im.mode)
        imheight = im.size[1]
        imwidth = im.size[0]
        maketiles(im, 100, 100, infile[:-4])