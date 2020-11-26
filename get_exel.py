from tkinter import filedialog
from customer_service.customer_service_read import *
import xlsxwriter

def get_exel_file(filename):
    filepath = filedialog.askdirectory()

    workbook = xlsxwriter.Workbook(filepath + '/' + filename + '.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'ลำดับ')
    worksheet.write('B1', 'เวลา')
    worksheet.write('C1', 'ไอดี')
    worksheet.write('D1', 'ชื่อ')
    worksheet.write('E1', 'นามสกุล')
    worksheet.write('F1', 'สมาชิค')
    worksheet.write('G1', 'เวลาที่ใช้บริการ')
    worksheet.write('H1', 'พนักงาน')
    worksheet.write('I1', 'ห้อง')
    worksheet.write('J1', 'ทรีทเม้นท์')

    count = 1
    for data in get_customer_service_info_all(filename):
        member = ''
        t_list = list()
        r_list = list()
        if(data['member'] == True):
            member = 'เป็น'
        if(data['member'] == False):
            member = 'ไม่เป็น'
        for e in data['employee']:
            employee = e
        r_list = data['room']
        for t in data['treatments']:
            show_t = str(t['treatment']) + ':' + str(t['amount'])
            t_list.append(show_t)
        worksheet.write('A' + str(count+1), data['seq'])
        worksheet.write('B' + str(count+1), data['time'])
        worksheet.write('C' + str(count+1), data['id'])
        worksheet.write('D' + str(count+1), data['fname'])
        worksheet.write('E' + str(count+1), data['sname'])
        worksheet.write('F' + str(count+1), member)
        worksheet.write('G' + str(count+1), data['service_time'])
        worksheet.write('H' + str(count+1), employee)
        worksheet.write('I' + str(count+1), str(r_list))
        worksheet.write('J' + str(count+1), str(t_list))
        count += 1

    workbook.close()