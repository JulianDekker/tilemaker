import PIL

from PIL import Image

img_file = "fpsbananaphonespray.png"
COLUMNS = {"1": {"position":"20"}, "2": {"position":"70"}}


def columnsFromImage():
    img = Image.open(img_file)
    image_name = img.filename

    width, height = img.size

    col = COLUMNS[str(1)]
    area = (0, 0, round(width*(int(col['position'])/100)), int(height))
    output_image = img.crop(area)
    output_image.save(str(0) + image_name + '.png', 'PNG')

    for i, col in enumerate(COLUMNS):
        col = COLUMNS.get(str(col))
        pixelsleftcorner = round(width*(int(col['position'])/100))
        try:
            pixelsrightcorner = round(width * (int(COLUMNS[str(i + 2)]['position']) / 100))
            area = (pixelsleftcorner, 0, pixelsrightcorner, int(height))
        except KeyError:
            area = (pixelsleftcorner, 0, int(width), int(height))
        output_image = img.crop(area)
        output_image.save(str(i+1)+image_name, 'PNG')

columnsFromImage()