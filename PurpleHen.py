import curses
import image_data #lol what a hack JS and PY use the same structure for lists/dictionarys so by using the .py instead of .js extension it can be read by both languages.
from PIL import Image, ImageOps
from os import listdir
from os.path import isfile, join

#=========================#
#     DEFAULT VALUES      #
#=========================#
default_location = ""
default_camera = ""
#=========================#

#varibles
timeout_speed = 500
selected_row = 0
x_scan_pos = 0
page_number = 0
is_user_typing = False
user_input = "Test Mctestface "
text_cur_pos = 0
save_to = ""
flip_to = ""
status = "Welcome!"
exif_date = ""

#setup curses
screen = curses.initscr()
height, width = screen.getmaxyx()
window = curses.newwin(height, width, 0, 0)
window.keypad(1)
curses.curs_set(False)
#curses.noecho()
#curses.cbreak()

#image data handling
image_set = image_data.imagedata #we need to append things so will create a local copy

#get a list of all files in images folder
files_without_entrys = [f for f in listdir("./images") if isfile(join("./images", f))]

#lets get a list of all sources in the dataset
file_sources = [] 
for x in range(len(image_set)): 
    file_sources.append(image_set[x]["source"])

#create a list of files in the images dir not present with entrys in image_data
files_without_entrys = list(set(files_without_entrys) - set(file_sources)) 

#take list of files without entrys and give them an entry
for x in files_without_entrys: 
    #generate thumbnail
    image = Image.open("./images/"+x)
    image = ImageOps.exif_transpose(image) #silly little orientation information, this works even if the image has no exif data
    #generate thumbnails
    image.thumbnail((640,480))
    image.save("./images/thumbs/"+x)
    #retrieve exif date data and check the image has some.
    try:
        exif_date = Image.open("./images/"+x)._getexif()[36867]
    except TypeError:
        exif_date = ""
    #add entry
    image_set.append({"source": x, "morph": "", "bird": "", "location": default_location, "date": exif_date, "camera": default_camera, "favourite": " F ", "new": " F ", "wild": " T "})

#split the image_data into pages of nth values each with nth being the rest of screen space from the terminal
image_page = [image_set[x:x+(height-4)] for x in range(0, len(image_set),(height-4))] 

#let the user know the programs doing stuff
status = "Welcome! " + str(len(files_without_entrys)) + " new photos found, generating thumbnails, extracting EXIF data, adding data entrys." 

#colors
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)

#functions
def draw_vertical_bar(pos):
    for x in range(len(image_page[page_number])+2):
        window.addstr(x+1,pos,"║")

def draw_column(key,title):
    global x_scan_pos
    draw_vertical_bar(x_scan_pos); x_scan_pos += 1; y = 0; cell_length = len(title)
    window.addstr(1,x_scan_pos,title)
    for x in image_page[page_number]:
        if y == selected_row:
            window.addstr(y+3,x_scan_pos,x[key],curses.color_pair(7)) #color highlight it

            if key == "source": #if key is source we then take the filename and save it too a file for the image viewer knows what to open
                f = open("send_image", "w") 
                f.write(x[key])
                f.close()
        else:
            window.addstr(y+3,x_scan_pos,x[key])
        if len(x[key]) > cell_length: #this tells x_scan_pos where to position itself based on the longest value found in the column
            cell_length = len(x[key])
        y += 1
    x_scan_pos += cell_length

def draw_function():
    global x_scan_pos
    x_scan_pos = 0
    window.addstr(0,0," "*width,curses.color_pair(1)) #make the header bar compleatly white even if the shortcuts dont fill the whole space
    window.addstr(0,0,"│ PAGE "+str(page_number)+" │ (S)ource │ (M)orph │ (B)ird │ (L)ocation │ (D)ate │ (C)amera │ (F)avourite │ (N)ew │ (W)ild │ (↵) Save │",curses.color_pair(1))

    window.addstr(2,0,"═"*width)

    #draw line numbers
    for x in range(len(image_page[page_number])):
        if x == selected_row:
            window.addstr(x+3,x_scan_pos+len(str(len(image_page[page_number])))-len(str(x)),str(x),curses.color_pair(7)) #highlight currently selected row and right justification
        else:
            window.addstr(x+3,x_scan_pos+len(str(len(image_page[page_number])))-len(str(x)),str(x)) #right justification
    x_scan_pos += len(str(len(image_page[page_number]))) #move the 'scanline' across so the new column doesnt draw ontop of the last

    draw_column("source","Source")
    draw_column("morph","Morph")
    draw_column("bird","Bird")
    draw_column("location","Location")
    draw_column("date","Date")
    draw_column("camera","Camera")
    draw_column("favourite","Fav")
    draw_column("new","New")
    draw_column("wild","Wild")

    #draw user input
    if is_user_typing == True:
        for x in range(len(user_input)):
            if x == text_cur_pos:
                window.addstr(height-1,x,user_input[x],curses.color_pair(1))
            else:
                window.addstr(height-1,x,user_input[x])
    else:
        window.addstr(height-1,0,status)

    #debug
    #window.addstr(3,11,str(selected_row))

