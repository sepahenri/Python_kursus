from tkinter import *
from tkinter import ttk

root = Tk()
root.title('BOT')
root.iconbitmap('')
root.geometry('1366x768')

my_notebook = ttk.Notebook(root)
my_notebook.pack()

# Loon raamid, milledele hakkan hiljem sisusi lisama
my_frame1 = Frame(my_notebook)
my_frame2 = Frame(my_notebook)
my_frame3 = Frame(my_notebook)
my_frame4 = Frame(my_notebook)

# Lisan eelnevalt loodud raamid kuvatale programmile
my_frame1.pack(fill='both', expand=1)
my_frame2.pack(fill='both', expand=1)
my_frame3.pack(fill='both', expand=1)
my_frame4.pack(fill='both', expand=1)

# Seon raamid tabidega
my_notebook.add(my_frame1, text='Market Overview')
my_notebook.add(my_frame2, text='Trade Management')
my_notebook.add(my_frame3, text='Portfolio Overview')
my_notebook.add(my_frame4, text='Historical Data')

# Käivita Tkinter
root.mainloop()
