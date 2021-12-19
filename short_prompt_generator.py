# Author H J Poe
# This program will generate short story prompt topics

import random
from tkinter import *
from tkinter.font import Font

subjectItems = ["woman", "cat", "dog", "man", "fish", "child", "shoe", "sweater", "mouse", "bottle", "lamp", "Teacher",
                "Student", "Athlete", "Swimmer", "Programmer", "Runner", "Umbrella", "Pirate", "Chicken", "Biker",
                "Prince", "Princess", "King", "Queen", "girl", "boy"]

connectionItems = ["who had a", "and the", "in the", "on the", "with the", "at the", "of", "who owned a", "of the"]

placeItems = ["ship", "plane", "house", "dewdrop", "car", "truck", "country", "city", "town", "village", "bottle",
              "school", "office", "pool", "spaceship", "bowl", "plate", "cup", "fork", "knife", "spoon", "book", "box",
              "road", "highway", "path", "Palace", "Kingdom", "Castle"]

randSub = random.randint(0, len(subjectItems) - 1)
subject = subjectItems[randSub]

randConn = random.randint(0, len(connectionItems) - 1)
connection = connectionItems[randConn]

randPlace = random.randint(0, len(placeItems) - 1)
place = placeItems[randPlace]

text = "The" + ' ' + subject + ' ' + connection + ' ' + place

bg_color = '#2a5aad'
fg_color = '#0b1629'

window = Tk()

window.geometry('480x100')
window.title("Short Prompt Generator")
window.config(bg=bg_color)
font = Font(family='Arial', size=16)
label = Label(window, text=text, relief='flat')
label.config(bg=bg_color, fg=fg_color)
label.config(font=font)
label.pack(padx=30, pady=30)

window.mainloop()
