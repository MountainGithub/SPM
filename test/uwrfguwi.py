import ttkbootstrap as ttk
from ttkbootstrap.constants import *

projects_data = (
    ('FPS Game','C:/Users/Admin/Downloads/FPS Game.sb3','2/8/2024',3.8),
    ('RPG Game','C:/Users/Admin/Desktop/RPG Game.sb3','1/1/2024',4.2),
    ('Endless Game','C:/Users/Admin/Downloads/Endless Game.sb3','4/3/2023',2.3),
    ('FPS Game','C:/Users/Admin/Downloads/FPS Game.sb3','2/8/2024',3.8),
    ('RPG Game','C:/Users/Admin/Desktop/RPG Game.sb3','1/1/2024',4.2),
    ('Endless Game','C:/Users/Admin/Downloads/Endless Game.sb3','4/3/2023',2.3),
    ('FPS Game','C:/Users/Admin/Downloads/FPS Game.sb3','2/8/2024',3.8),
    ('RPG Game','C:/Users/Admin/Desktop/RPG Game.sb3','1/1/2024',4.2),
    ('Endless Game','C:/Users/Admin/Downloads/Endless Game.sb3','4/3/2023',2.3),
    ('FPS Game','C:/Users/Admin/Downloads/FPS Game.sb3','2/8/2024',3.8),
    ('RPG Game','C:/Users/Admin/Desktop/RPG Game.sb3','1/1/2024',4.2),
    ('Endless Game','C:/Users/Admin/Downloads/Endless Game.sb3','4/3/2023',2.3),
)

def create_item(master, name:str, path:str, date:str, size:float):
    frame = ttk.Frame(master=master,width=300)
    
    ttk.Label(frame, text=name).grid(column=0,row=0,sticky='NW',padx=(0,50))
    ttk.Label(frame, text=path).grid(column=0,row=1,sticky='SW',padx=(0,50))
    ttk.Label(frame, text=date).grid(column=1,row=0,sticky='NE')
    ttk.Label(frame, text=f"{size}MB").grid(column=1,row=1,sticky='SE')
    
    return frame

class ScrollbarFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)

        # The Scrollbar, layout to the right
        vsb = ttk.Scrollbar(self, orient="vertical")
        vsb.pack(side="right", fill="y")

        # The Canvas which supports the Scrollbar Interface, layout to the left
        self.canvas = ttk.Canvas(self, borderwidth=0, background="#ffffff")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Bind the Scrollbar to the self.canvas Scrollbar Interface
        self.canvas.configure(yscrollcommand=vsb.set)
        vsb.configure(command=self.canvas.yview)

        # The Frame to be scrolled, layout into the canvas
        # All widgets to be scrolled have to use this Frame as parent
        self.scrolled_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((4, 4), window=self.scrolled_frame, anchor="nw")

        # Configures the scrollregion of the Canvas dynamically
        self.scrolled_frame.bind("<Configure>", self.on_configure)

    def on_configure(self, event):
        # Set the scroll region to encompass the scrolled frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


class App(ttk.Window):
    def __init__(self):
        super().__init__()

        sbf = ScrollbarFrame(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        sbf.grid(row=0, column=0, sticky='nsew')
        # sbf.pack(side="top", fill="both", expand=True)

        # Some data, layout into the sbf.scrolled_frame
        frame = sbf.scrolled_frame
        project_row = -1
        for name, path, date, size in projects_data:
            project_row+=1
            create_item(frame, name, path, date, size).grid(column=0,row=project_row)


if __name__ == "__main__":
    App().mainloop()