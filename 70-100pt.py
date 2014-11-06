##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

# Body of house
rect1 = drawpad.create_rectangle(300,300,500,500,fill='red')

# Roof 
line1 = drawpad.create_line(250,300,400,200)
line2 = drawpad.create_line(550,300,400,200)
line3 = drawpad.create_line(550,300,250,300)

#windows
window1 = drawpad.create_rectangle(350,350,375,375,fill='white')
window2 = drawpad.create_rectangle(450,350,425,325,fill='white')

#door
door = drawpad.create_rectangle(415,500,385,450,fill='white')

root.mainloop()
