import customtkinter as ttk
from PIL import Image, ImageTk
import os
from customtkinter import CTkButton, CTkLabel, CTkEntry
from cogs.load import Asset


ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


class Input(ttk.CTkToplevel):
    def __init__(self, root, text:str = 'Enter something here:', window_title:str = 'Input',*args, **kwargs):
        super().__init__(fg_color='#191919',*args, **kwargs)

        self.text = text
        self.window_title = window_title
        self.asset = Asset()

        # x = root.winfo_x()
        # y = root.winfo_y()

        # self.geometry("+%d+%d" % (x + 450, y + 200))
        self.return_value_signal = None
        self.resizable(False,False)
        self.title(self.window_title)
        self.after(200, lambda: self.iconbitmap(f'{ROOT_DIR}/assets/ralsei.ico'))
        self.after(200, self.lift)
        self.after(200, self.focus)
        self.grab_set()
        self.after(10, self._create_widgets)  # create widgets with slight delay, to avoid white flickering of background

    def _ok_button(self):
        self.value_on_close = self._entry.get()
        if self.return_value_signal:
            self.return_value_signal.emit(self.value_on_close)
        self.destroy()

    def _cancel_button(self):
        self.destroy()

    def connect_return_value_signal(self, signal):
        self.return_value_signal = signal


    def _create_widgets(self):

        self.grid_columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        self._label = CTkLabel(master=self,
                               width=300,
                               wraplength=300,
                               fg_color="transparent",
                               text=self.text,
                               font=self.asset.font_small)
        self._label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")
        self._entry = CTkEntry(master=self,
                               width=230,
                               fg_color='#191919',
                               border_color='#6f3131',
                               placeholder_text='New Project',
                               font=self.asset.font_small)
        self._entry.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="ew")

        self._ok_button = CTkButton(master=self,
                                    width=100,
                                    border_width=2,
                                    fg_color='transparent',
                                    corner_radius=0,
                                    border_color='#a5a5a5',
                                    hover_color='#a5a5a5',
                                    text='Ok',
                                    font=self.asset.font_small,
                                    command=self._ok_button)
        self._ok_button.grid(row=2, column=0, columnspan=1, padx=(20, 10), pady=(0, 20), sticky="ew")

        self._cancel_button = CTkButton(master=self,
                                        width=100,
                                        border_width=2,
                                        fg_color='transparent',
                                        corner_radius=0,
                                        border_color='#a5a5a5',
                                        hover_color='#a5a5a5',
                                        text='Cancel',
                                        font=self.asset.font_small,
                                        command=self._cancel_button)
        self._cancel_button.grid(row=2, column=1, columnspan=1, padx=(10, 20), pady=(0, 20), sticky="ew")

        self.after(150, lambda: self._entry.focus())  # set focus to entry with slight delay, otherwise it won't work
