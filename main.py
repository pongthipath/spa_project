from tkinter import *
from tkinter import messagebox
from time import *
from add_customer import *
from threading import Thread
from booking import *
from employee_info import *
from add_employee import *
from room_info import *
from treatment_info import *
from add_treatment_customer import *
from customer_service.customer_service_write import *
from treatments.treatment_data_read import *
from customer_use import *
import datetime

root = Tk()
root.title("Spa!")

room_list = list()
employee_list = list()
treatment_list = list()

# ++++++ All Function +++++++

def see_history():
    return

def calculate_time_service(use_list):
    total = 0
    for u in use_list:
        for t in get_treatment_all():
            if(u['treatment'] == t['name']):
                total += int(u['amount']) * int(t['token'])
    return total

def add_service_history(fname, sname, id_c):
    add_history(fname, sname, id_c, employee_list, room_list, calculate_time_service(treatment_list), treatment_list)

def increase_handpay():
    new_list = list()
    old_list = list()
    name_e = ''
    for e in employee_list:
        name_e = e
    for e_db in get_employee_all():
        if(e_db['name'] == name_e):
            for hp in e_db['hand_pay']:
                old_list.append(hp)
                for tl in treatment_list:
                    if(hp['treatment'] == tl['treatment']):
                        temp = int(hp['amount']) + int(tl['amount'])
                        new_json = {
                            'treatment': hp['treatment'],
                            'amount': str(temp)
                        }
                        new_list.append(new_json)
                        treatment_list.remove(tl)
                        old_list.remove(hp)
    for cuso in old_list:
        new_list.append(cuso)
    for cusn in treatment_list:
        new_list.append(cusn)
    increase_this_handPay(name_e, new_list)
    old_list.clear()
    new_list.clear()

def customer_use(name):
    member = True
    for n in get_customer_info_all():
        if(name == n['fname']):
            msgBox = messagebox.askquestion('ยืนยันลูกค้า', 'คุณ ' + n['fname'] + ' ' + n['sname'] + ' , ไอดี : '+ n['id'] + ' กำลังจะใช้บริการใช่หรือไม่?')
            if(msgBox == 'yes'):
                c_data = get_customer_info_by_name(name)
                add_service_history(c_data['fname'], c_data['sname'], c_data['id'])
                increase_handpay()
                messagebox.showinfo('เรียบร้อย!', 'เพิ่มการใช้บริการแล้ว')
                member = False
            else:
                return
    if(member):
        msgBox = messagebox.askquestion('ยืนยันลูกค้า', 'คุณ ' + name + ' กำลังจะใช้บริการใช่หรือไม่?')
        if(msgBox == 'yes'):
            c_data = get_customer_info_by_name(name)
            add_service_history(name, '', '')
            increase_handpay()
            messagebox.showinfo('เรียบร้อย!', 'เพิ่มการใช้บริการแล้ว')
            member = False
        else:
            return
    amount_entry.delete(0, END)
    room_list.clear()
    employee_list.clear()
    treatment_list.clear()
    r_info_listbox.delete(0, END)
    e_info_listbox.delete(0, END)
    t_info_listbox.delete(0, END)

def select_room_use(room_selected):
    room_list.append(room_selected)
    r_info_listbox.delete(0, END)
    for name in room_list:
        r_info_listbox.insert(END, name)

def select_employee_use(employee_selected):
    employee_list.append(employee_selected)
    e_info_listbox.delete(0, END)
    for name in employee_list:
        e_info_listbox.insert(END, name)

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

def remove_room_out(room_selected):
    room_list.remove(room_selected)
    r_info_listbox.delete(0, END)
    for name in room_list:
        r_info_listbox.insert(END, name)

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
        show_name = name['treatment'] + ":" + name['amount']
        t_info_listbox.insert(END, show_name)


# ++++++ Date +++++++

today = datetime.datetime.today()
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

customer_use_btn = Button(service_frame, text="ใช้บริการ", command=lambda: customer_use(c_name.get()), padx=30, pady=5)
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

add_promotion_btn = Button(menu_frame, text="เพิ่มทรีทเม้นท์ลูกค้า", command=add_treatment_customer)
add_promotion_btn.grid(row=1, column=2, padx=5, pady=5)

booking_btn = Button(menu_frame, text="จองคิว", command=booking)
booking_btn.grid(row=1, column=4, padx=5, pady=5)


root.mainloop()