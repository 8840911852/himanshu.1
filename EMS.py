class Employee:
    def __init__(self,mob_no,name,):
        self.mob_no=mob_no
        self.name=name
        self.attandence=[]
        
    def mark_attandence(self,date):
        self.attandence.append(date)

    def show_detail(self):
        print("name:",self.name)
        print("employee id:",self.mob_no)
        print("attandence:",self.attandence)

empolyees = []

while True:
    print("----empolyee management syastem----")
    print("1: Add new emoloye.")
    print("2:show employee detaial.")
    print("3:mark your attandence.")
    
    choise =input(" Enter your choise:")


    if choise=='1':
        mobn=input("enter your mobile numer:")
        name=input("Enter your name:")
        emp=Employee(mobn,name)
        empolyees.append(emp)
        print("Empolpyee added.")
        print("Thank you.")
    elif choise=='2':
        print("--Empolyee infirmation--")
        emp.show_details()
    elif choise=='3':
        eid=input("enter your empplyee id:")
        date=input("Eneter your date of birth(DD/MM/YY):")
        print("attandence marked!")
        print("Thank You")
    else:
        print("invalid")
        
   