#game loop
while True:
    window.timeout(timeout_speed)
    key = window.getch() #input initalize
    #keyboard input checker
    if is_user_typing == False:
        #data navagation
        if key == curses.KEY_DOWN and selected_row < len(image_page[page_number])-1:
            selected_row += 1; status = ""
        elif key == curses.KEY_UP and selected_row > 0:
            selected_row -= 1; status = ""
        elif key == curses.KEY_LEFT and page_number > 0:
            selected_row = 0; status = ""
            page_number -= 1
        elif key == curses.KEY_RIGHT and page_number < len(image_page)-1:
            selected_row = 0; status = ""
            page_number += 1
        #data editing
        elif key in (ord("S"),ord("M"),ord("B"),ord("L"),ord("C"),ord("D"),ord("s"),ord("m"),ord("b"),ord("l"),ord("c"),ord("d")): #check based off commands in header bar
            is_user_typing = True
            if key == ord("S") or key == ord("s"): save_to = "source"; user_input = image_page[page_number][selected_row]["source"]+" " #we append a blank space at the end so the text cursor can go to the end of a string and add stuff
            elif key == ord("M") or key == ord("m"): save_to = "morph"; user_input = image_page[page_number][selected_row]["morph"]+" "
            elif key == ord("B") or key == ord("b"): save_to = "bird"; user_input = image_page[page_number][selected_row]["bird"]+" "
            elif key == ord("L") or key == ord("l"): save_to = "location"; user_input = image_page[page_number][selected_row]["location"]+" "
            elif key == ord("C") or key == ord("c"): save_to = "camera"; user_input = image_page[page_number][selected_row]["camera"]+" "
            elif key == ord("D") or key == ord("d"): save_to = "date"; user_input = image_page[page_number][selected_row]["date"]+" "
            text_cur_pos = len(user_input)-1
        elif key in (ord("F"),ord("N"),ord("W"),ord("f"),ord("n"),ord("w")):
            if key == ord("F") or key == ord("f"): flip_to = "favourite"
            elif key == ord("N") or key == ord("n"): flip_to = "new"
            elif key == ord("W") or key == ord("w"): flip_to = "wild"
            #after working out what key was pressed flip the boolean value
            if image_page[page_number][selected_row][flip_to] == " F ":
                image_page[page_number][selected_row][flip_to] = " T "
            elif image_page[page_number][selected_row][flip_to] == " T ":
                image_page[page_number][selected_row][flip_to] = " F "
        #data saving
        elif key == 10: #10 is the enter key (sorry the return key, gotta remeber theyre different)
            f = open("new_image_data.py", "w")
            f.write("imagedata = [\n")
            for x in range(len(image_page)):
                for y in image_page[x]:
                    f.write(str(y)+"\n")
            f.write("];")
            f.close()
            status = "Successfully saved to new_image_data.py"
    else:
        #user input using ascii a-zA-Z0-9(),./_
        if key in (32, 40, 41, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122):
            user_input = user_input[:text_cur_pos] + chr(key) + user_input[text_cur_pos:] #so thats what immutable means
            text_cur_pos += 1
        elif key == curses.KEY_LEFT and text_cur_pos > 0:
            text_cur_pos -= 1
        elif key == curses.KEY_RIGHT and text_cur_pos < len(user_input)-1:
            text_cur_pos += 1
        elif key == curses.KEY_BACKSPACE and user_input != " ":
            user_input = user_input[:text_cur_pos-1] + user_input[text_cur_pos:]
            text_cur_pos -= 1
        elif key == 10: #10 is the enter key (sorry the return key, gotta remeber theyre different)
            user_input = user_input.rstrip(" ") #remove trailing whitespace
            image_page[page_number][selected_row][save_to] = user_input #save user input
            is_user_typing = False
            status = ""

    #draw loop
    window.clear()
    draw_function()

screen.refresh()
curses.endwin()
#I dont understand curses you cant draw the border after getch but you cant clear the window before getch. what am I missing this seems so abritrary.