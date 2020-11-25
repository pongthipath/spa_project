from tkinter import *
from datetime import *
from tkinter import messagebox
from rooms.rooms_data_write import *
from rooms.rooms_data_read import *
from rooms.rooms_data_delete import *

def room_add():
    room_add_window = Toplevel()
    room_add_window.title("Spa - เพิ่มห้อง!")

    def delete_room(name_e):
        msgBox = messagebox.askquestion('ยืนยันการลบข้อมูล', 'ต้องการลบห้อง ' + name_e + ' ใช่หรือไม่?')
        if(msgBox == 'yes'):
            delete_this_room(name_e)
            all_name_e_listbox.delete(0, END)
            all_name_e = get_room_all_name()
            for name in all_name_e:
                all_name_e_listbox.insert(END, name)
        else:
            messagebox.showinfo('ยกเลิก!', 'ยกเลิกการลบข้อมูล!')

    def add_room(name_e):
        add_new_room(name_e)
        messagebox.showinfo('เพิ่มห้อง!', 'เพิ่มห้อง ' + name_e + ' แล้ว!')
        all_name_e_listbox.delete(0, END)
        all_name_e = get_room_all_name()
        for name in all_name_e:
            all_name_e_listbox.insert(END, name)
        
    e_name_label = Label(room_add_window, text="ชื่อ: ")
    e_name_label.grid(row=0, column=0, padx=20, pady=5)
    e_name = Entry(room_add_window, width=30)
    e_name.grid(row=0, column=1, padx=20, pady=5)

    add_e_button = Button(room_add_window, text="เพิ่มห้อง", command=lambda: add_room(e_name.get()))
    add_e_button.grid(row=0, column=2, padx=20, pady=5)

    all_name_e_listbox = Listbox(room_add_window, exportselection=False)
    all_name_e_listbox.grid(row=1, column=0, columnspan=2, padx=20, pady=5)

    all_name_e = get_room_all_name()
    for name in all_name_e:
        all_name_e_listbox.insert(END, name)

    check_handPay_e_button = Button(room_add_window, text="ลบห้อง", command=lambda: delete_room(all_name_e_listbox.get(ANCHOR)))
    check_handPay_e_button.grid(row=2, column=0, columnspan=2, padx=20, pady=5)


