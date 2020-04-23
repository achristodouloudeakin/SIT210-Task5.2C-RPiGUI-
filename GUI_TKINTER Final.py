import RPi.GPIO as gpio

from tkinter import *
from gpiozero import LED

gpio.setmode(gpio.BCM)


# Hardware
red = LED(24)
green = LED(23)
blue = LED(18)

# GUI Definitions
win_gui = Tk()
win_gui.title("LED Toggler")


# Toggle Red Light
def toggle_red():
	if red.is_lit:
		red.off()
		button_red["text"] = "Toggle Red Led On"
	else:
		red.on()
		button_red["text"] = "Toggle Red Led Off"


# Toggle Green Light
def toggle_green():
        if green.is_lit:
                green.off()
                button_green["text"] = "Toggle Green Led On"
        else:
                green.on()
                button_green["text"] = "Toggle Green Led Off"

# Toggle Blue Light
def toggle_blue():
	if blue.is_lit:
		blue.off()
		button_blue["text"] = "Toggle Blue Led On"
	else:
		blue.on()
		button_blue["text"] = "Toggle Blue Led Off"

# Toggle GUI exit
def toggle_close():
	gpio.cleanup()
	win_gui.destroy()


##### GUI Widgets ####

# Red Button
button_red = Button(win_gui, text = 'Toggle Red Led On', command = toggle_red, bg = 'bisque2',height =1, width = 24)
button_red.grid(row=0,column=1)


# Green Button
button_green = Button(win_gui, text = 'Toggle Green Led On', command = toggle_green,bg = 'bisque2',height =1, width = 24)
button_green.grid(row=1,column=1)


# Blue Button
button_blue = Button(win_gui, text = 'Toggle Blue Led On', command = toggle_blue,bg = 'bisque2',height =1, width = 24)
button_blue.grid(row=2,column=1)

# Exit Button
exitButton = Button(win_gui, text = 'Exit', command = toggle_close,bg ='red',height =1, width = 6)
exitButton.grid(row=3,column=1)


# Clean exit from window 'x'
win_gui.protocol("WM DELETE WINDOW",toggle_close)

# Loop program forever
win_gui.mainloop()