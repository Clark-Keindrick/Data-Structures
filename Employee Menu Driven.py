import os  # allows us to run a command in the Python script


class Information:  # Creating a node for employee's information
    def __init__(self, id=None, name=None, address=None, salary=None):
        self.prev = None
        self.ID = id
        self.Name = name
        self.Address = address
        self.Salary = salary
        self.next = None


class Employee:  # class creation
    def __init__(self):  # initiating a self head
        self.head = None

    def add_employee(self, id, name, address, salary):  # method to add an employee
        employee = Information(id, name, address, salary)  # object instantiation

        if self.head:
            current = self.head

            while current.next:
                current = current.next
            current.next = employee
            employee.prev = current
            current = employee

        else:
            self.head = employee

    def search_employee(self, search_name):  # method to search an employee
        if self.head:
            current = self.head

            while current.next is not None and search_name not in current.Name:
                current = current.next

            if current.next is None and search_name not in current.Name:
                print("\nNo Records Found!!!")
            else:
                print("ID No.", current.ID)
                print("Employee name:", current.Name)
                print("Employee Address:", current.Address)
                print("Salary: P{:,.2f}".format(current.Salary))

        else:
            print("\nRecords are empty")

    def total_employees(self):  # method to get the total number of employees
        count = 0
        current = self.head

        while current:
            current = current.next
            count += 1
        print("\nThere are %d total numbers of employees" % count)

    def Total_Average_Salary(self):  # method to get the total average of all employee's salary
        count = 0
        Total = 0.0
        Average = 0.0

        if self.head:
            current = self.head

            while current:
                count += 1
                Total = Total + current.Salary
                current = current.next
            Average = Total / count

            print("\nTotal Average of Salary: P{:,.2f}".format(Average))

        else:
            print("\nAverage = 0.0")

    def delete_employee(self, search_id):  # method to delete an employee using their ID number
        if self.head:
            current = self.head

            if current.ID == search_id:
                self.head = self.head.next
                print("\nEmployee has been removed from the record list")
                return

            while current.next is not None and current.ID != search_id:
                current = current.next

            if current.next is None and current.ID != search_id:
                print("\nNo ID found in the records")

            elif search_id == current.ID and current.next is None:
                current.prev.next = None
                print("\nEmployee has been removed from the record list")

            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                print("\nEmployee has been removed from the record list")

        else:
            print("\nNo Records Show")

    def display(self):  # method to display all the employees with their information
        current = self.head

        while current:
            print("ID No.", current.ID)
            print("Employee name:", current.Name)
            print("Employee Address:", current.Address)
            print("Salary: P{:,.2f}".format(current.Salary))
            print()
            current = current.next


e = Employee()  # object instantiation

# storing at least 20 employees to the records list
e.add_employee(str(11).zfill(4), "Jecyl Gurrea", "Deca Homes, Ibabao Agus, Lapu- Lapu City", 21500.45)
e.add_employee(str(12).zfill(4), "Sherilyn Rico", "Pajac, Lapu-Lapu City", 18700.83)
e.add_employee(str(13).zfill(4), "Kurt Imperial", "Datag, Lapu-Lapu City", 25650.36)
e.add_employee(str(14).zfill(4), "Pence Palacio", "Babag 1, Lapu-Lapu City", 15000.90)
e.add_employee(str(15).zfill(4), "John Micheal Miano", "Suba Masulog, Basak Lapu-Lapu City", 20900.12)
e.add_employee(str(16).zfill(4), "Phoebe Ausan", "Pajo, Lapu- Lapu City", 15837.33)
e.add_employee(str(17).zfill(4), "Merna May Cudiera", "Gun-ob, Lapu-Lapu City", 16345.24)
e.add_employee(str(18).zfill(4), "Crizel Estorba", "Mabini, Bohol", 24356.66)
e.add_employee(str(19).zfill(4), "Dolph Brian Bitos", "Mabolo, Cebu City", 12000.00)
e.add_employee(str(20).zfill(4), "Harold Mansubre", "Pardo, Cebu City", 18500.25)
e.add_employee(str(21).zfill(4), "Karylle Serrano", "Basak, Lapu- Lapu City", 10450.50)
e.add_employee(str(22).zfill(4), "Jimcarry Omambak", "Marigondon, Lapu-Lapu City", 16000.00)
e.add_employee(str(23).zfill(4), "Aileen Velasco", "Canjulao, Lapu-Lapu City", 25000.00)
e.add_employee(str(24).zfill(4), "Angel Espinosa", "Marigondon, Lapu-Lapu City", 15000.00)
e.add_employee(str(25).zfill(4), "Marjerie Orapa", "Bangkal, Basak Lapu-Lapu City", 30000.00)
e.add_employee(str(26).zfill(4), "Maui Dano", "Sudtunggan, Basak, Lapu- Lapu City", 35837.95)
e.add_employee(str(27).zfill(4), "Shanley Mae Padirogao", "Poblacion, Lapu-Lapu City", 24000.55)
e.add_employee(str(28).zfill(4), "Jamaikha Miticua", "Calawisan, Lapu-Lapu City", 28450.50)
e.add_employee(str(29).zfill(4), "Smith Virgil Booc", "Opao, Mandaue City", 30750.71)
e.add_employee(str(30).zfill(4), "Neil Baligasa", "Looc, Mandaue City", 40000.25)

