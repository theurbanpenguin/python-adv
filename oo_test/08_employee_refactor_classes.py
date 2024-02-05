from employee import Manager, Waiter, Chef, Mechanic

if __name__ == '__main__':
    employees = [
        Manager("Vera", 2000),
        Waiter("Chuck", 1800),
        Waiter("Samantha", 1800),
        Chef("Roberto", 2100),
        Mechanic("Dave", 2200),
        Mechanic("Tina", 2300),
        Mechanic("Ringo", 1900)
    ]

    for e in employees:
        print(f"{e.name}: £{e.salary}: {e.job_title}")