import customtkinter as ttk
from PIL import Image, ImageTk
import os

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


class Asset():
    def __init__(self) -> None:

        """
        New Project
        Open
        Workspace
        Reload
        Rename
        Favorite
        """

        # images

        # self.delete = ImageTk.PhotoImage(Image.open(f'{ROOT_DIR}/assets/delete.png'))
        self.delete = ttk.CTkImage(Image.open(f'{ROOT_DIR}/assets/delete.png'))
        self.favourite = ttk.CTkImage(Image.open(f'{ROOT_DIR}/assets/favourite.png'))
        self.new = ttk.CTkImage(Image.open(f'{ROOT_DIR}/assets/new.png'))
        self.open = ttk.CTkImage(Image.open(f'{ROOT_DIR}/assets/open.png'))
        self.reload = ttk.CTkImage(Image.open(f'{ROOT_DIR}/assets/reload.png'))
        self.rename = ttk.CTkImage(Image.open(f'{ROOT_DIR}/assets/rename.png'))
        self.workspace = ttk.CTkImage(Image.open(f'{ROOT_DIR}/assets/workspace.png'))

        # font
        self.font_bold = ttk.CTkFont(family='Segoe UI',size=16)
        # self.font = ttk.CTkFont(family='Azeret Mono Medium',size=12)
        # self.font = ttk.CTkFont(family='Sans Serif',size=12,weight='bold')

        # color
        self.red = '#ff4d4d'
        self.dark_red = '#882f2f'
        self.light_red = '#f2735a'
        self.black = '#111111'
        self.light_black = '#1e1e1e'
        self.lighter_black = '#2e2e2e'
        self.green = '#4cbf56'
        self.yellow = '#ffbf00'
        self.clay = '#94a0c7'
        self.white = '#ffffff'
        self.blue = '#4c97ff'
        self.orange = '#ff8c1a'
        self.hover_green = '#8cff96'
        self.hover_blue = '#8cd7ff'
        self.hover_orange = '#ffcc5a'
        self.hover_red = '#ff8d8d'
        self.hover_yellow = '#ffff40'



