import customtkinter as ttk
from cogs.scrollbarframe import ScrollbarFrame
from cogs.load import Asset
from cogs.about import About
import subprocess    
import os
import datetime

class App(ttk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Name, Date Created , Modify Date, Size
        self.projects_data = [
            ['Game #1','2/8/2024','2/8/2024',3.8],
            ['Game #2','1/1/2024','2/8/2024',4.2],
            ['Gamehhhhhhhhhhhh #3','2/8/2024','4/3/2023',2.3],
            ['Game #4','4/3/2023','2/8/2024',2.3],
            ['Game #5','4/3/2023','2/8/2024',2.3],
            ['Game #6','4/3/2023','2/8/2024',2.3],
            ['Game #7','4/3/2023','2/8/2024',2.3],
            ['Game #8','4/3/2023','2/8/2024',2.3],
            ['Gamuuuuuuuuuue #9','4/3/2023','2/8/2024',2.3],
            ['Game #10','4/3/2023','2/8/2024',2.3],
            ['Game #11','4/3/2023','2/8/2024',2.3],
            ['Game #12','4/3/2023','2/8/2024',2.3],
            ['Game #13','4/3/2023','2/8/2024',2.3],
        ]


        self.title('SPM - Sratch Projects Manager')
        self.iconbitmap('./assets/ralsei.ico')
        self.resizable(False,False)


        # load assets
        self.asset = Asset()
        self.WORKSPACE = ''
        

        # main frame
        main_frame = ttk.CTkFrame(self, fg_color='#1e1e1e')
        main_frame.grid(column=0,row=0)
        main_frame.rowconfigure((0,1,2,3,4), weight=1, uniform='a')
        main_frame.columnconfigure((0,1,2,3,4), weight=1, uniform='a')

        # frame 1

        lable_frame_1 = ttk.CTkFrame(main_frame,width=1000,fg_color='#333333')
        lable_frame_1.grid(column=0,row=0,padx=25,pady=25,sticky='nsew',columnspan=4)

        search_entry = ttk.CTkEntry(lable_frame_1, width=300,placeholder_text='Search...',fg_color='#191919',border_color='#6f3131')
        search_entry.pack(side='left',padx=(25,0))

        clear_button = ttk.CTkButton(lable_frame_1,text_color='#ff4d4d',border_color='#ff4d4d',hover_color='#333333',fg_color="#333333", text='Clear', command=lambda: search_entry.delete(0,'end'), width=25, font=('Segoe UI',13))
        clear_button.bind("<Enter>", lambda e: clear_button.configure(font=('Segoe UI',13,"underline"), cursor="hand2"))
        clear_button.bind("<Leave>", lambda e: clear_button.configure(font=('Segoe UI',13), cursor="arrow"))
        clear_button.pack(side='left',padx=(10,25))

        value_inside = ttk.StringVar(self) 
        value_inside.set("Last Edited") 
        filter_options = ttk.CTkOptionMenu(
            lable_frame_1,
            fg_color='#323232',
            button_color='#323232',
            button_hover_color='#323232',
            dropdown_fg_color='#323232',
            text_color=self.asset.red,
            values=['Last Edited','Name','Size','Favorited'],
            width=110
        )
        filter_options.pack(side='left',padx=25)

        self.file_counter = ttk.CTkLabel(lable_frame_1, text_color=self.asset.red,text='69 files found.')
        self.file_counter.pack(side='left',padx=25)


        # frame 2

        lable_frame_2 = ttk.CTkFrame(main_frame, bg_color='#333333')
        lable_frame_2.grid(column=0,row=1,sticky='nsew',padx=25,rowspan=5,pady=(0,25),columnspan=4)

        # target frame
        sbf = ScrollbarFrame(lable_frame_2)
        sbf.pack(expand=True,fill='both',side='top')

        self.target_frame = sbf.scrolled_frame

        self.create_children()

        # frame 3

        lable_frame_3 = ttk.CTkFrame(main_frame)
        lable_frame_3.grid(column=4,row=0,rowspan=4,sticky='ns',padx=(0,25),pady=25)

        # styles

        ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_green,fg_color=self.asset.green,text_color=self.asset.black,compound='left',image=self.asset.new,text='New Project',width=20).pack(side='top',expand=True,fill='both',padx=10,pady=10)
        ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_blue,fg_color=self.asset.blue,text_color=self.asset.black,compound='left',image=self.asset.open,text='Open').pack(side='top',expand=True,fill='both',padx=10,pady=(0,10))
        workspace = ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_orange,fg_color=self.asset.orange,text_color=self.asset.black,compound='left',image=self.asset.workspace,text='Workspace')
        workspace.pack(side='top',expand=True,fill='both',padx=10,pady=(0,10))
        
        # workspace
        workspace.configure(command=self.choose_workspace)
        
        ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_orange,fg_color=self.asset.orange,text_color=self.asset.black,compound='left',image=self.asset.reload,text='Reload').pack(side='top',expand=True,fill='both',padx=10,pady=(0,10))
        ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_red,fg_color=self.asset.red,text_color=self.asset.black,compound='left',image=self.asset.rename,text='Rename').pack(side='top',expand=True,fill='both',padx=10,pady=(0,10))
        ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_red,fg_color=self.asset.red,text_color=self.asset.black,compound='left',image=self.asset.delete,text='Delete').pack(side='top',expand=True,fill='both',padx=10,pady=(0,10))
        ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_yellow,fg_color=self.asset.yellow,text_color=self.asset.black,compound='left',image=self.asset.favourite,text='Favourite').pack(side='top',expand=True,fill='both',padx=10,pady=(0,10))


        lable_frame_4 = ttk.CTkFrame(main_frame,border_width=1,fg_color='transparent')
        lable_frame_4.grid(column=4,row=4,rowspan=1,sticky='ns',padx=(0,25),pady=(0,25))


        self.toplevel_window = None
        # size, last edited, show in fe button
        # size_label = ttk.CTkLabel(lable_frame_4, text='Size: 69MB).pack(side='top',expand=True,fill='both',padx=10)
        # size_label = ttk.CTkLabel(lable_frame_4, text='Last Edited: 69/69/6969).pack(side='top',expand=True,fill='both',padx=10)
        reveal = ttk.CTkLabel(lable_frame_4,text='Reveal Workspace',font=('', 13), text_color="#4fa5e2")
        about = ttk.CTkLabel(lable_frame_4,text='About',font=('', 13), text_color="#4fa5e2")
        test = ttk.CTkLabel(lable_frame_4,text='About',font=('', 13), text_color="#4fa5e2")
        reveal.pack(side='top',expand=True,fill='both')
        test.pack(side='top',expand=True,fill='both')
        about.pack(side='top',expand=True,fill='both',pady=(0,15))
        # size_label = ttk.CTkLabel(lable_frame_4, text='Created Date: 69/69/6969').pack(side='top',expand=True,fill='both',padx=10)
        
        reveal.bind("<Button-1>", lambda e: subprocess.Popen(rf'explorer /select,"{self.WORKSPACE}"'))
        reveal.bind("<Enter>", lambda e: reveal.configure(font=('', 13, "underline"), cursor="hand2"))
        reveal.bind("<Leave>", lambda e: reveal.configure(font=('', 13), cursor="arrow"))
        
        about.bind("<Button-1>", lambda e: self.open_toplevel())
        about.bind("<Enter>", lambda e: about.configure(font=('', 13, "underline"), cursor="hand2"))
        about.bind("<Leave>", lambda e: about.configure(font=('', 13), cursor="arrow"))


    def choose_workspace(self):
        output = ttk.filedialog.askdirectory()
        if output != '': self.WORKSPACE = output

        print(self.WORKSPACE)

        file_list = []

        if self.WORKSPACE != '':
            # read workspace
            try: 
                for file in os.listdir(self.WORKSPACE):
                    name, extension  = os.path.splitext(file)
                    if extension == '.sb3':
                        created_date = os.path.getctime(f'{self.WORKSPACE}/{file}')
                        # created_date = datetime.datetime.fromtimestamp(created_date)

                        modify_date = os.path.getmtime(f'{self.WORKSPACE}/{file}')
                        # modify_date = datetime.datetime.fromtimestamp(modify_date)

                        size = os.path.getsize(f'{self.WORKSPACE}/{file}')
                        size = round(size/1024/1024,2)

                        file_list.append([name,created_date,modify_date,size])
            except:
                pass

            # overwrite projects list
            self.projects_data = file_list

            #destroy children (lmao)
            for child in self.target_frame.winfo_children():
                child.destroy()

            # make children
            self.create_children()

            # edit file count
            if len(self.projects_data) == 1:   
                self.file_counter.configure(text=f'{len(self.projects_data)} file found.')
            else:
                self.file_counter.configure(text=f'{len(self.projects_data)} files found.')
        
            
