from tkinter import *
import tkinter.messagebox as m_box
import translator as core

window = Tk()
window.title("C Translator")
window.geometry("700x620")
window.resizable(False, False)

frame_input = Frame(window)

label_instruct = Label(window, text="This program will provide lines of code in C language.\nWhen inserted in a "
                                    "program and executed will display output provided in the text field below")
label_instruct.pack(side=TOP, pady=10)

text_input = Text(frame_input, width=80, height=25)
scroll_input = Scrollbar(frame_input)
scroll_input.config(command=text_input.yview)
text_input.config(yscrollcommand=scroll_input.set)
scroll_input.pack(side=RIGHT, fill=Y)
text_input.pack(expand=NO)

frame_input.pack(pady=20)

frame_result = Frame(window)

label_result = Label(frame_result, text="Results will be stored in ")
label_result.pack(side=LEFT)


entry_name = Entry(frame_result)


def command_translate():
    name_result = entry_name.get()
    if name_result == "":
        m_box.showwarning("Unable to proceed", "Enter the name for the .txt file!")
    else:
        conf = m_box.askyesno("Confirmation", "The program will now create a file " + name_result
                              + ".txt\nIf the file exists it will be overwritten.\nDo you want to proceed?")
        if conf == 1:
            core.translate(text_input.get(index1="1.0", index2=END), name_result)


entry_name.pack(side=LEFT)

label_txt = Label(frame_result, text=".txt")
label_txt.pack(side=LEFT)

frame_result.pack(pady=20)

frame_btn = Frame(window)


def command_clear():
    text_input.delete(index1="1.0", index2=END)
    entry_name.delete(first=0, last=END)


button_clear = Button(frame_btn, text="Clear", command=command_clear, width=10, height=1)
button_clear.grid(row=0, column=0)

button_translate = Button(frame_btn, text="Translate", command=command_translate, width=10, height=1)
button_translate.grid(row=0, column=1, padx=40)

frame_btn.pack()
window.mainloop()
