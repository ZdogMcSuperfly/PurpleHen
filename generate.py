import os
from PIL import Image
# assign directory
directory = "./images"

# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print("// " + f)
        image = Image.open(f)
        image.thumbnail((640,480))
        image.save(directory+"/thumbs/"+filename)
        exif = Image.open(f)._getexif()
        exif_date = "Unknown date" if 36867 not in exif else exif[36867]
        print('{"src": "'+filename+'", "name": "", "morph": "", "location": "", "camera": "", "date": "'+ exif_date + '", "favourite": "false", "wild": "true", "new": "true"},')