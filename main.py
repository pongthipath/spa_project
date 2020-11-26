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
from history import *
import datetime
import time

root = Tk()
root.title("Spa!")

room_list = list()
employee_list = list()
treatment_list = list()

# ++++++ All Function +++++++

def calculate_time_service(use_list):
    total = 0
    for u in use_list:
        for t in get_treatment_all():
            if(u['treatment'] == t['name']):
                total += int(u['amount']) * int(t['token'])
    return total

def add_service_history(fname, sname, id_c, member):
    add_history(fname, sname, id_c, member, employee_list, room_list, calculate_time_service(treatment_list), treatment_list)

def increase_handpay(employees, treatment_list_e):
    for employee in employees:
        in_hp_employee(employee, treatment_list_e)
    
def decrease_treatment(data, treatment_list_c):
    fname = ''
    sname = ''
    id_c = ''
    res = de_customer_t_by_id(data, treatment_list_c)
    for n in get_customer_info_all():
        if(data == n['id']):
            fname = n['fname']
            sname = n['sname']
            id_c = n['id']
    msgbox = messagebox.askquestion('ยืนยัน', 'คุณ ' + fname + ' ' + sname + ' , ไอดี : ' + id_c + '\nคงเหลือ: \n' + str(res[0]) + '\n ขาด:\n' + str(res[1]) + '\nทำรายการต่อใช่หรือไม่?')
    if(msgbox == 'yes'):
        de_customer_t_by_id_to_json(data, res[2])
        return True
    else:
        return False

def member_service(name):
    for n in get_customer_info_all():
        if(name == n['fname']):
            msgBox = messagebox.askquestion('ยืนยันลูกค้า', 'คุณ ' + n['fname'] + ' ' + n['sname'] + ' , ไอดี : '+ n['id'] + ' กำลังจะใช้บริการใช่หรือไม่?')
            if(msgBox == 'yes'):
                c_data = get_customer_info_by_name(n['fname'])
                status_msg = decrease_treatment(n['id'], treatment_list)
                if(status_msg):
                    add_service_history(c_data['fname'], c_data['sname'], c_data['id'], True)
                    increase_handpay(employee_list, treatment_list)
                    messagebox.showinfo('เรียบร้อย!', 'เพิ่มการใช้บริการแล้ว!')
                    amount_entry.delete(0, END)
                    room_list.clear()
                    employee_list.clear()
                    treatment_list.clear()
                    r_info_listbox.delete(0, END)
                    e_info_listbox.delete(0, END)
                    t_info_listbox.delete(0, END)
                else:
                    messagebox.showinfo('ยกเลิก!', 'ยกเลิกการใช้บริการแล้ว!')
            else:
                messagebox.showinfo('ยกเลิก!', 'ยกเลิกการใช้บริการแล้ว!')

def search_n(name):
    name_member_list = list()
    for n in get_customer_info_all():
        if not (n.get('fname') is name):
            name_member_list.append(False)
        if(name == n['fname']):
            name_member_list.append(True)
    if (True not in name_member_list):
        not_member(name, True)
    if(True in name_member_list):
        member_service(name)
    

def not_member(name, member):
    if(member):
        msgBox = messagebox.askquestion('ยืนยันลูกค้า', 'คุณ ' + str(name) + ' กำลังจะใช้บริการใช่หรือไม่?')
        if(msgBox == 'yes'):
            add_service_history(name, '', '', False)
            increase_handpay(employee_list, treatment_list)
            messagebox.showinfo('เรียบร้อย!', 'เพิ่มการใช้บริการแล้ว!')
            member = False
            amount_entry.delete(0, END)
            room_list.clear()
            employee_list.clear()
            treatment_list.clear()
            r_info_listbox.delete(0, END)
            e_info_listbox.delete(0, END)
            t_info_listbox.delete(0, END)
        else:
            messagebox.showinfo('ยกเลิก!', 'ยกเลิกการใช้บริการแล้ว!')

