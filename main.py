from tkinter import *
from datetime import *
from time import *
from add_customer import *
from threading import Thread
from booking import *
from employee_info import *
from add_employee import *
from room_info import *


root = Tk()
root.title("Spa!")

# ++++++ All Function +++++++
def see_history():
    return

def add_promotion():
    return

def see_promotion():
    return

def customer_use():
    return
  

# ++++++ Date +++++++

today = datetime.today()
today_date = today.strftime("%d %B, %Y")
date_label = Label(root, text="วันที่: "+str(today_date), pady=20)
date_label.grid(row=0, column=0, columnspan=3, padx=5)


# ++++++ service +++++++

service_frame = LabelFrame(root, text="ลูกค้าใช้บริการ")
service_frame.grid(row=1, column=0, padx=10, pady=10)

c_name = Entry(service_frame, width=30)
c_name.grid(row=0, column=1, padx=20, pady=5)

c_name_label = Label(service_frame, text="ชื่อลูกค้า")
c_name_label.grid(row=0, column=0)

customer_use_btn = Button(service_frame, text="ใช้บริการ", command=lambda: customer_use(), padx=30, pady=5)
customer_use_btn.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

room_frame = LabelFrame(service_frame, text="ห้อง", padx=15, pady=145)
room_frame.grid(row=2, column=0, padx=10, pady=10)
employee_frame = LabelFrame(service_frame, text="พนักงาน", padx=20, pady=215)
employee_frame.grid(row=2, column=1, padx=10, pady=10)
promotion_frame = LabelFrame(service_frame, text="ทรีทเม้นท์")
promotion_frame.grid(row=2, column=2, padx=10, pady=10)

ROOMS = [
    ("VIP","VIP", 0),
    ("ทัวร์มาลิน","ทัวร์มาลิน", 1),
    ("โดม","โดม", 2),
    ("ห้อง2","ห้อง2", 3),
    ("ห้อง3","ห้อง3", 4),
    ("ห้อง4","ห้อง4", 5),
    ("ห้อง5","ห้อง5", 6),
    ("ห้อง7","ห้อง7", 7),
    ("ห้อง8","ห้อง8", 8),
    ("อบใน+ขัด","อบใน+ขัด", 9),
    ("อบนอก","อบนอก", 10),
]

EMPLOYEES = [
    ("ตา","ตา", 0, 0),
    ("ตาล","ตาล", 1, 0),
    ("จิ","จิ", 2, 0),
    ("สุ","สุ", 3, 0),
    ("เอ๋","เอ๋", 4, 0),
    ("ดาว","ดาว", 5, 0),
]

PROMOTIONS = [
    ("PT","PT", 0),
    ("Dome","Dome", 1),
    ("CM","CM", 2),
    ("M1","M1", 3),
    ("IBSW","IBSW", 4),
    ("CV","CV", 5),
    ("RF","RF", 6),
    ("AR","AR", 7),
    ("OM","OM", 8),
    ("หน้าA","หน้าA", 9),
    ("หน้าB(NGLM)","หน้าB(NGLM)", 10),
    ("นวดไทย","นวดไทย", 11),
    ("ตัวชุดA","ตัวชุดA", 12),
    ("ตัวชุดB","ตัวชุดB", 13),
    ("ตัวชุดC","ตัวชุดC", 14),
    ("ตัวชุดD(WM)","ตัวชุดD(WM)", 15),
    ("ตัวชุดE","ตัวชุดE", 16),
    ("BMอก","BMอก", 17),
    ("Wax(แขา,ขา)","Wax(แขา,ขา)", 18),
    ("Wax(รักแร้)","Wax(รักแร้)", 19),
    ("ปิดผมขาว","ปิดผมขาว", 20)
]

room = StringVar()
room.set("VIP")

employee = StringVar()
employee.set("ตา")

promotion = StringVar()
promotion.set("PT")

for text, mode, num in ROOMS:
    Radiobutton(room_frame, text=text, variable=room, value=mode).grid(row=num,padx=5, pady=2)

for text, mode, num, time in EMPLOYEES:
    Radiobutton(employee_frame, text=text, variable=employee, value=mode).grid(row=num,padx=5, pady=2)

for text, mode, num in PROMOTIONS:
    Checkbutton(promotion_frame, text=text).grid(row=num,padx=5, pady=2)

# ++++++ Check employees +++++++

active_employee_frame = LabelFrame(root, text="ข้อมูล",padx=60, pady=30)
active_employee_frame.grid(row=1, column=1, padx=10, pady=10)

employee_info_button = Button(active_employee_frame, text="ข้อมูลพนักงาน", command=employee_info)
employee_info_button.grid(row=0, column=0, padx=5, pady=5)
employee_info_button = Button(active_employee_frame, text="ข้อมูลห้อง", command=room_info)
employee_info_button.grid(row=0, column=1, padx=5, pady=5)
employee_info_button = Button(active_employee_frame, text="ข้อมูลทรีทเม้นท์", command=employee_info)
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