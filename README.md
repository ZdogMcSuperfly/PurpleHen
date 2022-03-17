# 'PurpleHen' <sub>v2</sub>
## Photo gallery and photo tagging for birders and nerders.

<p align="center"><br>
<img src="https://github.com/ZdogMcSuperfly/PurpleHen/blob/main/favicon.svg"></p>

I love birding, computers, data hoarding and collecting (same same). I made this software to nice and neatly display my photos in a way for me to enjoy and also to host it online to make sharing photos with friends and family easy too. I'm sure others could get some use out of this and improve apon it but I'm mainly hosting it on GitHub because Git is cool. 😎
## Features
- Frontend designed to display photos nicely.
- Nine different tag types to add to photos.
- Buttons to sort the gallery display based on tags.
- Script to automate the metadata creation for batches of photos.
- Script to generate thumbnails for batches of photos.
- Can be hosted online or used offline.
- Works on desktop and on mobile.

## User Interface
__Consists of two main sections:__<br>
A header that stays at the top of the page regardless of scrolling with infomation on the left (instructions to the user, current ammount of photos, and photo liceance), buttons in the middle for sorting photos (new photos, favorite photos, wild photos, captive photos, photos by country, and all photos), a heading and space for displaying descripts, and finally on the right a space for a logo or signature.

A gallery that displays photos on a single page in columns of three. Can show portrait and landscape photos next to each other and when hovering displays metadata of the photo below the buttons in the header. Horizontal rules and blank spaces can be inserted to seperate and organize photos.

## Installation
Dependencies: Python Pillow
```sh
git clone https://github.com/ZdogMcSuperfly/PurpleHen.git
```
## Usage
__"images" folder__<br>
Found in the root directory this is where all photos will be stored. Contains one subfolder "thumbs" which contains the thumbnails used in rendering; thumbnail filenames must be the same as the ones in images.

__image_data.js__<br>
This is where metadata for photos are stored, each photo has its own line and is rendered from first line to last, knowing this can be used to organize photos. Each line contains 9 different tags that can be filled out to give photos extra information.
<br>
```js
{"src": "", "name": "", "morph": "", "location": "", "camera": "", "date": "", "favourite": "", "wild": "", "new": ""},
```
| TAG  ||
| ------------- | ------------- |
| src  | Filename of the photo. |
| name  | Birds name. |
| morph  | Notate a birds phenotype.<br> eg. male, female, juvinile, albino etc. |
| location  | Location the photo was taken.<br> Use ISO 3166-1 alpha-3 codes at the end for country sorting to work. |
| camera  | What camera was used to take the photo. (even if it's a smartphone)  |
| date  | What date the photo was taken |
| favourite  | Set to "true" will mark that photo as a favorite one.|
| wild  | Set to "true" for wild birds "false" for captive ones.|
| new  | When adding a new batch of photos, set to "True" for sort by new to work.|

There are two special values that be can be used to alter gallery rendering. Setting "src" tags value to "hr" will create a horizontal rule across the page or use the value "blank" to create a blank spot in the gallery. (see __Know Issues__ for additional infomation.)

__generate.py__<br>
This python script (wip) will assist in creating metadata and must be ran from the root directory.<br>Open the file in a text editor to edit the template (line 14) filling in the "name","morph","location","camera","favourite","wild" and "new" tags.<br>Note that the template will be applied to all photos so normally "name", "morph", "location" will be set to blank,<br>"camera" to whatever camera was used and "favourite", "wild" and "new" set to boolean values. ("false", "true", "true" respectivly.)<br>The last two tags "src" takes the filename and "date" takes the date from the EXIF data from the file all automatically.

When the script is ran itll output data to be copied from terminal to "image_data.js". At the moment this part is not automatic.

## Customizing Ideas
On my copy I have the "Favorites" button renamed to "Lifelist" and I use it too display one photo per species like what a lifelist is.
For my logo I have the bird emoji (1F426, 🐦) so each device I visit my copy on I see a different glyph due to devices having different fonts. It's like Unicode birding.

This doesn't have to be used just for bird photos either could be bird drawings or other mediums or a mix! Could be used for any photo gallery/tagging needs so get creative! : )

## Known Issues
- Automation scripts are not fully automatic and are not explicitly user friendly.
- Blanks spaces work with using a tiny compleatly transparent image; this is jank and a better solution will improve this.
- Another jank is that horizontal rules take up 3 lines in image_data.js and must start in the leftmost column or else wont render properly.
- I cant think of a better name than PurpleHen, any ideas are appreciated.
- Only one photo resolution has really been tested (that being 4:3 and 3:4)
- Thumbnail script generates landscape thumbnails for portrait photos.

## License
GNU 3.0
