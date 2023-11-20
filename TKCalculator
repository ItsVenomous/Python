from tkinter import *
from tkinter import messagebox

# Create the window
top = Tk()
top.geometry('300x150')


def do_calculation():
    global lbl_result_text

    if not txt_num1.get() or not txt_num2.get():
        messagebox.showerror('Error', 'Please input both numbers')
        return

    num1 = float(txt_num1.get())
    num2 = float(txt_num2.get())
    op = om_operation_text.get()

    if op == '+':
        lbl_result_text.set(str(num1 + num2))

    elif op == '-':
        lbl_result_text.set(str(num1 + num2))

    elif op == '*':
        lbl_result_text.set(str(num1 * num2))

    elif op == '/':
        lbl_result_text.set(str(num1 / num2))


# Add widgets to window
lbl_num1 = Label(top, text='Num 1')
lbl_num1.place(x=5, y=5)

lbl_num2 = Label(top, text='Num 2')
lbl_num2.place(x=5, y=30)

lbl_num2 = Label(top, text='Operation')
lbl_num2.place(x=5, y=55)

txt_num1 = Entry(top)
txt_num1.place(x=90, y=5)

txt_num2 = Entry(top)
txt_num2.place(x=90, y=30)

om_operation_text = StringVar()
om_operation_text.set('+')
om_operation = OptionMenu(top, om_operation_text, '+', '-', '*', '/')
om_operation.place(x=90, y=60)

btn_calculate = Button(top, text='Calculate', command=do_calculation)
btn_calculate.place(x=90, y=90)

lbl_result_text = StringVar()
lbl_result_text.set('0')
lbl_result = Label(top, textvariable=lbl_result_text, font='Helvetica 18 bold')
lbl_result.place(x=90, y=120)
# Start the loop to show the window
top.mainloop()
