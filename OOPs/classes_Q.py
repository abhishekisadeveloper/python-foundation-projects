# 1. Student Class
# Create a Student class with:

# name
# age
# course

# Add a method display_info() that prints all three details.

# Example:

# student = Student("Abhishek", 22, "B.A.")
# student.display_info()

# Expected:

# Name: Abhishek
# Age: 22
# Course: B.A.


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")


student_one = Student("Abhishek", 23, "CS")

student_one.display_info()


# 2. Bank Account
# Create a BankAccount class with:

# account_holder
# balance

# Add two methods:

# deposit(amount) → adds money to the balance
# withdraw(amount) → subtracts money only if sufficient balance exists

# Test it with:

# account = BankAccount("Abhishek", 5000)
# account.deposit(2000)
# account.withdraw(1500)


class BankAccount:
    initial_balance = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.initial_balance += balance
        print(f"initial balance: {self.initial_balance}")

    # For deposit money
    def deposit(self, amount):
        self.initial_balance += amount
        print(f"Added Amount: {amount}")

    # For withdraw money
    def withdraw(self, amount):
        self.amount = amount
        if amount < self.initial_balance:
            self.initial_balance -= amount
            print(f"withdraw Amount: {amount}")
        else:
            print("No suficient Amount to withdraw.")

    # For check balance
    def get_balance(self):
        print(f"Total Amount: {self.initial_balance}")


s1 = BankAccount("Abhishek", 10000)
s1.deposit(1000)
s1.withdraw(50000)
s1.get_balance()


# 3. Employee Salary System
# Create an Employee class with:

# name
# salary
# department

# Add methods:

# give_raise(percentage) → increases salary by the given percentage
# display_salary() → displays the current salary

# Example:

# emp = Employee("Rahul", 40000, "Backend")
# emp.give_raise(10)
# emp.display_salary()

# Expected salary:

# 44000

# Challenge: Don't create a separate variable outside the class to calculate the new salary. The object itself should maintain its state.


class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def give_raise(self, percentage):
        self.salary += int(self.salary / percentage)

    def display_salary(self):
        print(f'New Salary: {self.salary}')

emp = Employee("Rahul", 100, "Backend")
emp.give_raise(10)
emp.display_salary()