def search_id(id_c):
    for n in get_customer_info_all():
        if(id_c == n['id']):
            msgBox = messagebox.askquestion('ยืนยันลูกค้า', 'คุณ ' + n['fname'] + ' ' + n['sname'] + ' , ไอดี : '+ n['id'] + ' กำลังจะใช้บริการใช่หรือไม่?')
            if(msgBox == 'yes'):
                c_data = get_customer_info_by_id(n['id'])
                status_msg = decrease_treatment(n['id'], treatment_list)
                if(status_msg):
                    add_service_history(c_data['fname'], c_data['sname'], c_data['id'], True)
                    increase_handpay(employee_list, treatment_list)
                    messagebox.showinfo('เรียบร้อย!', 'เพิ่มการใช้บริการแล้ว!')
                    amount_entry.delete(0, END)
                    room_list.clear()
                    employee_list.clear()
                    treatment_list.clear()
                    r_info_listbox.delete(0, END)
                    e_info_listbox.delete(0, END)
                    t_info_listbox.delete(0, END)
            else:
                messagebox.showinfo('ยกเลิก!', 'ยกเลิกการใช้บริการแล้ว!')
    if(id_c not in get_customer_info_all_id()):
        messagebox.showinfo('ยกเลิก!', 'ไม่พบไอดีที่ค้นหา!')

def customer_use(data, request):
    if(request == 'ค้นหาโดย..'):
        messagebox.showwarning('ผิดพลาด!', 'กรุณาใส่การค้นหา!')
    if(request == 'ชื่อ'):
        search_n(data)
    if(request == 'ไอดี'):
        search_id(data)

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

c_name_service_entry = Entry(service_frame, width=30)
c_name_service_entry.grid(row=0, column=1, padx=20, pady=5)

search_c_drop = ttk.Combobox(service_frame, value=["ค้นหาโดย..", "ชื่อ", "ไอดี"])
search_c_drop.current(0)
search_c_drop.grid(row=0, column=0, padx=5, pady=5)

customer_use_btn = Button(service_frame, text="ใช้บริการ", padx=30, pady=5, command=lambda: customer_use(c_name_service_entry.get(), search_c_drop.get()))
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

r_scrollbar_1 = Scrollbar(room_frame, orient=VERTICAL)
r_scrollbar_2 = Scrollbar(room_frame, orient=VERTICAL)

all_name_r_listbox = Listbox(room_frame, yscrollcommand=r_scrollbar_1.set, exportselection=False)
r_scrollbar_1.config(command=all_name_r_listbox.yview)
r_scrollbar_1.grid(row=1, column=1, sticky='nwes')
all_name_r_listbox.grid(row=1, column=0, pady=5)
r_info_listbox = Listbox(room_frame, yscrollcommand=r_scrollbar_2.set)
r_scrollbar_2.config(command=all_name_r_listbox.yview)
r_scrollbar_2.grid(row=1, column=4, sticky='nwes')
r_info_listbox.grid(row=1, column=3, pady=5)

all_name_r = get_room_all_name()
for name in all_name_r:
    all_name_r_listbox.insert(END, name)

select_r = Button(room_frame, text=">>", command=lambda: select_room_use(all_name_r_listbox.get(ANCHOR)))
select_r.grid(row=1, column=2, padx=5, pady=5)
remove_r = Button(room_frame, text="ลบ", command=lambda: remove_room_out(r_info_listbox.get(ANCHOR)))
remove_r.grid(row=2, column=2, padx=5, pady=5)

# ++++++ employee service +++++++

status_e_1 = Label(employee_frame, text="เลือก")
status_e_1.grid(row=0, column=0)
status_e_2 = Label(employee_frame, text="ใช้")
status_e_2.grid(row=0, column=2)

e_scrollbar_1 = Scrollbar(employee_frame, orient=VERTICAL)
e_scrollbar_2 = Scrollbar(employee_frame, orient=VERTICAL)

all_name_e_listbox = Listbox(employee_frame, yscrollcommand=e_scrollbar_1.set, exportselection=False)
e_scrollbar_1.config(command=all_name_e_listbox.yview)
e_scrollbar_1.grid(row=1, column=1, sticky='nwes')
all_name_e_listbox.grid(row=1, column=0, pady=5)
e_info_listbox = Listbox(employee_frame, yscrollcommand=e_scrollbar_2.set)
e_scrollbar_2.config(command=e_info_listbox.yview)
e_scrollbar_2.grid(row=1, column=4, sticky='nwes')
e_info_listbox.grid(row=1, column=3, pady=5)

