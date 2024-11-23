from tkinter import *
w = 800
h = 600
player_size = 50
x1, y1 = 0, 0
player_color = 'red'
x_finish = 700
def key_handler(event):
    pass
window = Tk()
window.title('Догони меня если сможешь!')
canvas = Canvas(window, width = w, height = h, bg = 'while')
player_id =
finish_id =
window.bind('<KeyRelease>', key_handler)
window.mainloop()