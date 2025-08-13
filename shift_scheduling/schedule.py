from collections import Counter
from classes import *
import random
import copy
import time
import json

# create departments
shoes = Department("shoes", 1)
cashier = Department("cashier", 5, 2)
home = Department("home", 2)
ladies = Department("ladies", 2)
processing = Department("processing", 4)
beauty = Department("beauty", 1)
jewellery = Department("jewellery", 1)

# create staff
kolade = Staff("kolade", "associate")
motun = Staff("motun", "associate")
core = Staff("core", "associate")
kunle = Staff("kunle", "associate")
dara = Staff("dara", "associate")
lanre = Staff("lanre", "associate")
tayo = Staff("tayo", "associate")
loli = Staff("loli", "associate")
shem = Staff("shem", "associate")
riri = Staff("riri", "associate")
segun = Staff("segun", "associate")
halafia = Staff("halafia", "associate")
ayo = Staff("ayo", "associate")
daoud = Staff("daoud", "associate")
hasan = Staff("hasan", "associate")
zara = Staff("zara", "associate")
bukayo = Staff("bukayo", "associate")
bola = Staff("bola", "associate")
niran = Staff("niran", "associate")
divine = Staff("divine", "associate")
# taiwo = Staff("taiwo", "associate")
# sam = Staff("sam", "associate")
# bosun = Staff("bosun", "associate")
# claudia = Staff("claudia", "associate")
# mimi = Staff("mimi", "associate")
# oba = Staff("oba", "associate")

departments = Department.list_departments()
staff_members = Staff.list_staff_members()

days_of_week = [
    "monday",
    "tuesday",
    "wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
shift_time = ["morning", "afternoon", "evening"]

domains = []
for day in days_of_week:
    for shift in shift_time:
        for department in departments:
            domain = day + "_" + shift + "_" + department.department_name
            domains.append(domain)

assigned_domains = {}

def is_domain_valid(domain, assignment):
    _, department = simplify_domain(domain)
    staff_assigned = assignment.get(domain, [])
    if len(staff_assigned) < department.max_num_staff:
        return True
    return False

def select_random_staff():
    staff = random.choice(staff_members)
    return staff

def simplify_domain(domain):
    """
    This function extracts the department from the domain, the department is usually the last thing in the string
    e.g monday_morning_shoes (day, time, department)
    """
    splits = domain.rsplit("_", 1)
    day_time = splits[0]
    department_name = splits[1]
    department = [
        department
        for department in departments
        if department.department_name == department_name
    ][0]
    return day_time, department


def consistent(assignment):
    """
    To check the consistency of a domain, we must ensure that
    1. Each department in the domain must meet its requirement for staff allocation
    2. Each staff cannot be in different departments same time
    3. There must be at least 2 team leads each day
    """

    for key, staff in assignment.items():
        day_time, department = simplify_domain(key)

        "if any staff has worked over their max hours, remove staff"

        "Each department must have its minimum num_of_staff and not exceed its max"
        if len(staff) > department.max_num_staff:
            return False

        "No duplicate staff in each shift"
        freq = Counter(staff)
        if any(freq[st] > 1 for st in staff):
            return False

        "Each staff must only be in one department per shift"
        for sec_key, sec_staff in assignment.items():
            if sec_key == key:
                continue

            if day_time in sec_key:
                for stf in staff:
                    if stf in assignment[sec_key]:
                        return False
                    stf_obj = get_staff_by_name(stf)
                    if not stf_obj.is_valid():
                        return False

    return True

# assignment will first be empty dictionary := {}
def backtrack(assignment):
    # if all items in domain exist in the assignment, that means each domain has been assigned a representative
    if len(assignment) == len(domains):
        vals = list({val for values in assignment.values() for val in values})
        if all(stf.name in vals for stf in staff_members):
            return assignment

    unfilled_domains = [d for d in domains if is_domain_valid(d, assignment)]
    # available_staff = [stf for stf in staff_members if stf.is_valid()]
    for domain in unfilled_domains:
        for stf in staff_members:
            # copy the assignment and keep original
            new_assignment = copy.deepcopy(assignment)

            # randomly select staff and assign to domain
            if not new_assignment.get(domain):
                new_assignment[domain] = [stf.name]
            else:
                new_assignment[domain].append(stf.name)

            # add hours to staff instance
            # stf.add_hours()

            if consistent(new_assignment):
                result = backtrack(new_assignment)
                if result is not None:
                    return result
            # stf.remove_hours()

    return None

def get_staff_by_name(name):
    return next(st for st in staff_members if st.name == name)

def sort_assignment(assignment):
    day_order = ["monday", "tuesday", "wednesday"]

    # Sort the keys based on the day_order
    sorted_items = sorted(
        assignment.items(), key=lambda item: day_order.index(item[0].split("_")[0])
    )

    # Rebuild the dictionary with the new order
    return dict(sorted_items)

def json_conv(assignment):
    readable_solution = {
        domain: [s.name for s in assigned_staff]
        for domain, assigned_staff in assignment.items()
    }
    return json.dumps(readable_solution, indent=4)

if __name__ == "__main__":
    solution = backtrack({})
    json_solution = json.dumps(solution, indent=4)
    print(json_solution)
    # print(json_conv(solution))

