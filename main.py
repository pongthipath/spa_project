from tkinter import *
from datetime import *

root = Tk()
root.title("Spa!")
root.geometry("800x600")

# ++++++ All Function +++++++

def customer_use():
    return

def add_customer():
    return

def see_history():
    return

def add_promotion():
    return

def see_promotion():
    return
# ++++++ All Function +++++++

# ++++++ Date +++++++

today = datetime.today()
today_date = today.strftime("%d %B, %Y")
date_label = Label(root, text="วันที่: "+str(today_date), pady=20)
date_label.grid(row=0, column=0, columnspan=3, padx=5)

# ++++++ Date +++++++

# ++++++ service +++++++

service_frame = LabelFrame(root, text="ลูกค้าใช้บริการ",padx=150, pady=60)
service_frame.grid(row=1, column=0, padx=10)

c_name = Entry(service_frame, width=30)
c_name.grid(row=0, column=1, padx=20)
use_promotion = Entry(service_frame, width=30)
use_promotion.grid(row=1, column=1, padx=20)

customer_use_btn = Button(service_frame, text="ลูกค้าใช้บริการ", command=customer_use, padx=30, pady=5)
customer_use_btn.grid(row=0, column=0, columnspan=4, padx=5)

# ++++++ service +++++++

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

# ++++++ Menu +++++++



root.mainloop()