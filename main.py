from tkinter import *
from datetime import *
from time import *
from add_customer import *
from threading import Thread
from booking import *


root = Tk()
root.title("Spa!")
root.geometry("800x1000")

# ++++++ All Function +++++++
def see_history():
    return

def add_promotion():
    return

def see_promotion():
    return

def customer_use(name, s_room, s_employee, s_promotion, time_m, time_s):
    time_thread = Thread(target=countdown, args=(time_m, time_s))
    time_thread.start()
    tnow = datetime.today()
    n_tnow = tnow.strftime("%A/%m/%Y")
    print(n_tnow + " คุณ: " + name + " , ใช้ห้อง: " + s_room + " , พนักงาน : " + s_employee + " , โปรโมชั่น: " + s_promotion)

def countdown(time_m, time_s): 
    t = int(int(time_m) * 60) + int(time_s)
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        for text, mode_v, num, time_v in EMPLOYEES:
            Label(active_employee_frame, text=timer).grid(row=num, column=1, padx=5, pady=2)
        sleep(1) 
        t -= 1
      
  

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
employee_time_m = Entry(service_frame, width=10)
employee_time_m.grid(row=1, column=1, padx=10, pady=10)
employee_time_s = Entry(service_frame, width=10)
employee_time_s.grid(row=1, column=2, padx=3, pady=10)
employee_time_m.insert(0, "นาที")
employee_time_s.insert(0, "วินาที")

c_name_label = Label(service_frame, text="ชื่อลูกค้า")
c_name_label.grid(row=0, column=0)
time_employee = Label(service_frame, text="ระยะเวลาพนักงาน")
time_employee.grid(row=1, column=0)


customer_use_btn = Button(service_frame, text="ใช้บริการ", command=lambda: customer_use(c_name.get(), room.get(), employee.get(), promotion.get(), employee_time_m.get(), employee_time_s.get()), padx=30, pady=5)
customer_use_btn.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

room_frame = LabelFrame(service_frame, text="ห้อง", padx=15, pady=145)
room_frame.grid(row=2, column=0, padx=10, pady=10)
employee_frame = LabelFrame(service_frame, text="พนักงาน", padx=20, pady=215)
employee_frame.grid(row=2, column=1, padx=10, pady=10)
promotion_frame = LabelFrame(service_frame, text="โปรโมชั่น")
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
    Radiobutton(promotion_frame, text=text, variable=promotion, value=mode).grid(row=num,padx=5, pady=2)
 
# ++++++ Check employees +++++++

active_employee_frame = LabelFrame(root, text="พนักงาน",padx=60, pady=30)
active_employee_frame.grid(row=1, column=1, padx=10)

active_employee_frame.after(500)
for text, mode, num, time in EMPLOYEES:
    Label(active_employee_frame, text=text).grid(row=num, column=0, padx=5, pady=2)
    Label(active_employee_frame, text=time).grid(row=num, column=1, padx=5, pady=2)



# ++++++ Menu +++++++

menu_frame = LabelFrame(root, text="เมนูเสริม",padx=60, pady=30)
menu_frame.grid(row=2, column=0, padx=10)

add_customer_btn = Button(menu_frame, text="เพิ่มลูกค้า", command=add_customer)
add_customer_btn.grid(row=1, column=0, padx=5, pady=5)

see_history_btn = Button(menu_frame, text="ประวัติลูกค้า", command=see_history)
see_history_btn.grid(row=1, column=1, padx=5, pady=5)

add_promotion_btn = Button(menu_frame, text="เพิ่มโปรโมชั่นลูกค้า", command=add_promotion)
add_promotion_btn.grid(row=1, column=2, padx=5, pady=5)

see_promotion_btn = Button(menu_frame, text="ดูโปรโมชั่นลูกค้า", command=see_promotion)
see_promotion_btn.grid(row=1, column=3, padx=5, pady=5)


booking_btn = Button(menu_frame, text="จองคิว", command=booking)
booking_btn.grid(row=1, column=4, padx=5, pady=5)



scrollbar = Scrollbar(root)
scrollbar.grid()

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.grid()
scrollbar.config( command = mylist.yview )

root.mainloop()