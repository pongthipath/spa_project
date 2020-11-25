from tkinter import *
from datetime import *
from tkinter import messagebox
from employee_data.employee_data_write import *
from employee_data.employee_data_read import *
from employee_data.employee_data_delete import *
from treatments.treatment_data_read import *

def employee_add():
    employee_add_window = Toplevel()
    employee_add_window.title("Spa - เพิ่มพนักงาน!")

    def delete_employee(name_e):
        msgBox = messagebox.askquestion('ยืนยันการลบข้อมูล', 'ต้องการลบพนักงาน ' + name_e + ' ใช่หรือไม่?')
        if(msgBox == 'yes'):
            delete_this_employee(name_e)
            all_name_e_listbox.delete(0, END)
            all_name_e = get_employee_all_name()
            for name in all_name_e:
                all_name_e_listbox.insert(END, name)
        else:
            messagebox.showinfo('ยกเลิก!', 'ยกเลิกการลบข้อมูล!')

    def add_employee(name_e):
        this_t_list = list()
        for t in get_treatment_all_name():
            json_t ={
                'treatment': t,
                'amount': '0'
            }
            this_t_list.append(json_t)
        add_new_employee(name_e, this_t_list)
        messagebox.showinfo('เพิ่มพนักงาน!', 'เพิ่มพนักงาน ' + name_e + ' แล้ว!')
        all_name_e_listbox.delete(0, END)
        all_name_e = get_employee_all_name()
        for name in all_name_e:
            all_name_e_listbox.insert(END, name)
        
    e_name_label = Label(employee_add_window, text="ชื่อ: ")
    e_name_label.grid(row=0, column=0, padx=20, pady=5)
    e_name = Entry(employee_add_window, width=30)
    e_name.grid(row=0, column=1, padx=20, pady=5)

    add_e_button = Button(employee_add_window, text="เพิ่มพนักงาน", command=lambda: add_employee(e_name.get()))
    add_e_button.grid(row=0, column=2, padx=20, pady=5)

    all_name_e_listbox = Listbox(employee_add_window, exportselection=False)
    all_name_e_listbox.grid(row=1, column=0, columnspan=2, padx=20, pady=5)

    all_name_e = get_employee_all_name()
    for name in all_name_e:
        all_name_e_listbox.insert(END, name)

    check_handPay_e_button = Button(employee_add_window, text="ลบพนักงาน", command=lambda:delete_employee(all_name_e_listbox.get(ANCHOR)))
    check_handPay_e_button.grid(row=2, column=0, columnspan=2, padx=20, pady=5)


