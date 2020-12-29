# Author Harriet Poe
# This program will generate short story prompt topics

import random

subjectItems = ["woman", "cat", "dog", "man", "fish", "child", "shoe", "sweater", "mouse", "bottle", "lamp", "Teacher",
                "Student", "Athlete", "Swimmer", "Programmer", "Runner", "Umbrella", "Pirate", "Chicken", "Biker",
                "Prince", "Princess", "King", "Queen", "girl", "boy"]

connectionItems = ["\b's", "and the", "in the", "on the", "with the", "at the", "of", "\b"]

placeItems = ["ship", "plane", "house", "dewdrop", "car", "truck", "country", "city", "town", "bottle", "school",
              "office", "pool", "spaceship", "bowl", "plate", "box", "road", "highway", "Palace", "Kingdom"]

randSub = random.randint(0, len(subjectItems) - 1)
subject = subjectItems[randSub]

randConn = random.randint(0, len(connectionItems) - 1)
connection = connectionItems[randConn]

randPlace = random.randint(0, len(placeItems) - 1)
place = placeItems[randPlace]

print("The", subject, connection, place)
