import customtkinter as ttk
from cogs.scrollbarframe import ScrollbarFrame
from cogs.load import Asset
from cogs.about import About
import subprocess    
import os
from datetime import datetime
from configparser import ConfigParser
import shutil

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
        self.main_frame = ttk.CTkFrame(self, fg_color='#191919')
        self.main_frame.grid(column=0,row=0)
        self.main_frame.rowconfigure((0,1,2,3,4), weight=1, uniform='a')
        self.main_frame.columnconfigure((0,1,2,3,4), weight=1, uniform='a')

    def lbf1(self):
        lable_frame_1 = ttk.CTkFrame(self.main_frame,width=1000,fg_color='#1e1e1e')
        lable_frame_1.grid(column=0,row=0,padx=25,pady=25,sticky='nsew',columnspan=4)

        self.search_entry = ttk.CTkEntry(lable_frame_1, width=200,placeholder_text='Search...',fg_color='#191919',border_color='#6f3131')
        self.search_entry.pack(side='left',padx=(25,0),expand=True,fill='x')
        self.search_entry.bind('<KeyRelease>', self.update_entry)


        self.value_inside = ttk.StringVar(self) 
        self.value_inside.set("Filter") 
        self.filter_options = ttk.CTkOptionMenu(
            lable_frame_1,
            fg_color='#1e1e1e',
            button_color='#1e1e1e',
            button_hover_color='#1e1e1e',
            dropdown_fg_color='#1e1e1e',
            corner_radius=3,
            text_color=self.asset.red,
            values=[
                'Recently Modified',
                'Not Recently Modified',
                'Newest',
                'Oldest',
                'Name',
                'Name (Reversed)',
                'Biggest',
                'Smallest',
                'Favorited'
                ],
            variable=self.value_inside,
            width=175,
            command=self.update_filter,
        )

        self.filter_options.pack(side='left',padx=25)

        self.file_counter = ttk.CTkLabel(lable_frame_1, text_color=self.asset.red, fg_color='#1e1e1e',corner_radius=3,text='')
        self.file_counter.pack(side='left',padx=25)
        
    def lbf2(self):

        lable_frame_2 = ttk.CTkFrame(self.main_frame)
        lable_frame_2.grid(column=0,row=1,sticky='nsew',padx=25,rowspan=3,pady=(0,25),columnspan=4)

        # target frame
        sbf = ScrollbarFrame(lable_frame_2)
        sbf.pack(expand=True,fill='both',side='top')

        self.target_frame = sbf.scrolled_frame
        
    def lbf3(self):

        lable_frame_3 = ttk.CTkFrame(self.main_frame,fg_color='transparent')
        lable_frame_3.grid(column=4,row=0,rowspan=4,sticky='ns',padx=(0,25),pady=25)

        # styles

        new_btn = ttk.CTkButton(lable_frame_3,font=self.asset.font_small,height=40,hover_color=self.asset.green,fg_color='#191919',border_width=2,corner_radius=0,border_color=self.asset.green,text_color=self.asset.white,compound='left',text='New Project',width=20)
        new_btn.pack(side='top',expand=True,fill='x',padx=10)
        new_btn.configure(command=self.newfile)

        open_btn = ttk.CTkButton(lable_frame_3,font=self.asset.font_small,height=40,hover_color=self.asset.blue,fg_color='#191919',border_width=2,corner_radius=0,border_color=self.asset.blue,text_color=self.asset.white,compound='left',text='Open')
        open_btn.pack(side='top',expand=True,fill='x',padx=10)
        open_btn.configure(command=self.open_btn)
        
        workspace = ttk.CTkButton(lable_frame_3,font=self.asset.font_small,height=40,hover_color=self.asset.orange,fg_color='#191919',border_width=2,corner_radius=0,border_color=self.asset.orange,text_color=self.asset.white,compound='left',text='Workspace')
        workspace.pack(side='top',expand=True,fill='x',padx=10)

        workspace.configure(command=self.workspace_btn)
        
        reload_btn = ttk.CTkButton(lable_frame_3,font=self.asset.font_small,height=40,hover_color=self.asset.orange,fg_color='#191919',border_width=2,corner_radius=0,border_color=self.asset.orange,text_color=self.asset.white,compound='left',text='Reload')
        reload_btn.pack(side='top',expand=True,fill='x',padx=10)
        reload_btn.configure(command=self.reload_btn)

        rename_btn = ttk.CTkButton(lable_frame_3,font=self.asset.font_small,height=40,hover_color=self.asset.red,fg_color='#191919',border_width=2,corner_radius=0,border_color=self.asset.red,text_color=self.asset.white,compound='left',text='Rename')
        rename_btn.pack(side='top',expand=True,fill='x',padx=10)
        
        delete_btn = ttk.CTkButton(lable_frame_3,font=self.asset.font_small,height=40,hover_color=self.asset.red,fg_color='#191919',border_width=2,corner_radius=0,border_color=self.asset.red,text_color=self.asset.white,compound='left',text='Delete')
        delete_btn.pack(side='top',expand=True,fill='x',padx=10)
        
        fav_btn = ttk.CTkButton(lable_frame_3,font=self.asset.font_small,height=40,hover_color=self.asset.yellow,fg_color='#191919',border_width=2,corner_radius=0,border_color=self.asset.yellow,text_color=self.asset.white,compound='left',text='Favourite')
        fav_btn.pack(side='top',expand=True,fill='x',padx=10)
        
    def lbf4(self):
        lable_frame_4 = ttk.CTkFrame(self.main_frame,fg_color='transparent')
        lable_frame_4.grid(column=4,row=4,sticky='ns',padx=(0,25),pady=(0,25))


        self.toplevel_window = None
        # size, last edited, show in fe button
        # size_label = ttk.CTkLabel(lable_frame_4, text='Size: 69MB).pack(side='top',expand=True,fill='both',padx=10)
        # size_label = ttk.CTkLabel(lable_frame_4, text='Last Edited: 69/69/6969).pack(side='top',expand=True,fill='both',padx=10)
        reveal = ttk.CTkLabel(lable_frame_4,text='Reveal Workspace',font=self.asset.font_small, text_color="#4fa5e2")
        about = ttk.CTkLabel(lable_frame_4,text='About',font=self.asset.font_small, text_color="#4fa5e2")
        test = ttk.CTkLabel(lable_frame_4,text='Reveal Source Folder',font=self.asset.font_small, text_color="#4fa5e2")
        reveal.pack(side='top',expand=True,fill='both')
        test.pack(side='top',expand=True,fill='both')
        about.pack(side='top',expand=True,fill='both')
        # size_label = ttk.CTkLabel(lable_frame_4, text='Created Date: 69/69/6969').pack(side='top',expand=True,fill='both',padx=10)
        
        reveal.bind("<Button-1>", lambda e: subprocess.Popen(rf'explorer /select,"{self.WORKSPACE}"'))
        reveal.bind("<Enter>", lambda e: reveal.configure(font=self.asset.font_small_underline, cursor="hand2"))
        reveal.bind("<Leave>", lambda e: reveal.configure(font=self.asset.font_small, cursor="arrow"))
        
        about.bind("<Button-1>", lambda e: self.open_toplevel())
        about.bind("<Enter>", lambda e: about.configure(font=self.asset.font_small_underline, cursor="hand2"))
        about.bind("<Leave>", lambda e: about.configure(font=self.asset.font_small, cursor="arrow"))

    def lbf5(self):
        lable_frame_5 = ttk.CTkFrame(self.main_frame,fg_color='#1e1e1e')
        lable_frame_5.grid(column=0,row=4,padx=25,pady=(0,25),columnspan=4,sticky='nsew')

        lable_frame_5.grid_columnconfigure((0),weight=1,uniform='a')
        lable_frame_5.grid_rowconfigure((0,1),weight=1,uniform='a')

        # f1 = ttk.CTkFrame(lable_frame_5)
        # f1.grid(row=0,column=0,sticky='nsew')

        f2 = ttk.CTkFrame(lable_frame_5,fg_color='#1e1e1e')
        f2.grid(row=1,column=0,sticky='nsew')

        self.info_name = ttk.CTkLabel(lable_frame_5,text='NAME',font=self.asset.font_title,text_color='#ff4d4d')
        # lb1.pack(expand=True,fill='both')
        self.info_name.grid(row=0,column=0,sticky='s')


        self.info_cdate = ttk.CTkLabel(f2,text='C.Date: 00/00/2000',font=self.asset.font_small)
        self.info_cdate.pack(side='left',expand=True,fill='x',anchor='n',pady=(5,0))

        self.info_mdate = ttk.CTkLabel(f2,text='M.Date: 00/00/2000',font=self.asset.font_small)
        self.info_mdate.pack(side='left',expand=True,fill='x',anchor='n',pady=(5,0))

        self.info_size = ttk.CTkLabel(f2,text='Size: 69,69 MB',font=self.asset.font_small)
        self.info_size.pack(side='left',expand=True,fill='x',anchor='n',pady=(5,0))


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

    def edit_stuff_after_change_workspace(self, filelist: list[list], overwrite:bool = True, overwrite_current:bool = True, reload_workspace:bool = False) -> None:

        # 
        if reload_workspace:
            filelist = self.load_files_from_workspace(self.WORKSPACE)

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

    def on_hover(self, btn):
        btn.configure(border_width=1,border_color='#6f3131')

    def off_hover(self, btn):
        btn.configure(border_width=0)

    def select_btn(self, btn: ttk.CTkButton):
        text = btn.cget('text')
        
        for project in self.projects_data:
            if project[0] == text:

                print(project)

                t = datetime.fromtimestamp(project[1])
                cdate = f"{t.day}/{t.month}/{t.year}" 
                mdate = self.time_since(datetime.fromtimestamp(project[2]),datetime.now())

                self.info_name.configure(text=project[0])
                self.info_cdate.configure(text=f'C.Date: {cdate}')
                self.info_mdate.configure(text=f'M.Date: {mdate}')
                self.info_size.configure(text=f'Size: {project[3]} MB')

                break

        

    def create_item(self, master, name:str, created_date:str , modified_date:str , size, style):
        frame = ttk.CTkFrame(master=master,corner_radius=0,bg_color='blue')
        frame.grid(column=0,row=0,sticky='nsew',ipady=20)

        frame.rowconfigure(0, weight = 1)
        frame.columnconfigure((0,1,2,3,4), weight = 1, uniform = 'a')

        # widgets 
        this = ttk.CTkButton(frame,font=self.asset.font_bold,fg_color='#1e1e1e',text_color=self.asset.white,corner_radius=0,text = name)
        this.grid(row = 0, column = 0, columnspan = 4,sticky='nsew')

        this.bind('<Enter>', command=lambda e: self.on_hover(this))
        this.bind('<Leave>', command=lambda e: self.off_hover(this))
        this.bind('<Button-1>', command=lambda e: self.select_btn(this))

        # ttk.CTkButton(frame,fg_color=self.asset.lighter_black,text_color_disabled='#e2e6e9',state='disabled',corner_radius=0,text = '⠀').grid(row = 0, column = 3,sticky='nsew')
        size_label = ttk.CTkButton(frame,fg_color='#1e1e1e',text_color_disabled='#e2e6e9',state='disabled',corner_radius=0)
        size_label.grid(row = 0, column = 4,sticky='nsew')
        if size == '': 
            size_label.configure(text='')
        else:
            size_label.configure(text=f'{size}MB')

        return frame

    def reload_btn(self) -> None:
        self.value_inside.set('Filter')
        self.filter_options.configure(variable=self.value_inside)
        self.edit_stuff_after_change_workspace(self.projects_data, reload_workspace=True)
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
        if selection == 'Not Recently Modified':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[1])
        elif selection == 'Recently Modified':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[1],reverse=True)
        elif selection == 'Oldest':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[2])
        elif selection == 'Newest':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[2],reverse=True)
        elif selection == 'Name':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[0])
        elif selection == 'Name (Reversed)':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[0],reverse=True)
        elif selection == 'Biggest':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[3])
        elif selection == 'Smallest':
            sorted_list = sorted(self.current_projects_data, key=lambda x:x[3],reverse=True)
        elif selection == 'Favourited':
            ...

        self.edit_stuff_after_change_workspace(sorted_list, overwrite=False, overwrite_current=False)

    def time_since(self, dt1, dt2):
        """
        Calculates the difference between two datetime objects in a human-readable format.

        Args:
            dt1: The earlier datetime object.
            dt2: The later datetime object.

        Returns:
            A string representing the time difference between dt1 and dt2.
        """
        now = dt2
        diff = now - dt1

        seconds = abs(int(diff.total_seconds()))
        minutes = int(seconds / 60)
        hours = int(minutes / 60)
        days = int(hours / 24)
        months = int(days / 30)
        years = int(months / 12)

        if years > 0:
            return f"{years} {'year' if years == 1 else 'years'} ago"
        elif months > 0:
            return f"{months} {'month' if months == 1 else 'months'} ago"
        elif days > 0:
            return f"{days} {'day' if days == 1 else 'days'} ago"
        elif hours > 0:
            return f"{hours} {'hour' if hours == 1 else 'hours'} ago"
        elif minutes > 0:
            return f"{minutes} {'minute' if minutes == 1 else 'minutes'} ago"
        else:
            return f"{seconds} {'second' if seconds == 1 else 'seconds'} ago"
        
    def newfile(self):
        dialog = ttk.CTkInputDialog(text="Name your project:", title="Name your project")
        text = dialog.get_input()
        if text is None: return
        shutil.copyfile('./assets/example.sb3',f'{self.WORKSPACE}/{text}.sb3')
        self.openfile(filename=text)

    def openfile(self, filename: str):
        os.startfile(f'{self.WORKSPACE}/{filename}.sb3')

    def open_btn(self):
        if self.info_name.cget("text") is None: return
        self.openfile(filename=self.info_name.cget("text"))

app = App()
app.mainloop()