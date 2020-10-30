from tkinter import *

def add_customer_to_db():
    return

def add_customer():
    add_customer_window = Toplevel()
    add_customer_window.title("Spa - เพิ่มลูกค้า!")
    add_customer_window.geometry("400x800")

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

    promotion = StringVar()
    promotion.set("PT")

    c_name_label = Label(add_customer_window, text="ชื่อ: ")
    c_name_label.grid(row=0, column=0, padx=5, pady=5)
    s_name_label = Label(add_customer_window, text="นาม-สกุล")
    s_name_label.grid(row=1, column=0, padx=5, pady=5)

    c_name = Entry(add_customer_window, width=30)
    c_name.grid(row=0, column=1, padx=5, pady=5)
    s_name = Entry(add_customer_window, width=30)
    s_name.grid(row=1, column=1, padx=5, pady=5)

    add_btn = Button(add_customer_window, text="เพิ่มลูกค้า", command=add_customer_to_db)
    add_btn.grid(row=3, column=1, padx=5, pady=5)

    promotion_frame = LabelFrame(add_customer_window, text="โปรโมชั่น")
    promotion_frame.grid(row=2, column=0, padx=10, pady=10)

    for text, mode, num in PROMOTIONS:
        Radiobutton(promotion_frame, text=text, variable=promotion, value=mode).grid(row=num,padx=5, pady=2)
 