from tkinter import *
from tkinter import ttk
from datetime import *
from tkinter import messagebox
from customer_service.customer_service_read import *
from customer_service.customer_service_delete import *
from customer_service.customer_service_edit import *
from employee_data.employee_data_edit import *
from customer_data.customer_info_edit import *
from tkinter.filedialog import asksaveasfile
from get_exel import *
import os, fnmatch, sys
import time

path = os.path.abspath('../spa_project') + '/data/history/'

width_en = 30

def history():
    history_window = Toplevel()
    history_window.title("Spa - ประวัติการใช้บริการ!")

    today = datetime.today()

    filename_list = list()

    def start_label():
        e1 = Entry(history_frame, width=width_en)
        e1.grid(row=0, column=0)
        e1.insert(END, 'ลำดับ')
        e1.config(state='disabled')
        e2 = Entry(history_frame, width=width_en)
        e2.grid(row=0, column=1)
        e2.insert(END, 'เวลา')
        e2.config(state='disabled')
        e3 = Entry(history_frame, width=width_en)
        e3.grid(row=0, column=2)
        e3.insert(END, 'ไอดี')
        e3.config(state='disabled')
        e4 = Entry(history_frame, width=width_en)
        e4.grid(row=0, column=3)
        e4.insert(END, 'ชื่อ')
        e4.config(state='disabled')
        e5 = Entry(history_frame, width=width_en)
        e5.grid(row=0, column=4)
        e5.insert(END, 'นามสกุล')
        e5.config(state='disabled')
        e6 = Entry(history_frame, width=width_en)
        e6.grid(row=0, column=5)
        e6.insert(END, 'สมาชิค')
        e6.config(state='disabled')
        e7 = Entry(history_frame, width=width_en)
        e7.grid(row=0, column=6)
        e7.insert(END, 'เวลาที่ใช้บริการ(นาที)')
        e7.config(state='disabled')
        e8 = Entry(history_frame, width=width_en)
        e8.grid(row=0, column=7)
        e8.insert(END, 'พนักงาน')
        e8.config(state='disabled')
        e9 = Entry(history_frame, width=width_en)
        e9.grid(row=0, column=8)
        e9.insert(END, 'ห้อง')
        e9.config(state='disabled')
        e10 = Entry(history_frame, width=width_en)
        e10.grid(row=0, column=9)
        e10.insert(END, 'ทรีทเม้นท์')
        e10.config(state='disabled')

    def delete_history(seq, filename):
        c_data = get_customer_service_info_by_seq(seq, filename)
        msgBox = messagebox.askquestion('ยืนยันการลบข้อมูล', 'ต้องการลบประวัติการใช้งานของคุณ ' + c_data['seq'] + ' ' + c_data['fname'] + ' ' + c_data['sname'] + ' , ไอดี : '+ c_data['id'] + ' ใช่หรือไม่?')
        if(msgBox == 'yes'):
            employee = ''
            for e in c_data['employee']:
                employee = e
            de_hp_employee(employee, c_data['treatments'])
            in_customer_t_by_id(c_data['id'], c_data['treatments'])
            delete_customer_service_info_by_seq(seq, filename)
            edit_seq_customer_service(filename)
            delete_r_button.configure(state='disabled')
            data_entry.delete(0, END)
            search_c_drop.current(0)
            search_history('ทั้งหมด', filename, '')
        else:
            messagebox.showinfo('ยกเลิก!', 'ยกเลิกการลบข้อมูล!')

    def search_history(request, filename, data):
        for widget in history_frame.winfo_children():
            widget.destroy()

        r_data_list = list()
        raw_c = list()
        if(request == 'ทั้งหมด'):
            raw_c = get_customer_service_info_all(filename)
        if(request == 'ชื่อ'):
            raw_c = get_customer_service_info_by_fname_list(data, filename)
        if(request == 'นามสกุล'):
            raw_c = get_customer_service_info_by_sname_list(data, filename)
        if(request == 'ไอดี'):
            raw_c = get_customer_service_info_by_id_list(data, filename)
        if(request == 'ลำดับ'):
            raw_data = get_customer_service_info_by_seq(data, filename)
            raw_c.append(raw_data)
            delete_r_button.configure(state='normal')
            

        start_label()

        for r in raw_c:
            member_s = ''
            if(r['member'] == True):
                member_s = 'เป็น'
            if(r['member'] == False):
                member_s = 'ไม่เป็น'
            c_data_list = []
            c_data_list.append(r['seq'])
            c_data_list.append(r['time'])
            c_data_list.append(r['id'])
            c_data_list.append(r['fname'])
            c_data_list.append(r['sname'])
            c_data_list.append(member_s)
            c_data_list.append(r['service_time'])
            c_data_list.append(r['employee'])
            c_data_list.append(r['room'])
            t_data_list = list()
            for t in r['treatments']:
                t_data = t['treatment'] + ':' + t['amount']
                t_data_list.append(t_data)
            c_data_list.append(t_data_list)
            r_data_list.append(c_data_list)

        total_rows = len(r_data_list)
        total_columns = len(r_data_list[0])

        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(history_frame, width=width_en)
                e.grid(row=i+1, column=j)
                e.insert(END, r_data_list[i][j])
                e.configure(state='disabled')

    def get_exel_file_f(filename):
        get_exel_file(filename)
        messagebox.showinfo('ดาวโหลด!', 'ดาวโหลดไฟล์Excelแล้ว!')

    listOfFiles = os.listdir(path)
    pattern = "*.json"
    for entry in reversed(listOfFiles):
        if fnmatch.fnmatch(entry, pattern):
                day = entry.split('.')
                filename_list.append(day[0])

    filename_label = Label(history_window, text="เลือกวันที่")
    filename_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
    filename_drop = ttk.Combobox(history_window, value=filename_list)
    filename_drop.current(0)
    filename_drop.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

    data_entry = Entry(history_window, width=30)
    data_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

    search_c_drop = ttk.Combobox(history_window, value=["ทั้งหมด", "ชื่อ", "นามสกุล", "ไอดี", "ลำดับ"])
<<<<<<< HEAD
    search_c_drop.current(0)

    search_c_drop.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    add_r_button = Button(history_window, text="ค้นหา", command=lambda: search_history(search_c_drop.get(), filename_drop.get(), data_entry.get()))
    add_r_button.grid(row=1, column=2, columnspan=3, padx=20, pady=5)

    build_xsl_button = Button(history_window, text="บันทึกเป็นExel", command=lambda: get_exel_file_f(filename_drop.get()))
    build_xsl_button.grid(row=2, column=1, columnspan=3, padx=20, pady=5)

    delete_r_button = Button(history_window, text="ลบประวัติ", command=lambda: delete_history(data_entry.get(), filename_drop.get()))
    delete_r_button.grid(row=2, column=2, columnspan=3, padx=20, pady=5)
    delete_r_button.configure(state='disabled')

    history_frame = LabelFrame(history_window, text="ประวัติการใช้บริการ", width=100, height=100)
    history_frame.grid(row=3, column=2, columnspan=3, padx=20, pady=5)

    start_label()
