from tkinter import  *


def get_simb():
    item = ent.get().strip()
    out_text.config(text=item)

window = Tk()
inp_text = Label(text= "Введите значение: ")
inp_text.pack(pady= 10)
ent = Entry()
ent.pack()

btn = Button(text='=', command=get_simb)
btn.pack(pady=10)
out_text = Label(text = '', bg='lightgrey')
out_text.pack()


window.mainloop()