# 'PurpleHen' <sub>v3</sub>
## Photo gallery and photo tagging for birders and nerders.

<p align="center"><br>
<img src="https://github.com/ZdogMcSuperfly/PurpleHen/blob/main/favicon.svg"></p>

I love birding, computers, data hoarding and collecting (same same). I made this software to nice and neatly display my photos in a way for me to enjoy and also to host it online to make sharing photos with friends and family easy too. I'm sure others could get some use out of this and improve apon it but I'm mainly hosting it on GitHub because Git is cool. 😎

## Whats New
The unfriendly python script has been replaced with a complete TUI/GUI data editor and thumbnails now generate in correct orientation.

## Features
- Gallery to display photos nicely.
- Nine different tag types to add to photos.
- Buttons to sort the gallery display based on tags.
- Data editor to automate certain metadata creation for batches of photos.
- Data editor allows for users to manually tag photos.
- Data editor to generate thumbnails for batches of photos.
- Image viewer to see what photo is being edited in the data editor.
- Gallery be hosted online or viewed offline.
- Gallery works on desktop and on mobile.

## User Interface for `PurpleHen.py`
__Consists of two main sections:__<br>
A header with current page number and a list of shortcuts (accepts lowercase or uppercase input).

A spreadsheet with data from `image_data.py`. It can be navigated with the up and down keys and if the data is longer than your terminal then left and right will scroll to different pages of data. Pressing enter saves to a file called `new_image_data.py` or if typing just saves your input.

## User Interface for `PurpleHen_gallery.html`
__Consists of two main sections:__<br>
A header that stays at the top of the page regardless of scrolling with infomation on the left (instructions to the user, current ammount of photos, and photo liceance), buttons in the middle for sorting photos (new photos, favorite photos, wild photos, captive photos, photos by country, and all photos), a heading and space for displaying descripts, and finally on the right a space for a logo or signature.

A gallery that displays photos on a single page in columns of three. Can show portrait and landscape photos next to each other and when hovering displays metadata of the photo below the buttons in the header. Horizontal rules and blank spaces can be inserted to seperate and organize photos.

## Installation
Dependencies: NCurses, Pillow, Tkinter
```sh
git clone https://github.com/ZdogMcSuperfly/PurpleHen.git
```
## Usage
__`images` folder__<br>
Found in the root directory this is where all photos will be stored. Contains one subfolder `thumbs` which contains the thumbnails used in rendering; thumbnail filenames must be the same as the ones in `images`.

__`image_data.py`__<br>
This is where metadata for photos are stored, each photo has its own line and is rendered from first line to last, knowing this can be used to organize photos. Each line contains 9 different tags that can be filled out to give photos extra information.
<br>
```js
{"sorce": "", "morph": "", "bird": "", "location": "", "date": "", "camera": "", "favourite": "", "new": "", "wild": ""},
```
| TAG  ||
| ------------- | ------------- |
| source  | Filename of the photo. |
| morph  | Notate a birds phenotype.<br> eg. male, female, juvinile, albino etc. |
| bird  | Birds name. |
| location  | Location the photo was taken.<br> Use ISO 3166-1 alpha-3 codes at the end for country sorting to work. |
| date  | What date the photo was taken. |
| camera  | What camera was used to take the photo. (even if it's a smartphone)  |
| favourite  | Set to "true" will mark that photo as a favorite one.|
| new  | When adding a new batch of photos, set to "True" for sort by new to work.|
| wild  | Set to "true" for wild birds "false" for captive ones.|

There are two special values that be can be used to alter gallery rendering. Setting `source` tags value to "hr" will create a horizontal rule across the page or use the value "blank" to create a blank spot in the gallery. (see __Know Issues__ for additional infomation.)

__`PurpleHen_image_viewer.py`__<br>
After operning `PurpleHen.py` in your terminal open another terminal and run this file to get a visual of what photo is currently highlighted.

## Customizing Ideas
On my copy I have the "Favorites" button renamed to "Lifelist" and I use it too display one photo per species like what a lifelist is.
For my logo I have the bird emoji (1F426, 🐦) so each device I visit my copy on I see a different glyph due to devices having different fonts. It's like Unicode birding.

This doesn't have to be used just for bird photos either could be bird drawings or other mediums or a mix! Could be used for any photo gallery/tagging needs so get creative! : )

## Known Issues
- Blanks spaces work with using a tiny compleatly transparent image; this is jank and a better solution will improve this.
- Another jank is that horizontal rules take up 3 lines in image_data.js and must start in the leftmost column or else wont render properly.
- Only one photo resolution has really been tested (that being 4:3 and 3:4)
- Thumbnail script generates landscape thumbnails for portrait photos.
- Only been tested to work on Linux.

## License
GNU 3.0
