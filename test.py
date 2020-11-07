class Employee:
    
    def __init__(self, name, company, retired = 'NO'): 
        self._name=name
        self.__company = company # __ denotes as a private attribute
        self.__retired = retired

    @property 
    def company(self):
        print("@property class method called")
        return self.__company 

    @company.setter
    def company(self,value):
        print("@company.setter class method called")
        self.__company = value

        
e=Employee('Pranay','Amazon')
print("Company name is :", e.company)
print("="* 35)
e.company='Google'
print("Company name is :", e.company)
print("="* 35)
Employee.company='Microsoft' # set the value by calling the propery method using class name
print("Company name is :", Employee.company)