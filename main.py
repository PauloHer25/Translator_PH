from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
from PIL import Image
from PIL import ImageTk

root = Tk()

root.title("Translate Below")
root.geometry("1560x920")
def show():
    v1=combo_f.get()
    v2=combo_second.get()
    first_l.config(text=v1)
    second_l.config(text=v2)
    root.after(1000,show)
def clear():
    output_text.delete(1.0,END)
    input_text.delete(1.0,END)

def exit():
    root.destroy()

def translate():
    trans=Translator()
    transl=trans.translate(input_text.get(1.0,END),src=combo_f.get(),dest=combo_second.get())

    output_text.delete(1.0,END)
    output_text.insert(END,transl.text)

img = ImageTk.PhotoImage(Image.open("luke-chesser-tgrBcf7S_dY-unsplash.jpg"))  # PIL solution
lab=Label(root,image=img)
lab.pack()

first_l=Label(root,text='English',fg='black',bg='#e66a2e',font=('Arial', 20,'bold'))
first_l.place(x=40,y=150)

second_l=Label(root,text='Portuguese',fg='black',bg='#df543d',font=('Arial', 20,'bold'))
second_l.place(x=790,y=150)

language=list(LANGUAGES.values())

combo_f=ttk.Combobox(root,values=language)
combo_f.place(x=40,y=86)
combo_f.set('English')

combo_second=ttk.Combobox(root,values=language)
combo_second.place(x=790,y=86)
combo_second.set('Portuguese')

input_text=Text(root,height=20,width=80,wrap = WORD)
input_text.place(x=30,y=240)

output_text=Text(root,height=20,width=80,wrap = WORD)
output_text.place(x=730,y=240)

convert=Button(root,text='conver',height = 2,
               width = 14,bg="#0a78c7",fg="white",highlightthickness = 0, bd = 0,
               activebackground="#0a78c7",activeforeground="Black",command=translate)
convert.place(x=515,y=650)

clear=Button(root,text='clear',height = 2,
             width = 14,bg="#0d8259",fg="white",highlightthickness = 0, bd = 0,
             activebackground="#0d8259",activeforeground="Black",command=clear)
clear.place(x=640,y=650)

ext=Button(root,text='exit',height = 2,
           width =14,bg="#a82407",fg="white",highlightthickness = 0, bd = 0,
           activebackground="#a82407",activeforeground="Black",command=exit)
ext.place(x=765,y=650)
show()
root.mainloop()

