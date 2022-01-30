import tkinter
from PIL import ImageTk, Image
import os

# creating main window
root = tkinter.Tk()
  
# loading the image
image = Image.open("StressFlow.jpeg")
resize_img = image.resize((400,400))
img = ImageTk.PhotoImage(resize_img)

# reading the image
panel = tkinter.Label(root, image = img)
  
# setting the application
panel.pack(side = "bottom", fill = "both",
           expand = "yes")
# running the application
root.mainloop()