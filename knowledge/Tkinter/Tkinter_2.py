import tkinter as tk
window = tk.Tk()
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)


def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")
button.bind("<Button-1>", handle_click)
"""
In this example, the "<Button-1>" event on the button widget is bound
to the handle_click event handler. The "<Button-1>" event occurs whenever
the left mouse button is pressed while the mouse is over the widget.
There are other events for mouse button clicks including "<Button-2>"
for the middle mouse button, if one exists, and "<Button-3>" for the
right mouse button.


"""

window.mainloop()