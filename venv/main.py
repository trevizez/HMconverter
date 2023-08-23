import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import os

import converter

root = tk.Tk()

path_output = ''
list_format = ['h2n', 'hm2', 'hm3']

def f_inp():
    global path_output
    fd = tk.filedialog.askopenfilenames(title="Выберите файл раздач", multiple=True)

    if fd:
        txt.config(state='normal')
        txt.delete(1.0, 'end')
        for i in fd:
            txt.insert('end', i+'\n')
            if path_output == '':
                path_output = os.path.dirname(i)
        txt.insert('end', '\n' + 'Конец списка' + '\n')
        txt.config(state='disable')
        bt_run.config(state='normal')

def f_out():
    global path_output
    path_output = tk.filedialog.askdirectory(title="Укажите место сохранения файлов")
    txt.config(state='normal')
    txt.insert('end', '\n' + 'Сохранить в: ' + '\n' + path_output + '\n')
    txt.config(state="disable")

lb_info = tk.Label(text = 'Выберите один или несколько файлов: ')
lb_info.place(y = 10, x = 10)

bt_input = tk.Button(root, text = '   ...   ', command = f_inp)
bt_input.place(y = 10, x = 235)

txt = tk.Text(width = 70, state = 'disable')
txt.place(y = 80, x = 10)

lb_output = tk.Label(text = 'Выберите каталог для сохранения файлов:')
lb_output.place(y = 10, x = 300)

bt_output = tk.Button(root, text = '   ...   ', command = f_out)
bt_output.place(y = 10, x = 545)


lb_format_info = tk.Label(text = 'В какой формат конвертировать файл(ы)?')
lb_format_info.place(y = 40, x = 10)

list_format_file = ttk.Combobox(root,
                                values = ['h2n', 'hm2', 'hm3'],
                                height=3, state = 'readonly')
list_format_file.current(0)
list_format_file.place(y = 40, x = 250)

bt_run = tk.Button(root, text = 'Выполнить', command = converter.converter, state = 'disable')
bt_run.place(y = 40, x = 510)


root.geometry('600x500')
root.title('h2n hm2 hm3 converter')
root.mainloop()
if __name__ == '__main__':
    pass