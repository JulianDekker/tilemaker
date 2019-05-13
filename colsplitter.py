import PIL

from PIL import Image

img_file = "fpsbananaphonespray.png"
COLUMNS = {"1": {"position":"20"}, "2": {"position":"50"}, "3": {"position":"70"}}


def columnsFromImage():
    img = Image.open(img_file)
    image_name = img.filename

    width, height = img.size
    for i, col in enumerate(COLUMNS):
        col = COLUMNS.get(str(col))
        try:
            print(height)
            area = (int(col['position']), 0, int(COLUMNS[str(i+2)]['position']), int(height))
            print('no error')
        except KeyError:
            print('error')
            area = (int(col['position']), 0, int(width), int(height))
        output_image = img.crop(area)
        output_image.save(image_name+str(i)+'.png', 'PNG')

columnsFromImage()