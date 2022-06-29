#single line comments and multiline comments


'''
project name: ATM  project
project client : SBI,HDFC,ICICI,UNION
program version: V.1.0
Date of creation : 25-jan-2022
modified date:
    
project head: Anil

'''

import os
import sys

client_name     =  'ICICI'
card_number     =   int(input(" enter card number\n"))
customer_name   =   input("Enter your name\n")
existing_pin    =   1234

print(F"welcome to {client_name} bank")

print(card_number)
print(customer_name)

# =============================================================================
# Show different languages
# =============================================================================

try:
    
    language1 = "Telugu"
    language2 = "Hindi"
    language3 = "English"
    
    language = input("enter your language\n")
    
    if language == language1:
        print(f'your selected language is {language}')
    
    elif language == language2:
        print(f'your selected language is {language}')
        

except:
    print(f" please enter correct {language}")
    sys.exit()
    


# =============================================================================
# Enter your pin
# =============================================================================

try:
    for i in range(0,3,1):
        pin_num = int(input("Enter your pin number"))
        print(pin_num,type(pin_num))
    
        if existing_pin == pin_num:
            print(f"matching the pin{pin_num}")
    
    
except:
    print(f"not matching the pin{pin_num}")
    sys.exit()
    
# =============================================================================
# 
# =============================================================================

try:
     card_related_bank = "ICICI Card"
     print("Welcome to banking with  ICICI ")

except:
    print("card and Bank is not matching")
    sys.exit()
    
# =============================================================================
# Banking Select the service
# =============================================================================

try:

    # service1 = "1.Mini statements"
    # service2 = "2.balance enquiry"
    # service3 = "3.pin related"
    
    
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
        
    
   
    
    service = int(input("enter your choice"))
    
    if service == 1:
        print(f"your into {service1}")
    elif service == 2:
       print(f"your into {service2}")
    elif service == 3:
        print(f"your into {service3}")
        

except:
    print("wrong selection")
    sys.exit()
    
    
    
    















