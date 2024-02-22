import customtkinter as ctk
import tkinter as tk

def on_mouse_wheel(event):
    if event.delta:
        canvas.yview_scroll(-1*(event.delta//120), "units")

def on_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    update_scrollbars()

def update_scrollbars():
    if canvas.winfo_height() < canvas.canvasy(1):
        vbar.pack(side="right", fill="y")
    else:
        vbar.pack_forget()

    if canvas.winfo_width() < canvas.canvasx(1):
        hbar.pack(side="bottom", fill="x")
    else:
        hbar.pack_forget()

root = tk.Tk()
root.title("Scrollbar Example")

# Create a Canvas widget
canvas = ctk.CTkCanvas(root, width=400, height=300, scrollregion=(0, 0, 1000, 1000))
canvas.pack(side="left", fill="both", expand=True)

# Create a Scrollbar for vertical scrolling
vbar = ctk.CTkFrame(root, width=10, height=300)
canvas.set_vertical_scrollbar(vbar)

# Create a Scrollbar for horizontal scrolling
hbar = ctk.CTkFrame(root, width=400, height=10)
canvas.set_horizontal_scrollbar(hbar)

# Bind mouse scroll to canvas scrolling
canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# Bind scroll event to update scroll region and scrollbars
canvas.bind("<Configure>", on_scroll)

# Create a frame to hold content in the canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Add some widgets inside the frame
for i in range(50):
    tk.Label(frame, text=f"Label {i}").pack()

# Update scroll region and scrollbars initially
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))
update_scrollbars()

root.mainloop()