# Name, Date Created , Modify Date, Size

    def create_children(self):
        project_row = -1
        for name, created_date, modify_date, size in self.projects_data:
            project_row+=1
            self.create_item(self.target_frame, name, created_date, modify_date, size, project_row).grid(column=0,row=project_row)

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            print('hello')
            self.toplevel_window = About(root=self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def create_item(self, master, name:str, created_date:str , modify_date:str , size, style):
        frame = ttk.CTkFrame(master=master,corner_radius=0,bg_color='blue')
        frame.grid(column=0,row=0,sticky='nsew',ipady=20)

        frame.rowconfigure(0, weight = 1)
        frame.columnconfigure((0,1,2,3,4), weight = 1, uniform = 'a')

        # widgets 
        ttk.CTkButton(frame,hover_color='#6f3131',font=self.asset.font_bold,bg_color=self.asset.lighter_black,fg_color=self.asset.lighter_black,text_color=self.asset.white,corner_radius=0,text = name).grid(row = 0, column = 0, columnspan = 3,sticky='nsew')
        ttk.CTkButton(frame,fg_color=self.asset.lighter_black,text_color_disabled='#e2e6e9',state='disabled',corner_radius=0,text = '⠀').grid(row = 0, column = 3,sticky='nsew')
        size_label = ttk.CTkButton(frame,fg_color=self.asset.lighter_black,text_color_disabled='#e2e6e9',state='disabled',corner_radius=0)
        size_label.grid(row = 0, column = 4,sticky='nsew')
        if size == '': 
            size_label.configure(text='')
        else:
            size_label.configure(text=f'{size}MB')
        
        # ttk.CTkButton(frame, image=photo,width=5,.pack(side=LEFT,expand=True,fill=X,padx=5)
        # btn = ttk.CTkButton(frame,text=name,width=450,height=100)
        # btn.pack(side='left',expand=True,fill='both',padx=20,pady=20)
        return frame

app = App()
app.mainloop()