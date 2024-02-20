#Import the required library
from tkinter import*
#Create an instance of tkinter frame
win= Tk()
#Set the geometry
win.geometry("750x280")
#Create an canvas object
canvas= Canvas(win, width= 1000, height= 750)
#Load an image inside the canvas
smiley = PhotoImage(file="superhero.png")
#Create an image in the canvas object
image_item = canvas.create_image((200, 140), image=smiley)
#Bind the Button Event to the Canvas Widget
canvas.tag_bind(image_item, '<Button-1>', lambda e:
canvas.delete(image_item))
canvas.pack()
win.mainloop()