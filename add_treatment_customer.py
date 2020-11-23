from tkinter import *
from tkinter import ttk
from datetime import *
import time
from customer_data.customer_info_read import *
from treatments.treatment_data_read import *
from customer_data.customer_info_edit import *

treatment_list = list()

def add_treatment_customer():
    treatment_add_window = Toplevel()
    treatment_add_window.title("Spa - เพิ่มทรีทเม้นท์ลูกค้า!")

    def search_by(request, data):
        all_data_list = list()
        if(request == "ทั้งหมด"):
            all_data_list = get_customer_info_all()
            status_label.config(text="ค้นหาทั้งหมด!")
        if(request == "ชื่อ"):
            all_data_list = get_customer_info_by_fname_list(data)
            status_label.config(text="ค้าหาโดยชื่อสำเร็จ!")
        if(request == "นามสกุล"):
            all_data_list = get_customer_info_by_sname_list(data)
            status_label.config(text="ค้าหาโดยนามสกุลสำเร็จ!")
        if(request == "ไอดี"):
            all_data_list = get_customer_info_by_id_list(data)
            status_label.config(text="ค้าหาโดยไอดีสำเร็จ!")
        if(all_data_list == None or all_data_list == []):
            status_label.config(text="ไม่พบข้อมูล!")
        all_name_c_listbox.delete(0, END)
        for name in all_data_list:
            data_in = name['fname'] + " " + name['sname'] + " " + str(name['id'])
            all_name_c_listbox.insert(END, str(data_in))

    def find_treatment(data):
        data_list = data.split(" ")
        all_t_listbox.delete(0, END)
        all_name_c = get_customer_info_by_id(data_list[2])
        for name in all_name_c['treatments']:
            data_in = name['treatment'] + ":" + name["amount"]
            all_t_listbox.insert(END, data_in)

    def select_treatment_use(treatment_selected, amount):
        if(amount == ''):
            return
        for name in treatment_list:
            if(treatment_selected == name['treatment']):
                return
        this_treatment = {
            'treatment' : treatment_selected,
            'amount' : amount
        }
        treatment_list.append(this_treatment)
        t_info_listbox.delete(0, END)
        for name in treatment_list:
            show_name = name['treatment'] + ":" + name['amount']
            t_info_listbox.insert(END, show_name)

    def remove_treatment_out(treatment_select):
        treatment_selected = treatment_select.split(":")
        this_treatment = {
            'treatment' : treatment_selected[0],
            'amount' : treatment_selected[1]
        }
        treatment_list.remove(this_treatment)
        t_info_listbox.delete(0, END)
        for name in treatment_list:
            show_name = name['treatment'] + ":" + name['amount']
            t_info_listbox.insert(END, show_name)

    def add_treatment_to_c(data):
        if(data == None): 
            status_label.config(text="โปรดเลือกลูกค้า!")
        data_in = data.split(" ")
        new_list = list()
        old_list = list()
        get_c = get_customer_info_by_id(data_in[2])
        for i_db in get_c['treatments']:
            old_list.append(i_db)
            for c in treatment_list:
                if(c['treatment'] == i_db['treatment']):
                    temp = int(c['amount']) + int(i_db['amount'])
                    new_json = {
                        'treatment': i_db['treatment'],
                        'amount': str(temp)
                    }
                    new_list.append(new_json)
                    treatment_list.remove(c)
                    old_list.remove(i_db)
        for cuso in old_list:
            new_list.append(cuso)
        for cusn in treatment_list:
            new_list.append(cusn)
        edit_treatment_customer_info_by_id(data_in[2], new_list)
        treatment_list.clear()
        t_info_listbox.delete(0, END)
        status_label.config(text="เพิ่มทรีทเม้นท์ของ " + data + " เรียบร้อยแล้ว")

    search_customer_drop = ttk.Combobox(treatment_add_window, value=["ทั้งหมด", "ชื่อ", "นามสกุล", "ไอดี"])
    search_customer_drop.current(0)
    search_customer_drop.grid(row=0, column=0, padx=5, pady=5)

    search_customer_entry = Entry(treatment_add_window, width=30)
    search_customer_entry.grid(row=0, column=1, padx=5, pady=5)

    search_customer_button = Button(treatment_add_window, text="ค้นหา", command=lambda: search_by(search_customer_drop.get(), search_customer_entry.get()))
    search_customer_button.grid(row=0, column=2, padx=5, pady=5)

    all_name_c_listbox = Listbox(treatment_add_window, width=60, exportselection=False)
    all_name_c_listbox.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

    all_name_c = get_customer_info_all()
    for name in all_name_c:
        data_in = name['fname'] + " " + name['sname'] + " " + str(name['id'])
        all_name_c_listbox.insert(END, data_in)
    
    all_t_listbox = Listbox(treatment_add_window)
    all_t_listbox.grid(row=1, column=2, columnspan=3, padx=20, pady=10)

    find_treatment_button = Button(treatment_add_window, text="ดูทรีทเม้นท์", command=lambda: find_treatment(all_name_c_listbox.get(ANCHOR)))
    find_treatment_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    treatment_frame = LabelFrame(treatment_add_window, text="เพิ่มทรีทเม้นท์")
    treatment_frame.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    status_t_1 = Label(treatment_frame, text="เลือก")
    status_t_1.grid(row=0, column=0)
    status_t_2 = Label(treatment_frame, text="ใช้")
    status_t_2.grid(row=0, column=2)

    all_name_t_listbox = Listbox(treatment_frame)
    all_name_t_listbox.grid(row=1, column=0, padx=20, pady=5)
    t_info_listbox = Listbox(treatment_frame)
    t_info_listbox.grid(row=1, column=2, padx=20, pady=5)

    all_name_t = get_treatment_all_name()
    for name in all_name_t:
        all_name_t_listbox.insert(END, name)

    select_t = Button(treatment_frame, text=">>", command=lambda: select_treatment_use(all_name_t_listbox.get(ANCHOR), amount_entry.get()))
    select_t.grid(row=1, column=1, padx=5, pady=5)
    amount_label = Label(treatment_frame, text="จำนวน: ")
    amount_label.grid(row=2, column=0, padx=5, pady=5)
    amount_entry = Entry(treatment_frame, width=5)
    amount_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
    remove_t = Button(treatment_frame, text="ลบ", command=lambda: remove_treatment_out(t_info_listbox.get(ANCHOR)))
    remove_t.grid(row=3, column=1, padx=5, pady=5)

    add_treatment_button = Button(treatment_add_window, text="เพิ่มทรีทเม้นท์", command=lambda: add_treatment_to_c(all_name_c_listbox.get(ANCHOR)))
    add_treatment_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
    
    status_label = Label(treatment_add_window, text="")
    status_label.grid(row=5, column=0, columnspan=3, padx=20, pady=5)
