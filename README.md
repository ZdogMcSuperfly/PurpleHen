# 'PurpleHen' <sub>v2</sub>
## Photo gallery and photo tagging for birders.

<p align="center"><br>
<img src="https://github.com/ZdogMcSuperfly/PurpleHen/blob/main/favicon.svg"></p>

I love birding, computers, data hoarding and collecting (same same). I made this software to nice and neatly display my photos in a way for me to enjoy and also to host it online to make sharing photos with friends and family easy too. I'm sure others could get some use out of this and improve apon it but I'm mainly hosting it on GitHub because Git is cool. 😎
## Features
- Frontend designed to display photos nicely.
- Seven different tag types to add to photos.
- Buttons to sort the gallery display based on tags.
- Script to automate the metadata creation for batches of photos.
- Script to generate thumbnails for batches of photos.
- Can be hosted online or used offline.
- Works on desktop and on mobile.

## User Interface
__Consists of two main sections:__<br>
A header that stays at the top of the page regardless of scrolling with infomation on the left (instructions to the user, current ammount of photos, and photo liceance), buttons in the middle for sorting photos (new photos, favorite photos, wild photos, captive photos, photos by country, and all photos), a heading and space for displaying descripts, and finally on the right a space for a logo or signature.<br><br>
A gallery that displays photos on a single page in columns of three. Can show portrait and landscape photos next to each other and when hovering displays metadata of the photo below the buttons in the header. Horizontal rules and blank spaces can be inserted to seperate and organize photos.

## Installation
```sh
git clone https://github.com/ZdogMcSuperfly/PurpleHen.git
```
## Usage
Sorting by country works by appending ISO 3166-1 alpha-3 codes to the end of the "location" tag.

## Customizing Ideas
On my copy I have the "Favorites" button renamed to "Lifelist" and I use it too display one photo per species like what a lifelist is.
For my logo I have the bird emoji (1F426, 🐦) so each device I visit my copy on I see a different glyph due to devices having different fonts. It's like Unicode birding.

## Known Issues
- Automation scripts are not fully automatic and are not explicitly user friendly.
- Blanks spaces work with using a tiny compleatly transparent image; this is jank and a better solution will improve this.
- Another jank is that horizontal rules take up 3 lines in image_data.js and must start in the leftmost column or else wont render properly.
- I cant think of a better name than PurpleHen, any ideas are appreciated.

## License
GNU 3.0
