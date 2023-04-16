import easygui as gui

# gui.msgbox(msg="Hello!", title="My first message box")
# gui.msgbox(msg="Hello!", title="Greeting", ok_button="Click me")

# print(gui.buttonbox(
# msg="What is your favorite color?",
# title="Choose wisely...",
# choices=("Red", "Yellow", "Blue"),))

# print(gui.indexbox(
# msg="What is your favorite color?",
# title="Choose wisely...",
# choices=("Red", "Yellow", "Blue"),))


# print(gui.enterbox(
# msg="What is your favorite color?",
# title="Favorite color",
# ))

gui.fileopenbox(title="Select a file")


"""

msgbox() A dialog box for displaying a message with a
single button. It returns the label of the button.
buttonbox() A dialog box with several buttons. It returns the
label of the selected button.
indexbox() A dialog box with several buttons. It returns the
index of the selected button.
enterbox() A dialog box with a text entry box. It returns the
text entered.
fileopenbox() A dialog box for selecting a file to be opened. It
returns the absolute path to the selected file.
diropenbox() A dialog box for selecting a directory to be
opened. It returns the absolute path to the
selected directory.
filesavebox() A dialog box for saving a file. It returns the
absolute path to the location for saving the file

"""

