import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 

im = Image.open("times-up.jpeg")

# ask user to enter desired countdown time
set_time = int(input("Please set your timer in seconds: "))

#give insturctions to let players stand
print('Players stand!')

time.sleep(set_time)
print("Time's up!")

im.show()

#ask users to enter the player sit down last and those who didn't sit down
last_player = input("Please enter the name of the last player to sit down.")
not_seated = input("Please enter the name of players who are not seated, separated by ;")

#print out the result
print("The winner is: " + last_player)
print("Players not seated: " + not_seated)
