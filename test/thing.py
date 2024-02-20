import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename='superhero')

main_frame = ttk.Frame(root).grid(column=0,row=0)

# a = ttk.font.Font(family='Azeret Mono SemiBold',size=12)

# print(a)

a = ttk.Querybox.get_font(main_frame)

l = ttk.Label(master=main_frame, font=a, text='weiofh').grid(column=0,row=0)

root.mainloop()

#Azeret Mono SemiBold 12px
#Sans Serif Collection 8px