import tkinter as tk

window = tk.Tk()


# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Assume that this list gets updated automatically
events_list = []
# Run the event loop
while True:
    # If events_list is empty, the no events have occurred and we
    # can skip to the next iteration of the loop
    if events_list == []:
        continue
        # If execution reaches this point, then there is at least one
        # event object in events_list
    event = events_list[0]

    # If event is a keypress event object
    if event.type == "keypress":
        # Call the keypress event handler
        handle_keypress(event)

window.mainloop()