while True:  # Infinite loop for user input
    os.system('cls')  # system clear screen to clear the previous input in the console

    print("[1]- Add Employee")
    print("[2]- Search Employee (Based on Name)")
    print("[3]- Display All Employee")
    print("[4]- Get the total numbers of employees")
    print("[5]- Get the Total Average of Salary")
    print("[6]- Delete an Employee based on the ID")
    print("[0]- Exit")

    choice = int(input("\nPlease Select a Number: "))

    while choice == 1:  # while loop for user's input choice
        os.system('cls')
        print("Fill the required information to add an employee\n")
        id = str(input("Input ID number: ")).zfill(4)  # zfill function to add leading zeroes in your id number
        name = input(
            "Input the Name: ").title()  # title function to automatically capitalize the first letter of every words
        address = input("Input the Address: ").title()
        salary = float(input("Input the Salary: "))

        e.add_employee(id, name, address, salary)

        os.system('cls')
        print("\nEmployee has been added to the record list!!!")
        press = input("\nPress any key to add again and press 'x' if you want to exit: ")
        if press.lower() == 'x':
            break

    while choice == 2:
        os.system('cls')
        print("Search Employee (Based on Name)")
        search = input("\nPlease Input the Employee's Name: ")

        print()
        os.system('cls')
        e.search_employee(search.title())

        press = input("\nPress any key to search again and press 'x' if you want to exit: ")
        if press.lower() == 'x':
            break

    while choice == 3:
        os.system('cls')
        print("Employee's Record List\n")

        e.display()

        press = input("\nPress 'x' if you want to exit: ")
        if press.lower() == 'x':
            break

    while choice == 4:
        os.system('cls')

        e.total_employees()

        press = input("\nPress 'x' if you want to exit: ")
        if press.lower() == 'x':
            break

    while choice == 5:
        os.system('cls')

        e.Total_Average_Salary()

        press = input("\nPress 'x' if you want to exit: ")
        if press.lower() == 'x':
            break

    while choice == 6:
        os.system('cls')
        ID_no = str(input("Input the ID Number: ")).zfill(4)

        os.system('cls')
        e.delete_employee(ID_no)

        press = input("\nPress any key to delete again and press 'x' if you want to exit: ")
        if press.lower() == 'x':
            break

    if choice == 0:
        break

# def search_employee(self, search_name):
#      if self.head:
#          current = self.head
#
#          while current.next is not None and search_name not in current.Name:
#              current = current.next
#
#          if current.next is None and search_name not in current.Name:
#              print("\nEmployee Doesn't exist")
#          else:
#              print("ID No.", current.ID)
#              print("Employee name:", current.Name)
#              print("Employee Address:", current.Address)
#              print("Salary: P{:,.2f}".format(current.Salary))
#
#      else:
#          print("\nRecords are empty")
