company_info = (
    "PythonGuruKool",
    "Pune",
    2018,
    "ISO 27001 Certified"
)

tools = [
    "GitHub",
    "AWS",
    "Slack",
    "Jira",
    "Production Server",
    "HR Portal",
    "Figma",
    "Docker"
]

roles = (
    "intern",
    "developer",
    "tester",
    "manager",
    "admin"
)

role_permissions = {
    "intern": ["Slack", "Jira"],
    "developer": ["GitHub", "Slack", "Jira", "AWS"],
    "tester": ["Slack", "Jira", "GitHub", "Docker"],
    "manager": ["GitHub", "Slack", "Jira", "AWS", "HR Portal"],
    "admin": ["GitHub", "Slack", "Jira", "AWS",
              "HR Portal", "Production Server", "Figma", "Docker"]
}

employees = {
    "E101": {
        "name": "Aarav Sharma",
        "role": "developer",
        "access": ["GitHub", "Slack", "Jira", "AWS"]
    },
    "E102": {
        "name": "Sneha Patil",
        "role": "intern",
        "access": ["Slack", "Jira"]
    }
}

access_log = [
    ("E101", "GitHub", "GRANTED", "2025-01-15"),
    ("E102", "AWS", "DENIED", "2025-02-10")
]

print("=" * 70)
print("ACCESS GUARD".center(70))
print("SECURE ACCESS CONTROL SYSTEM".center(70))
print("=" * 70)

print(f"{company_info[0]} | HQ: {company_info[1]} | Est: {company_info[2]}".center(70))
print(f"Security Standard: {company_info[3]}".center(70))

print("-" * 70)

print("SYSTEM OVERVIEW".center(70))
print(f"Total Tools Available : {len(tools)}")
print(f"Valid Roles           : {len(role_permissions)}")
print(f"Employees Registered  : {len(employees)}")
print(f"Access Log Entries    : {len(access_log)}")

print("-" * 70)

print("SYSTEM STATUS : ONLINE".center(70))
print("SECURITY      : ACTIVE".center(70))

print("-" * 70)

print("WELCOME TO ACCESS GUARD".center(70))

print("=" * 70)

print("=" * 70)
print("AVAILABLE TOOLS".center(70))
print("=" * 70)

print(f"01. {tools[0]}")
print(f"02. {tools[1]}")
print(f"03. {tools[2]}")
print(f"04. {tools[3]}")
print(f"05. {tools[4]}")
print(f"06. {tools[5]}")
print(f"07. {tools[6]}")
print(f"08. {tools[7]}")


print("\n" + "=" * 70)
print("VALID ROLES".center(70))
print("=" * 70)

print(f"01. {roles[0]}")
print(f"02. {roles[1]}")
print(f"03. {roles[2]}")
print(f"04. {roles[3]}")
print(f"05. {roles[4]}")


print("\n" + "=" * 70)
print("ROLE PERMISSIONS".center(70))
print("=" * 70)

print(f"Intern     --> {role_permissions['intern']}")
print(f"Developer  --> {role_permissions['developer']}")
print(f"Tester     --> {role_permissions['tester']}")
print(f"Manager    --> {role_permissions['manager']}")
print(f"Admin      --> {role_permissions['admin']}")


print("\n" + "=" * 70)
print("EXISTING EMPLOYEES".center(70))
print("=" * 70)

print(f"E101 | {employees['E101']['name']} | {employees['E101']['role']} | "
      f"Access: {employees['E101']['access']}")

print(f"E102 | {employees['E102']['name']} | {employees['E102']['role']} | "
      f"Access: {employees['E102']['access']}")


print("\n" + "=" * 70)
print("ACCESS LOG".center(70))
print("=" * 70)

print(f"{access_log[0]}")
print(f"{access_log[1]}")

print("=" * 70)

print("\n--- NEW EMPLOYEE ONBOARDING--- \n".center(70))
full_name = input("Enter full name: ").strip().title()
name_parts = full_name.split()

first_name = name_parts[0]
last_name = name_parts[-1]
if not first_name.isalpha() or not last_name.isalpha():
    print("Invalid name. Name must contain only letters.")
else:
    print(f"Name accepted: {full_name}")

emp_id = input("Enter Employee ID (e.g.E103):  ").strip().upper()

if not emp_id.startswith("E"):
    print("Employee ID must start with 'E' ")
elif not emp_id[1:].isdigit():
    print("After 'E',only numbers are allowed")
elif len(emp_id)!= 4:
    print("Employee ID must be exactly 4 characters e.g.E103")
else:
    print(f"Employee ID accepted : {emp_id}")

print(f"\n Available roles : {roles}")
role=input("Enter role : ").strip().lower()

if role not in roles:
    print(f"Invalid role. choose from {roles}")
else:
    print(f"Role Accepted : {role.title()}")

