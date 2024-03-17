import customtkinter as ttk
from PIL import Image, ImageTk
import os
import pyperclip
from cogs.load import Asset

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

class About(ttk.CTkToplevel):
    def __init__(self, root,*args, **kwargs):
        super().__init__(*args, **kwargs)

        # x = root.winfo_x()
        # y = root.winfo_y()

        self.asset = Asset()
        # self.geometry("+%d+%d" % (x + 450, y + 200))
        self.resizable(False,False)
        self.title('About')
        self.after(200, lambda: self.iconbitmap(f'{ROOT_DIR}/assets/ralsei.ico'))
        self.after(250, self.lift)
        self.after(250, self.focus)
        self.grab_set()
        self.after(10, self._create_widgets)


    def _create_widgets(self):
        self.columnconfigure((0,1,2,3,4,5), weight=1)
        self.rowconfigure((0,1,2,3,4,5), weight=1)

        img = ImageTk.PhotoImage(Image.open(f'{ROOT_DIR}/assets/smoking_ralsei.png'))

        ttk.CTkLabel(self,image=img,text='').grid(column=0,row=2,padx=(25,0))

        self.label = ttk.CTkLabel(self, text_color='#ffffff',text="Scratch Projects Manager v0.1", font=('Varela Round',36,'bold','italic'))
        self.label2 = ttk.CTkLabel(self, text_color='#ffbf00',text="by Mount4in", font=('Varela Round',18))
        self.label3 = ttk.CTkLabel(
            self,
            text=
            "SPM is an offline file explorer for Scratch 3.\n"+
            "I came up this idea when I was bored.\n"+
            "With my lack of coding skill (I tried my best),\n"+
            "I've created this program so don't judge me lmao.\n",
            font=('Varela Round',18)
        )
        self.frame = ttk.CTkFrame(self,fg_color='transparent')
        self.label4 = ttk.CTkLabel(self.frame, text="Discord:", font=self.asset.font_small)
        self.label5 = ttk.CTkLabel(self.frame, text="notmountain", font=self.asset.font_small)
        ttk.CTkLabel(self, text='pls dont sue me for using smoking ralsei image :(',font=('Varela Round',8)).grid(sticky='w',column=5,row=3)
        self.copy = ttk.CTkLabel(self.frame, text="⠀ ⠀ ⠀ ⠀", font=self.asset.font_small,text_color='#4c97ff')

        self.label.grid(column=0,row=0,columnspan=6,padx=20, pady=(20,0))
        self.label2.grid(column=5,row=1,padx=0, pady=(0,20))
        self.label3.grid(column=1,row=2,padx=(25,25), pady=20,columnspan=5)
        self.frame.grid(column=0,row=3,padx=0, pady=20)

        
        self.label4.pack(side='left')

        self.label5.bind("<Button-1>", lambda e: self.copyText())
        self.label5.bind("<Enter>", lambda e: self.label5.configure(font=self.asset.font_small_underline, cursor="hand2"))
        self.label5.bind("<Leave>", lambda e: self.label5.configure(font=self.asset.font_small, cursor="arrow"))
        self.label5.pack(side='left',padx=(10,0))

        self.copy.pack(side='right',padx=(20,0),anchor='ne')

    def copyText(self):
        self.copy.configure(text='Copied!')
        pyperclip.copy(self.label5.cget('text'))

        return None
