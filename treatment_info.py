from tkinter import *
from datetime import *
from treatments.treatment_data_read import *
from add_treatment import *

def treatment_info():
    treatment_info_window = Toplevel()
    treatment_info_window.title("Spa - ข้อมูลทรีทเม้นท์!")

    name_label = Label(treatment_info_window, text="ชื่อ  |  ระยะเวลา  | ค่ามือหมอ")
    name_label.grid(row=0, column=0, padx=20, pady=5)

    all_name_e_listbox = Listbox(treatment_info_window, exportselection=False)
    all_name_e_listbox.grid(row=1, column=0, padx=40, pady=10)

    all_name_e = get_treatment_all()
    for t in all_name_e:
        data = str(t['name']) + " | " + str(t['duration']) + " | " + str(t['token'])
        all_name_e_listbox.insert(END, data)

    add_r_button = Button(treatment_info_window, text="ตั้งค่า", command=treatment_add)
    add_r_button.grid(row=3, column=0, columnspan=3, padx=20, pady=5)
