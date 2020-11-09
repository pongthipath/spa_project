from tkinter import *
from datetime import *
from treatments.treatments_data_write import *
from treatments.treatment_data_read import *
from treatments.treatment_data_delete import *

def treatment_add():
    treatment_add_window = Toplevel()
    treatment_add_window.title("Spa - เพิ่มทรีทเม้นท์!")

    def delete_treatment(name_e):
        delete_this_treatment(name_e)
        status_label.config(text=str(name_e) + " ถูกลบแล้ว!")
        all_name_e_listbox.delete(0, END)
        all_name_e = get_treatment_all()
        for t in all_name_e:
            data = str(t['name']) + " | " + str(t['duration']) + " | " + str(t['token'])
            all_name_e_listbox.insert(END, data)

    def add_treatment(name_e, t_duration, t_hand_pay):
        add_new_treatment(name_e, t_duration, t_hand_pay)
        status_label.config(text=str(name_e) + " ถูกเพิ่มแล้ว!")
        all_name_e_listbox.delete(0, END)
        all_name_e = get_treatment_all()
        for t in all_name_e:
            data = str(t['name']) + " | " + str(t['duration']) + " | " + str(t['token'])
            all_name_e_listbox.insert(END, data)
        
    e_name_label = Label(treatment_add_window, text="ชื่อ: ")
    e_name_label.grid(row=0, column=0, padx=20, pady=5)
    e_name = Entry(treatment_add_window, width=30)
    e_name.grid(row=0, column=1, padx=20, pady=5)
    duration_label = Label(treatment_add_window, text="ระยะเวลา: ")
    duration_label.grid(row=1, column=0, padx=20, pady=5)
    duration_t = Entry(treatment_add_window, width=30)
    duration_t.grid(row=1, column=1, padx=20, pady=5)
    hand_pay_label = Label(treatment_add_window, text="ค่ามือหมอ: ")
    hand_pay_label.grid(row=2, column=0, padx=20, pady=5)
    hand_pay_t = Entry(treatment_add_window, width=30)
    hand_pay_t.grid(row=2, column=1, padx=20, pady=5)
    status_label = Label(treatment_add_window, text="")
    status_label.grid(row=4, column=2, columnspan=3, padx=20, pady=5)

    add_e_button = Button(treatment_add_window, text="เพิ่มทรีทเม้นท์", command=lambda: add_treatment(e_name.get(), duration_t.get(), hand_pay_t.get()))
    add_e_button.grid(row=1, column=2, padx=20, pady=5)

    name_label = Label(treatment_add_window, text="ชื่อ  |  ระยะเวลา  | ค่ามือหมอ")
    name_label.grid(row=3, column=0, columnspan=2, padx=20, pady=5)

    all_name_e_listbox = Listbox(treatment_add_window)
    all_name_e_listbox.grid(row=4, column=0, columnspan=2, padx=20, pady=5)

    all_name_e = get_treatment_all()
    for t in all_name_e:
        data = str(t['name']) + " | " + str(t['duration']) + " | " + str(t['token'])
        all_name_e_listbox.insert(END, data)

    check_handPay_e_button = Button(treatment_add_window, text="ลบทรีทเม้นท์", command=lambda:delete_treatment(all_name_e_listbox.get(ANCHOR)))
    check_handPay_e_button.grid(row=5, column=0, columnspan=2, padx=20, pady=5)


