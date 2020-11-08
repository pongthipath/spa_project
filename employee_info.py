from tkinter import *
from datetime import *
from employee_data.employee_data_read import *
from employee_data.employee_data_edit import *
import add_employee

def employee_info():
    employee_info_window = Toplevel()
    employee_info_window.title("Spa - ข้อมูลพนักงาน!")

    def check_handPay(name_em):
        e_info_listbox.delete(0, END)
        old_name_em = name_em
        this_e_info = get_employee_some(old_name_em)
        for hp in this_e_info['hand_pay']:
            for key, value in hp.items():
                e_info_listbox.insert(END, str(key) + " : " + str(value))

    def reset_handPay(name_em):
        reset_this_handPay(name_em)
        status_label.config(text= "ค่ามือหมอของ " + name_em + " ถูกรีเซ็ตแล้ว!")


    status_label = Label(employee_info_window, text="")
    status_label.grid(row=0, column=0, columnspan=3, padx=20, pady=5)
    e_info_listbox = Listbox(employee_info_window)
    e_info_listbox.grid(row=1, column=1, padx=20, pady=5)
    all_name_e_listbox = Listbox(employee_info_window)
    all_name_e_listbox.grid(row=1, column=0, padx=20, pady=5)

    all_name_e = get_employee_all_name()
    for name in all_name_e:
        all_name_e_listbox.insert(END, name)

    check_handPay_e_button = Button(employee_info_window, text="ดูค่ามือหมอ", command=lambda:check_handPay(all_name_e_listbox.get(ANCHOR)))
    check_handPay_e_button.grid(row=2, column=0, padx=20, pady=5)
    reset_handPay_e_button = Button(employee_info_window, text="รีเซ็ตค่ามือหมอ", command=lambda:reset_handPay(all_name_e_listbox.get(ANCHOR)))
    reset_handPay_e_button.grid(row=2, column=1, padx=20, pady=5)

    add_e_button = Button(employee_info_window, text="ตั้งค่า", command=add_employee.employee_add)
    add_e_button.grid(row=3, column=0, columnspan=3, padx=20, pady=5)

