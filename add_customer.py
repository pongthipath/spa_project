from tkinter import *
from treatments.treatment_data_read import *
from customer_data.customer_info_write import *

treatment_list = list()

def add_customer():
    add_customer_window = Toplevel()
    add_customer_window.title("Spa - เพิ่มลูกค้า!")

    def add_customer_to_db(fname, sname, id_c, treatment):
        status_to_db = add_new_customer(fname, sname, id_c, treatment_list)
        status_label.config(text=status_to_db)
        print(status_to_db)

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
        print(treatment_list)


    def remove_treatment_out(treatment_select):
        treatment_selected = treatment_select.split(":")
        this_treatment = {
            'treatment' : treatment_selected[0],
            'amount' : treatment_selected[1]
        }
        treatment_list.remove(this_treatment)
        t_info_listbox.delete(0, END)
        for name in treatment_list:
            t_info_listbox.insert(END, name)
        print(treatment_list)

    c_name_label = Label(add_customer_window, text="ชื่อ")
    c_name_label.grid(row=0, column=0, padx=5, pady=5)
    s_name_label = Label(add_customer_window, text="นาม-สกุล")
    s_name_label.grid(row=1, column=0, padx=5, pady=5)
    id_label = Label(add_customer_window, text="ไอดี")
    id_label.grid(row=2, column=0, padx=5, pady=5)

    c_name = Entry(add_customer_window, width=30)
    c_name.grid(row=0, column=1, padx=5, pady=5)
    s_name = Entry(add_customer_window, width=30)
    s_name.grid(row=1, column=1, padx=5, pady=5)
    id_entry = Entry(add_customer_window, width=30)
    id_entry.grid(row=2, column=1, padx=5, pady=5)

    add_treatment_frame = LabelFrame(add_customer_window, text="เลือกทรีทเม้นท์")
    add_treatment_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    status_t_1 = Label(add_treatment_frame, text="เลือก")
    status_t_1.grid(row=0, column=0)
    status_t_2 = Label(add_treatment_frame, text="ใช้")
    status_t_2.grid(row=0, column=2)

    all_name_t_listbox = Listbox(add_treatment_frame)
    all_name_t_listbox.grid(row=1, column=0, padx=20, pady=5)
    t_info_listbox = Listbox(add_treatment_frame)
    t_info_listbox.grid(row=1, column=2, padx=20, pady=5)

    all_name_t = get_treatment_all_name()
    for name in all_name_t:
        all_name_t_listbox.insert(END, name)

    select_t = Button(add_treatment_frame, text=">>", command=lambda: select_treatment_use(all_name_t_listbox.get(ANCHOR), amount_entry.get()))
    select_t.grid(row=1, column=1, padx=5, pady=5)
    amount_label = Label(add_treatment_frame, text="จำนวน: ")
    amount_label.grid(row=2, column=0, padx=5, pady=5)
    amount_entry = Entry(add_treatment_frame, width=5)
    amount_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
    remove_t = Button(add_treatment_frame, text="ลบ", command=lambda: remove_treatment_out(t_info_listbox.get(ANCHOR)))
    remove_t.grid(row=2, column=1, padx=5, pady=5)

    add_btn = Button(add_customer_window, text="เพิ่มลูกค้า", command=lambda: add_customer_to_db(c_name.get(), s_name.get(), id_entry.get(), all_name_t_listbox.get(ANCHOR)))
    add_btn.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    status_label = Label(add_customer_window, text="")
    status_label.grid(row=5, column=0, columnspan=3, padx=20, pady=5)
