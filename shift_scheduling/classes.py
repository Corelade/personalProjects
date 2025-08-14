import random

# Define classes for Departments and Staff

# Some departments should only require staff during specific shifts like only evenings or afternoons and evenings or morning, afternoon and evenings

# Some staff members have availability days

class Department:
    '''
        Each department has a 
        - Name
        - Maximum number of staff at every given shift
    '''
    departments = []
    
    def __init__(self, department_name:str, max_num_staff:int, min_num_staff:int = 1):
        self.department_name = department_name.lower()
        self.__class__.departments.append(self)
        self.max_num_staff = max_num_staff
        self.min_num_staff = min_num_staff
        
    @classmethod
    def list_departments(cls):
        return [department for department in cls.departments]
        
    def __str__(self):
        return self.department_name    
    
class Staff:
    '''
        Each staff has a
        - Name
        - Contracted hours
        - Position (Associate, Management, Team Lead, Loss Protection)
        - Availability (To Be Implemented)
    '''
    
    # i'm to add staff availability, i.e some staff can only work on some certain days 
    
    staff_members = []
    
    def __init__(self, name:str, position:str):
        self.name = name.lower()
        self.position = position.lower()
        self.contract_hours = random.choice([i for i in range(8, 46, 4)])
        self.min_hours = 8

        Staff.staff_members.append(self)
    
    @classmethod
    def list_staff_members(cls):
        return [staff for staff in Staff.staff_members]
    
    def add_hours(self):
        self.hours_worked += 4
        return self.hours_worked
        
    def remove_hours(self):
        self.hours_worked -= 4
        return self.hours_worked
    
    def is_valid(self):
        return self.hours_worked <= self.max_hours
    
    def __str__(self):
        return self.name
    