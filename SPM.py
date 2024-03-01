import customtkinter as ttk
from cogs.scrollbarframe import ScrollbarFrame
from cogs.load import Asset
from cogs.about import About
import subprocess    
import os
import datetime
from configparser import ConfigParser

class App(ttk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.projects_data = []
        self.current_projects_data = []

        self.title('SPM - Sratch Projects Manager')
        self.iconbitmap('./assets/ralsei.ico')
        self.resizable(False,False)


        # load assets
        self.asset = Asset()
        self.WORKSPACE = ''
        self.load_settings()  

        # main frame
        self.main_frame()
        # frame 1
        self.lbf1()
        # frame 2
        self.lbf2()
        # frame 3
        self.lbf3()
        # frame 4
        self.lbf4()
        # framw 5
        self.lbf5()

        self.change_workspace(workspace=self.WORKSPACE)

    def main_frame(self):
        self.main_frame = ttk.CTkFrame(self, fg_color='#1e1e1e')
        self.main_frame.grid(column=0,row=0)
        self.main_frame.rowconfigure((0,1,2,3,4), weight=1, uniform='a')
        self.main_frame.columnconfigure((0,1,2,3,4), weight=1, uniform='a')

    def lbf1(self):
        lable_frame_1 = ttk.CTkFrame(self.main_frame,width=1000,fg_color='#333333')
        lable_frame_1.grid(column=0,row=0,padx=25,pady=25,sticky='nsew',columnspan=4)

        self.search_entry = ttk.CTkEntry(lable_frame_1, width=300,placeholder_text='Search...',fg_color='#191919',border_color='#6f3131')
        self.search_entry.pack(side='left',padx=(25,0),expand=True,fill='x')
        self.search_entry.bind('<KeyRelease>', self.update_entry)

        # clear_button = ttk.CTkButton(lable_frame_1,text_color='#ff4d4d',border_color='#ff4d4d',hover_color='#333333',fg_color="#333333", text='Clear', command=lambda: self.search_entry.delete(0,'end'), width=25, font=('Segoe UI',13))
        # clear_button.bind("<Enter>", lambda e: clear_button.configure(font=('Segoe UI',13,"underline"), cursor="hand2"))
        # clear_button.bind("<Leave>", lambda e: clear_button.configure(font=('Segoe UI',13), cursor="arrow"))
        # clear_button.pack(side='left',padx=(10,25))

        value_inside = ttk.StringVar(self) 
        value_inside.set("Last Edited") 
        filter_options = ttk.CTkOptionMenu(
            lable_frame_1,
            fg_color='#323232',
            button_color='#323232',
            button_hover_color='#323232',
            dropdown_fg_color='#323232',
            text_color=self.asset.red,
            values=[
                'Recently Modified',
                'Latest Modified',
                'Oldest',
                'Newest',
                'Name',
                'Name (Reversed)',
                'Biggest',
                'Smallest',
                'Favorited'
                ],
            width=150,
            command=self.update_filter,
        )

        filter_options.pack(side='left',padx=25)

        self.file_counter = ttk.CTkLabel(lable_frame_1, text_color=self.asset.red,text='')
        self.file_counter.pack(side='left',padx=25)
        
    def lbf2(self):

        lable_frame_2 = ttk.CTkFrame(self.main_frame)
        lable_frame_2.grid(column=0,row=1,sticky='nsew',padx=25,rowspan=3,pady=(0,25),columnspan=4)

        # target frame
        sbf = ScrollbarFrame(lable_frame_2)
        sbf.pack(expand=True,fill='both',side='top')

        self.target_frame = sbf.scrolled_frame
        
    def lbf3(self):

        lable_frame_3 = ttk.CTkFrame(self.main_frame)
        lable_frame_3.grid(column=4,row=0,rowspan=4,sticky='ns',padx=(0,25),pady=25)

        # styles

        ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_green,fg_color=self.asset.green,text_color=self.asset.black,compound='left',image=self.asset.new,text='New Project',width=20).pack(side='top',expand=True,fill='both',padx=10,pady=10)
        ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_blue,fg_color=self.asset.blue,text_color=self.asset.black,compound='left',image=self.asset.open,text='Open').pack(side='top',expand=True,fill='both',padx=10,pady=(0,10))
        workspace = ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_orange,fg_color=self.asset.orange,text_color=self.asset.black,compound='left',image=self.asset.workspace,text='Workspace')
        workspace.pack(side='top',expand=True,fill='both',padx=10,pady=(0,10))
        workspace.configure(command=self.workspace_btn)
        
        reload_btn = ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_orange,fg_color=self.asset.orange,text_color=self.asset.black,compound='left',image=self.asset.reload,text='Reload')
        reload_btn.pack(side='top',expand=True,fill='both',padx=10,pady=(0,10))
        reload_btn.configure(command=self.reload_btn)

        ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_red,fg_color=self.asset.red,text_color=self.asset.black,compound='left',image=self.asset.rename,text='Rename').pack(side='top',expand=True,fill='both',padx=10,pady=(0,10))
        ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_red,fg_color=self.asset.red,text_color=self.asset.black,compound='left',image=self.asset.delete,text='Delete').pack(side='top',expand=True,fill='both',padx=10,pady=(0,10))
        ttk.CTkButton(lable_frame_3,hover_color=self.asset.hover_yellow,fg_color=self.asset.yellow,text_color=self.asset.black,compound='left',image=self.asset.favourite,text='Favourite').pack(side='top',expand=True,fill='both',padx=10,pady=(0,10))
        
    def lbf4(self):
        lable_frame_4 = ttk.CTkFrame(self.main_frame,border_width=1,fg_color='transparent')
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

    def lbf5(self):
        lable_frame_5 = ttk.CTkFrame(self.main_frame)
        lable_frame_5.grid(column=0,row=4,padx=25,pady=(0,25),columnspan=4,sticky='nsew')

        ttk.CTkLabel(lable_frame_5,text='hello').pack()


    def load_settings(self):
        if 'settings.ini' in os.listdir('./'):
            print('Found settings.ini!')
        else:
            print('Missing settings.ini file, creating one...')
            nf = ConfigParser()
            nf.add_section('settings')
            nf['settings']['wsdir'] = 'C:/'
            with open('settings.ini','w') as f:
                nf.write(f)

        f = ConfigParser()
        f.read('settings.ini')
        
        self.WORKSPACE = f['settings']['wsdir']

    def workspace_btn(self):
        ws = self.choose_workspace()
        if ws is None:
            return
        else:
            self.change_workspace(workspace=ws)

    def change_workspace(self, workspace: str):
        self.WORKSPACE = workspace
        file_list = []

        file_list = self.load_files_from_workspace(workspace=workspace)
        self.edit_stuff_after_change_workspace(filelist=file_list)

    def choose_workspace(self) -> str | None:
        output = ttk.filedialog.askdirectory()
        if output == '': 
            return None
        else:
            return output

    def load_files_from_workspace(self, workspace) -> list[list]:
        fl = []
        for file in os.listdir(workspace):
            name, extension  = os.path.splitext(file)
            if extension == '.sb3':
                created_date = os.path.getctime(f'{workspace}/{file}')
                # created_date = datetime.datetime.fromtimestamp(created_date)

                modified_date = os.path.getmtime(f'{workspace}/{file}')
                # modify_date = datetime.datetime.fromtimestamp(modify_date)

                size = os.path.getsize(f'{workspace}/{file}')
                size = round(size/1024/1024,2)

                fl.append([name,created_date,modified_date,size])
        
        return fl

    def edit_stuff_after_change_workspace(self, filelist: list[list], overwrite:bool = True, overwrite_current:bool = True) -> None:

        #destroy children (lmao)
        for child in self.target_frame.winfo_children():
            child.destroy()

        # make children
        self.create_children(filelist=filelist)

        # edit file count
        if len(filelist) == 1:   
            self.file_counter.configure(text=f'{len(filelist)} file found.')
        else:
            self.file_counter.configure(text=f'{len(filelist)} files found.')

        # overwrite projects list
        if overwrite: 
            self.projects_data = filelist

        if overwrite_current:
            self.current_projects_data = filelist

        # save workspace to settings.ini
        self.edit_settings('settings','wsdir',self.WORKSPACE)

    def edit_settings(self, section: str, option:str, edit_to:str):
        nf = ConfigParser()
        nf.read('settings.ini')

        if section not in nf.sections():
            nf.add_section(section)
        
        nf[section][option] = edit_to

        with open('settings.ini','w') as f:
            nf.write(f)
        
    def create_children(self, filelist:list[list] = None):
        if filelist is None: filelist = self.projects_data
        project_row = -1
        for name, created_date, modify_date, size in filelist:
            project_row+=1
            self.create_item(self.target_frame, name, created_date, modify_date, size, project_row).grid(column=0,row=project_row)

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            print('hello')
            self.toplevel_window = About(root=self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def create_item(self, master, name:str, created_date:str , modified_date:str , size, style):
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

    def reload_btn(self) -> None:
        self.edit_stuff_after_change_workspace(self.projects_data)
        self.search_entry.delete(0,'end')

    def update_entry(self, e) -> None:
        typed = self.search_entry.get()

        result = []
        if typed == '':
            result = self.projects_data
        else:
            for project in self.projects_data:
                if typed.lower() in project[0].lower():
                    result.append(project)

        self.edit_stuff_after_change_workspace(result, overwrite=False)

    def update_filter(self, selection):
        print(self.current_projects_data)

        # Name, Modified Date, Created Date, Size, Favourited

        sorted_list = []
        if selection == 'Recently Modified':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[0])
        elif selection == 'Latest Modified':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[0],reverse=True)
        elif selection == 'Oldest':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[1])
        elif selection == 'Newest':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[1],reverse=True)
        elif selection == 'Name':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[2])
        elif selection == 'Name (Reversed)':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[2],reverse=True)
        elif selection == 'Biggest':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[3])
        elif selection == 'Smallest':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[3],reverse=True)
        elif selection == 'Favourited':
            ...

        self.edit_stuff_after_change_workspace(sorted_list, overwrite=False, overwrite_current=False)
            

app = App()
app.mainloop()