from tkinter import *
from PIL import ImageTk, Image #tkinter cant read .jpg out of the box?  
import image_data

#varibles
image_to_draw = "./images/thumbs/"+image_data.imagedata[0]["source"]

#setup tkinter
root = Tk()
canvas = Canvas(root, width = 640, height = 640)
canvas.pack()
img = ImageTk.PhotoImage(Image.open(image_to_draw))  
canvas.create_image(0,0, anchor=NW, image=img)

#functions
def refresh_tkinter():
    f = open("send_image", "r")
    image_to_draw = "./images/thumbs/"+f.read()
    img = ImageTk.PhotoImage(Image.open(image_to_draw))  
    f.close()

    canvas.delete("all")
    canvas.img = ImageTk.PhotoImage(Image.open(image_to_draw))  
    canvas.create_image(0,0, anchor=NW, image=canvas.img)
    canvas.config(width=img.width(), height=img.height())
    root.after(300, refresh_tkinter)

refresh_tkinter()
mainloop()