all_name_e = get_employee_all_name()
for name in all_name_e:
    all_name_e_listbox.insert(END, name)

select_e = Button(employee_frame, text=">>", command=lambda: select_employee_use(all_name_e_listbox.get(ANCHOR)))
select_e.grid(row=1, column=2, padx=5, pady=5)
remove_e = Button(employee_frame, text="ลบ", command=lambda: remove_employee_out(e_info_listbox.get(ANCHOR)))
remove_e.grid(row=2, column=2, padx=5, pady=5)

# ++++++ treatment service +++++++

status_t_1 = Label(treatment_frame, text="เลือก")
status_t_1.grid(row=0, column=0)
status_t_2 = Label(treatment_frame, text="ใช้")
status_t_2.grid(row=0, column=2)

t_scrollbar_1 = Scrollbar(treatment_frame, orient=VERTICAL)
t_scrollbar_2 = Scrollbar(treatment_frame, orient=VERTICAL)

all_name_t_listbox = Listbox(treatment_frame, yscrollcommand=t_scrollbar_1.set, exportselection=False)
t_scrollbar_1.config(command=all_name_t_listbox.yview)
t_scrollbar_1.grid(row=1, column=1, sticky='nwes')
all_name_t_listbox.grid(row=1, column=0, pady=5)
t_info_listbox = Listbox(treatment_frame, yscrollcommand=t_scrollbar_2.set)
t_scrollbar_2.config(command=t_info_listbox.yview)
t_scrollbar_2.grid(row=1, column=4, sticky='nwes')
t_info_listbox.grid(row=1, column=3, pady=5)

all_name_t = get_treatment_all_name()
for name in all_name_t:
    all_name_t_listbox.insert(END, name)

select_t = Button(treatment_frame, text=">>", command=lambda: select_treatment_use(all_name_t_listbox.get(ANCHOR), amount_entry.get()))
select_t.grid(row=1, column=2, padx=5, pady=5)
amount_label = Label(treatment_frame, text="จำนวน: ")
amount_label.grid(row=2, column=0, padx=5, pady=5)
amount_entry = Entry(treatment_frame, width=5)
amount_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
remove_t = Button(treatment_frame, text="ลบ", command=lambda: remove_treatment_out(t_info_listbox.get(ANCHOR)))
remove_t.grid(row=3, column=2, padx=5, pady=5)

# ++++++ Check employees +++++++

information_frame = LabelFrame(root, text="ข้อมูล",padx=60, pady=30)
information_frame.grid(row=2, column=1, padx=10, pady=10)

add_promotion_btn = Button(information_frame, text="ข้อมูลลูกค้า", command=add_treatment_customer)
add_promotion_btn.grid(row=0, column=0, padx=5, pady=5)
employee_info_button = Button(information_frame, text="ข้อมูลพนักงาน", command=employee_info)
employee_info_button.grid(row=0, column=1, padx=5, pady=5)
employee_info_button = Button(information_frame, text="ข้อมูลห้อง", command=room_info)
employee_info_button.grid(row=0, column=2, padx=5, pady=5)
employee_info_button = Button(information_frame, text="ข้อมูลทรีทเม้นท์", command=treatment_info)
employee_info_button.grid(row=0, column=3, padx=5, pady=5)


# ++++++ Menu +++++++

menu_frame = LabelFrame(root, text="เมนูเสริม",padx=60, pady=30)
menu_frame.grid(row=2, column=0, padx=10, pady=10)

add_customer_btn = Button(menu_frame, text="เพิ่มลูกค้า", command=add_customer)
add_customer_btn.grid(row=0, column=0, padx=5, pady=5)

see_history_btn = Button(menu_frame, text="ประวัติลูกค้า", command=history)
see_history_btn.grid(row=0, column=1, padx=5, pady=5)

booking_btn = Button(menu_frame, text="จองคิว", command=booking)
booking_btn.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()