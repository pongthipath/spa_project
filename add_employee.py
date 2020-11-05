from tkinter import *
from datetime import *
import employee_data.employee_data_write as em

def employee_add():
    employee_add_window = Toplevel()
    employee_add_window.title("Spa - เพิ่มพนักงานพนักงาน!")
    employee_add_window.geometry("400x800")

    e_name_label = Label(employee_add_window, text="ชื่อ: ")
    e_name_label.grid(row=0, column=0, padx=20, pady=5)
    e_name = Entry(employee_add_window, width=30)
    e_name.grid(row=0, column=1, padx=20, pady=5)

    add_e_button = Button(employee_add_window, text="เพิ่มพนักงาน", command=lambda: em.add_new_employee(str(e_name.get())))
    add_e_button.grid(row=0, column=2, padx=20, pady=5)


