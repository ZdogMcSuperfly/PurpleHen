import os
from PIL import Image
# assign directory
directory = "./images"

# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        image = Image.open(f)
        image.thumbnail((640,480))
        image.save(ddirectory+"/thumbs/"+f[38:])
        print('{"src": "'+f[38:]+'", "name": "", "morph": "", "location": "", "camera": "", "date": "'+Image.open(f)._getexif()[36867]+'", "favourite": "false", "wild": "true", "new": "true"},')

# Image.open(f)._getexif()[36867]
