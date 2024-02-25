import customtkinter as ctk

# Define a function to be called when the selection changes
def on_select(selection):
    print("Selected option:", selection)

# Create a customtkinter application window
window = ctk.CTk()
window.title("OptionMenu Example")

# Define options for the OptionMenu
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Create the OptionMenu widget

option_menu = ctk.CTkOptionMenu(window, values=options, command=on_select)
option_menu.pack()

# Run the customtkinter event loop
window.mainloop()