email= first_name.lower() + "." + last_name.lower() + "@pythongurukool.com"
print(f"Auto-Generated email : {email}")

temp_password= first_name[:3].lower()+emp_id[:-3]+"@TN"
print(f"Temporary password: {temp_password}")

experience=int(input("Enter years of experience : "))
if experience<0:
    print("Experience cannot be negative")
elif experience==0 :
    print("Fresher detected.Mentor will be assigned soon")
elif experience<=3 :
    print("Junior level")
elif experience<=7 :
    print("Mid level")
else:
    print("Senior level")

access=role_permissions[role].copy()

employees[emp_id] = {
    "name": full_name,
    "role": role,
    "access": access,
    "email": email
}

onboard_record = (emp_id, full_name, role, "2026-10-01")

print("=" * 60)
print("ONBOARDING COMPLETE".center(60))
print(f"Name       : {full_name}")
print(f"ID         : {emp_id}")
print(f"Role       : {role.title()}")
print(f"Email      : {email}")
print(f"Password   : {temp_password}")
print(f"Access     : {', '.join(access)}")
print(f"Note       : Role-based access granted.")
print("=" * 60)
print(f"Permanent Record: {onboard_record}")
print(f"Record Type: {type(onboard_record)}")
print("=" * 60)

print("\n" + "=" * 60)
print("ACCESS REQUEST PORTAL".center(60))
print("=" * 60)

print(f"Registered Employee IDs: {employees.keys()}")

employee_id = input("Enter employee ID: ").strip().upper()
emp = employees.get(employee_id)
if emp is None:
    print("Employee not found.")
else:
    print(f"\nWelcome, {emp['name']}!")
    print(f"Current Role : {emp['role'].title()}")
    print("You currently have access to:")
    print(", ".join(emp["access"]))

    print(f"\nAll available tools : {tools}")

    tool = input("Enter tool name: ").strip()
if tool in tools:
    print(f"Tool '{tool}' is available.")

    if tool in emp["access"]:
        print(f"You already have access to {tool}.")

    else:
        if tool in role_permissions[emp["role"]]:
         emp["access"].append(tool)
         print(f"Access granted to {tool}.")

         log_record = (employee_id, tool, "GRANTED", "2026-10-02")
         access_log.append(log_record)
         print(f"Updated access : emp['access']")
        else:
         print(f"Access to {tool} is not permitted for your role.")

         log_record = (employee_id, tool, "DENIED", "2026-10-02")
         access_log.append(log_record)
else:
    print(f"Tool '{tool}' does not exist.")

print(f"\nUpdated Access Log : \n{access_log}")

aarav_access = set(employees["E101"]["access"])
sneha_access = set(employees["E102"]["access"])
all_tools = set(tools)

common = aarav_access & sneha_access
print(f"Tools both have: {common}")
aarav_extra = aarav_access - sneha_access
print(f"Only Aarav has: {aarav_extra}")
sneha_extra = sneha_access - aarav_access
print(f"Only Sneha has: {sneha_extra}")
combined_access = aarav_access | sneha_access
print(f"Combined access: {combined_access}")
exclusive_tools = aarav_access ^ sneha_access
print(f"Exclusive tools: {exclusive_tools}")
unused_tools = all_tools - combined_access
print(f"Unused tools: {unused_tools}")
print(f"Company paying for {len(unused_tools)} unused tools.")
print("Is Sneha's access a subset of Aarav's?",
      sneha_access.issubset(aarav_access))

print("Is Aarav's access a superset of Sneha's?",
      aarav_access.issuperset(sneha_access))

print("Are Aarav and Sneha's accesses disjoint?",
      aarav_access.isdisjoint(sneha_access))
aarav_access.add("Docker")
print(f"After adding Docker : {aarav_access}")
aarav_access.discard("Docker")
print(f"After discarding Docker : {aarav_access}")
aarav_access.remove("AWS")
print(f"After removing AWS : {aarav_access}")
removed_tool = aarav_access.pop()
print(f"Removed tool : {removed_tool}")
print(f"After pop : {aarav_access}")
aarav_access.clear()
print(f"After clearing : {aarav_access}")
tool_list = ["GitHub", "Slack", "GitHub", "Jira", "Slack"]
unique_tools = set(tool_list)
print("Original list:", tool_list)
print("After deduplication:", unique_tools)
emp_id = input("Enter Employee ID: ").strip().upper()
emp = employees.get(emp_id)
if emp is None:
    print("Employee not found.")
