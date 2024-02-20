import customtkinter as ttk
from cogs.load import Asset

class ScrollbarFrame(ttk.CTkFrame):
    def __init__(self, parent):
        ttk.CTkFrame.__init__(self, parent)

        self.asset = Asset()

        self.vsb = ttk.CTkScrollbar(self, orientation="vertical")
        self.vsb.pack(side="right", fill="y")

        # The Canvas which supports the Scrollbar Interface, layout to the left
        self.canvas = ttk.CTkCanvas(self,background=self.asset.black,highlightcolor=self.asset.black,highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Bind the Scrollbar to the self.canvas Scrollbar Interface
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.configure(command=self.canvas.yview)

        # The Frame to be scrolled, layout into the canvas
        # All widgets to be scrolled have to use this Frame as parent
        self.scrolled_frame = ttk.CTkFrame(self.canvas)
        self.scrolled_frame.pack(fill="x", expand=True)
        self.canvas.create_window((4, 4), window=self.scrolled_frame, anchor="nw")

        # Configures the scrollregion of the Canvas dynamically
        self.scrolled_frame.bind("<Configure>", self.on_configure)
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))

    def on_configure(self, event):
        # Set the scroll region to encompass the scrolled frame
        self.vsb.place_forget()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))