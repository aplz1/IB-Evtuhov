from tkinter import *
from tkinter import messagebox, scrolledtext, ttk
from tkinter.ttk import Checkbutton, Combobox
from tkinter.filedialog import askopenfilename

window = Tk()
window.title("Евтухов А.А.")
window.geometry('800x500')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text="                                     Первая                                     ") 
tab_control.add(tab2, text="                                     Вторая                                     ") 
tab_control.add(tab3, text="                                     Третья                                     ")



#первая вкладка "калькулятор"
def calculator():
    a = txt1.get()
    b = txt2.get()
    res = 0
    c = combo1.get()
    if c == '+':
        res = float(a) + float(b)
    if c == '-':
        res = float(a) - float(b)
    if c == '*':
        res = float(a) * float(b)
    if c == '/':
        res = float(a) / float(b)
    lbl2['text'] = res

txt1 = Entry(tab1 ,width=10)
txt1.grid(column = '1', row = '0')

txt2 = Entry(tab1, width= 10)
txt2.grid(column= '3', row = '0')

combo1 = Combobox(tab1)
combo1.grid(column = '2', row = '0')
combo1['values'] = ('+', '-', '*', '/')

btn1 = Button(tab1, text = '=', command=calculator)
btn1.grid(column = '4', row = '0')

lbl2 = Label(tab1, text = '')
lbl2.grid(column = '5', row = '0')




#вторая вкладка "выпадающий список"
def button():
    if c1.instate(['selected']) == True and c2.instate(['selected']) == True and c3.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали все варианты')
    elif c1.instate(['selected']) == True and c2.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали первый и второй варианты')
    elif c1.instate(['selected']) == True and c3.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали первый и третий варианты')
    elif c2.instate(['selected']) == True and c3.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали второй и третий варианты')
    elif c1.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали первый вариант')
    elif c2.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали второй вариант')
    elif c3.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали третий вариант')
    else:
        lbl.configure(text = "Вы ничего не выбрали")

lbl = Label(tab2)

cs1 = BooleanVar()
cs2 = BooleanVar()
cs3 = BooleanVar()

c1 = Checkbutton(tab2, text="Первый", var=cs1)
c2 = Checkbutton(tab2, text="Второй", var=cs2)
c3 = Checkbutton(tab2, text="Третий", var=cs3)
c1.grid(column=0, row=0)
c2.grid(column=0, row=1)
c3.grid(column=0, row=2)

btn = Button(tab2, text="Выбрать", command=button)   
btn.grid(column=0, row=3) 


#третья вкладка "открытие текстового файла"
def open_file():
    filepath = askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt.insert(END, text)

txt = scrolledtext.ScrolledText(tab3, height=25, width=80)
fr_buttons = Frame(tab3)

btn_open = Button(fr_buttons, text="Открыть", command=open_file)
btn_open.grid(row=0, column=0, sticky="ew")

fr_buttons.grid(row=0, column=0)
txt.grid(row=0, column=1)


tab_control.pack(expand=1, fill="both")
window.mainloop()