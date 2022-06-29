# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 07:20:27 2022

@author: durga
# """

# menu_list =["Mini statement","Balance enquiry","Pin Related"]
# menu_list.append("Language Change")
# menu_list.append("Checkbook info")

# print(menu_list)


# print("length of list:",len(menu_list))




# print("please select one from below\n\n")
# # print(f"1.{menu_list[0]}")
# # print(f"2.{menu_list[1]}")
# # print(f"3.{menu_list[2]}")
# # print(f"4.{menu_list[3]}")

# for i in range(0,4,1):
#     print(f"{i}.{menu_list[i]}")
    
    
    
menu_list =["Mini statement","Balance enquiry","Pin Related"]
menu_list.append("Language Change")
menu_list.append("Checkbook info")

print(menu_list)
print("please select one from below\n\n")
# print(f"1.{menu_list[0]}")
# print(f"2.{menu_list[1]}")
# print(f"3.{menu_list[2]}")
# print(f"4.{menu_list[3]}")

for i in range(0,len(menu_list),1):
    print(f"{i}.{menu_list[i]}")
    
    
    
    
    