else:
    print(f"Employee found: {emp['name']}")
    print(f"Current access: {emp['access']}")
    tool = input("Tool to revoke: ").strip()
    emp_id = input("Enter Employee ID: ").strip().upper()
    if tool not in emp["access"]:
      print(f"{emp['name']} doesn't have {tool}.")
    else:
         pos = emp["access"].index(tool)
         print(f"Found '{tool}' at position {pos}")
         emp["access"].remove(tool)
         print(f"Access to {tool} revoked.")
         print(f"Updated access: {emp['access']}")
         log_record = (emp_id, tool, "REVOKED", "2026-10-03")
         access_log.append(log_record)
         print(f"Revocation logged: {log_record}")

print(f"Total log entries: {len(access_log)}")

print(f"First log entry : {access_log[0]}")
print(f"Last log entry : {access_log[-1]}")
print(f"First 2 log entries : {access_log[:2]}")
print(f"Last 3 entries : {access_log[-3:]}")
sorted_log = sorted(access_log)
print("Sorted log:", sorted_log)
print("Original log:", access_log)
reversed_log = access_log.copy()
reversed_log.reverse()
print("Reversed log:", reversed_log)
print("Original log:", access_log)
popped_entry = reversed_log.pop()
print("Popped entry:", popped_entry)
reversed_log.insert(0, ("SYSTEM", "AUDIT", "MARKER", "2026-10-03"))
print("Updated reversed log:", reversed_log)
print(f"\nFinal Access Log : {access_log} ")
print(f"\nFinal Reversed Log: {reversed_log}")
emp_id = input("Employee ID to update: ").strip().upper()
emp = employees.get(emp_id)

if emp is None:
    print("Employee not found.")
else:
    print("Employee found.")
    print(f"Fields: {list(emp.items())}")
    print(f"Available fields: {emp.keys()}")
    # --- ROLE UPDATE ---

    new_role = input("Enter new role (or Enter to skip): ").strip().lower()

    if new_role != "":
       if new_role not in roles:
          print(f"Invalid. Choose from {roles}")
       else:
           emp.update({
            "role": new_role,
            "access": role_permissions[new_role].copy()
            })

           print(f"Role updated to {new_role.title()}")

    emp.setdefault("phone", "Not provided")

    phone = input("Enter phone (or Enter to skip): ").strip()

    if phone != "":
       if len(phone) != 10 or not phone.isdigit():
          print("Phone must be exactly 10 digits.")
       else:
            emp["phone"] = phone


    remove_field = input("Remove a field? or Enter to skip ").strip()

    if remove_field != "":
      removed = emp.pop(remove_field, "Field not found")
      print(f"Removed '{remove_field}': {removed}")

    print(f"Keys   : {emp.keys()}")
    print(f"Values : {emp.values()}")      

aarav_access = employees["E101"]["access"]
riya_access = aarav_access.copy()
print(f"Riya's access : {riya_access}")
print(f"Aarav's access: {aarav_access}")
print("Aarav's list is unaffected!")
print(f"Same object? {riya_access is aarav_access}")
original = ["GitHub", "Slack", "Jira"]

copy_1 = original.copy() 
copy_2 = list(original)    
copy_3 = original[:]      
print(f"copy_1 is original? {copy_1 is original}")
print(f"copy_2 is original? {copy_2 is original}")
print(f"copy_3 is original? {copy_3 is original}")

aarav_backup = employees["E101"].copy()
aarav_backup["access"] = employees["E101"]["access"].copy()
aarav_backup["access"].append("Figma")
print(f"Backup access  : {aarav_backup['access']}")
print(f"Original access: {employees['E101']['access']}")
print("Original is unaffected! Both independent.")

# --- FINAL DASHBOARD ---

title = "ACCESS GUARD - FINAL REPORT"
print(title.center(60, "="))
# --- EMPLOYEE TABLE ---

print(f"\n{'ID':<8}{'Name':<20}{'Role':<12}{'Tools':<6}")
print("-" * 70)


emp = employees["E101"]

print(
    f"{'E101':<8}"
    f"{emp['name']:<20}"
    f"{emp['role'].upper():<12}"
    f"{len(emp['access']):<6}"
    f"{' | '.join(emp['access'])}"
)


emp = employees["E102"]

print(
    f"{'E102':<8}"
    f"{emp['name']:<20}"
    f"{emp['role'].upper():<12}"
    f"{len(emp['access']):<6}"
    f"{' | '.join(emp['access'])}"
)

emp = employees["E103"]

print(
    f"{'E103':<8}"
    f"{emp['name']:<20}"
    f"{emp['role'].upper():<12}"
    f"{len(emp['access']):<6}"
    f"{' | '.join(emp['access'])}"
)
print("Total Employees", len(employees), sep=": ", end=" | ")
print("Total Tools", len(tools), sep=": ", end=" | ")
print("Log Entries", len(access_log), sep=": ")
print("\nRecent Access Log:")
print(access_log[-3:])
print("\n" + "=" * 60)
print("ACCESS GUARD REPORT GENERATED SUCCESSFULLY".center(60))
print("=" * 60)