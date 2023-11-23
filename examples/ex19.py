"""
One more list comprehension example
"""


def main():
    employees = [
        "1192,Shyam Sundar,ADMIN,78000",
        "1292,Kishore Kumar,ACCOUNTING,65000",
        "5292,Ramesh Iyer,ADMIN,65000",
        "1283,Ramnath,MARKETING,77000"
    ]

    admin_emp_names = [
        emp.split(',')[1]                   # what is collected
        for emp in employees                # from where is it collected
        if emp.split(',')[2] == 'ADMIN'     # only if this condition is met
    ]

    print(admin_emp_names)

    emps = [
        f'{emp.split(",")[1]} earns Rs.{emp.split(",")[3]}'
        for emp in employees
        if float(emp.split(",")[3]) > 70000
    ]

    print(emps)


if __name__ == '__main__':
    main()
