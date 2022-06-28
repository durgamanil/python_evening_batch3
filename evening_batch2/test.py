# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 19:21:06 2022

@author: durga
"""

conn = pymysql.connect(host='localhost',user='root',password = "",db='school_management')
cursor1 = conn.cursor()

# sql = "INSERT INTO `student_table`(`sno`, `student_name`, `student_admission_number`, `student_gender`, `student_father`, `student_mother`, `student_dob`, `student_standard`, `student_contact`, `student_doa`, `student_section`, `student_address`) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# val = ('3',student_name_text, student_admission_number_text,student_gender_text,student_father_text,student_mother_text ,student_dob_text,student_standard_text,student_contact_text,student_doa_text,student_section_text,student_address_text)

# cursor1.execute(sql, val)

# conn.commit()