import tkinter as tk

#create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

#create widgets within the window
tk.Text(master = window).pack()


#run
window.mainloop()