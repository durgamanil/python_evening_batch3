

# class Employee:
#     def __init__(self,name,rollno):
#         self.a = name
#         self.b = rollno

        
#     def display_name(self):
#         print("employee name",self.a)
         
#     def display_idno(self):
#         print("employee rollno",self.b)



# list1 = ["sandeep","kumar","srikanth","uday bhasker","anil","charan"]
# list1.append("laxmi")
# list1.append("saraswathi")

# for i in range(0,len(list1)):
#     emp1 = Employee(list1[i], i+1)
#     emp1.display_name()
#     emp1.display_idno()
    
#     print("="*30)
    
    

class Employee:
    def __init__(self,name,rollno,salary):
        self.a = name
        self.b = rollno
        self.total_sal= salary

        
    def show_details(self):
        print("employee name",self.a)
        print("employee rollno",self.b)
        print("employee salary",self.sal)
    
    def salary_split(self):
        pf_employee = 1800
        pf_employer = 1800
        car_allawance= 100000
        house_rent_al = 240000
        general_al = 500000
        total_sal = self.sal-pf_employee-pf_employer+car_allawance+house_rent_al+general_al
        #print(total_sal)
        
        
        

list1 = ["sandeep","kumar","srikanth","uday bhasker","anil","charan"]
list1.append("laxmi")
list1.append("saraswathi")
#print(len(list1))

sal1 =[100000,200000,300000,400000,500000,900000,10000000,10000000]

#print(len(sal1))

emp1 = Employee("raju",1,100000)
emp1.show_details()
#emp1.salary_split().total_sal
 




# for i in range(0,len(list1)):
#     emp1 = Employee(list1[i], i+1,sal1[i])
#     emp1.show_details()
    
    
#     print("="*30)


