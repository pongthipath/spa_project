from tkinter import *
from datetime import *
from time import *
from add_customer import *
from threading import Thread
from booking import *
from employee_info import *
from add_employee import *
from room_info import *
from treatment_info import *


root = Tk()
root.title("Spa!")

room_list = list()
employee_list = list()
treatment_list = list()

# ++++++ All Function +++++++
def see_history():
    return

def add_promotion():
    return

def see_promotion():
    return

def customer_use():
    room_list.clear()
    employee_list.clear()
    treatment_list.clear()
    r_info_listbox.delete(0, END)
    e_info_listbox.delete(0, END)
    t_info_listbox.delete(0, END)
    return

def select_room_use(room_selected):
    room_list.append(room_selected)
    r_info_listbox.delete(0, END)
    for name in room_list:
        r_info_listbox.insert(END, name)
    print(room_list)

def select_employee_use(employee_selected):
    employee_list.append(employee_selected)
    e_info_listbox.delete(0, END)
    for name in employee_list:
        e_info_listbox.insert(END, name)
    print(employee_list)

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

def remove_room_out(room_selected):
    room_list.remove(room_selected)
    r_info_listbox.delete(0, END)
    for name in room_list:
        r_info_listbox.insert(END, name)
    print(room_list)

def remove_employee_out(employee_selected):
    employee_list.remove(employee_selected)
    e_info_listbox.delete(0, END)
    for name in employee_list:
        e_info_listbox.insert(END, name)
    print(employee_list)

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


# ++++++ Date +++++++

today = datetime.today()
today_date = today.strftime("%d %B, %Y")
date_label = Label(root, text="วันที่: "+str(today_date), pady=20)
date_label.grid(row=0, column=0, columnspan=3, padx=5)


# ++++++ service +++++++

service_frame = LabelFrame(root, text="ลูกค้าใช้บริการ")
service_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

c_name = Entry(service_frame, width=30)
c_name.grid(row=0, column=1, padx=20, pady=5)

c_name_label = Label(service_frame, text="ชื่อลูกค้า")
c_name_label.grid(row=0, column=0)

customer_use_btn = Button(service_frame, text="ใช้บริการ", command=lambda: customer_use(), padx=30, pady=5)
customer_use_btn.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

room_frame = LabelFrame(service_frame, text="ห้อง",)
room_frame.grid(row=2, column=0, padx=10, pady=10)
employee_frame = LabelFrame(service_frame, text="พนักงาน")
employee_frame.grid(row=2, column=1, padx=10, pady=10)
treatment_frame = LabelFrame(service_frame, text="ทรีทเม้นท์")
treatment_frame.grid(row=2, column=2, padx=10, pady=10)

# ++++++ room service +++++++
status_r_1 = Label(room_frame, text="เลือก")
status_r_1.grid(row=0, column=0)
status_r_2 = Label(room_frame, text="ใช้")
status_r_2.grid(row=0, column=2)

all_name_r_listbox = Listbox(room_frame)
all_name_r_listbox.grid(row=1, column=0, padx=20, pady=5)
r_info_listbox = Listbox(room_frame)
r_info_listbox.grid(row=1, column=2, padx=20, pady=5)

all_name_r = get_room_all_name()
for name in all_name_r:
    all_name_r_listbox.insert(END, name)

select_r = Button(room_frame, text=">>", command=lambda: select_room_use(all_name_r_listbox.get(ANCHOR)))
select_r.grid(row=1, column=1, padx=5, pady=5)
remove_r = Button(room_frame, text="ลบ", command=lambda: remove_room_out(r_info_listbox.get(ANCHOR)))
remove_r.grid(row=2, column=1, padx=5, pady=5)

# ++++++ employee service +++++++
status_e_1 = Label(employee_frame, text="เลือก")
status_e_1.grid(row=0, column=0)
status_e_2 = Label(employee_frame, text="ใช้")
status_e_2.grid(row=0, column=2)

all_name_e_listbox = Listbox(employee_frame)
all_name_e_listbox.grid(row=1, column=0, padx=20, pady=5)
e_info_listbox = Listbox(employee_frame)
e_info_listbox.grid(row=1, column=2, padx=20, pady=5)

all_name_e = get_employee_all_name()
for name in all_name_e:
    all_name_e_listbox.insert(END, name)

select_e = Button(employee_frame, text=">>", command=lambda: select_employee_use(all_name_e_listbox.get(ANCHOR)))
select_e.grid(row=1, column=1, padx=5, pady=5)
remove_e = Button(employee_frame, text="ลบ", command=lambda: remove_employee_out(e_info_listbox.get(ANCHOR)))
remove_e.grid(row=2, column=1, padx=5, pady=5)

# ++++++ treatment service +++++++
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

# ++++++ Check employees +++++++

active_employee_frame = LabelFrame(root, text="ข้อมูล",padx=60, pady=30)
active_employee_frame.grid(row=2, column=1, padx=10, pady=10)

employee_info_button = Button(active_employee_frame, text="ข้อมูลพนักงาน", command=employee_info)
employee_info_button.grid(row=0, column=0, padx=5, pady=5)
employee_info_button = Button(active_employee_frame, text="ข้อมูลห้อง", command=room_info)
employee_info_button.grid(row=0, column=1, padx=5, pady=5)
employee_info_button = Button(active_employee_frame, text="ข้อมูลทรีทเม้นท์", command=treatment_info)
employee_info_button.grid(row=0, column=2, padx=5, pady=5)



# ++++++ Menu +++++++

menu_frame = LabelFrame(root, text="เมนูเสริม",padx=60, pady=30)
menu_frame.grid(row=2, column=0, padx=10, pady=10)

add_customer_btn = Button(menu_frame, text="เพิ่มลูกค้า", command=add_customer)
add_customer_btn.grid(row=1, column=0, padx=5, pady=5)

see_history_btn = Button(menu_frame, text="ประวัติลูกค้า", command=see_history)
see_history_btn.grid(row=1, column=1, padx=5, pady=5)

add_promotion_btn = Button(menu_frame, text="เพิ่มทรีทเม้นท์ลูกค้า", command=add_promotion)
add_promotion_btn.grid(row=1, column=2, padx=5, pady=5)

see_promotion_btn = Button(menu_frame, text="ดูทรีทเม้นท์ลูกค้า", command=see_promotion)
see_promotion_btn.grid(row=1, column=3, padx=5, pady=5)

booking_btn = Button(menu_frame, text="จองคิว", command=booking)
booking_btn.grid(row=1, column=4, padx=5, pady=5)


root.mainloop()