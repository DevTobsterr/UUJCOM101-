#UUJ COURSEWORK
#OBJECT PYTHON FOR COM101
#EMPOLYEE DATA MANAGEMENT TOOL
#DEVELOPED BY TOBY KILLEN
#B00753973

#SECTION 1 - IMPORTING
import os
import time
#SECTION 2 - FUNCTIONS
def header():
    print("Welcome to the Employee Management Tool v1.6")
    print("Developed By Toby Killen")
    print("--------------------------------------------")

def helpFunction():
    print("read - Print out number of data entires in database.")
    print("readall - List employees and Details.")
    print("salary - Print report on total salary.")
    print("salary -a - Print report on average salary based on number of employee.")
    print("add - Add new employee to database.")
    print("group - Print report detailing number of employee grouped by each position.")
    print("query - Query the list, returning employees above set salary.")
    print("exit - Quits the Data management tool.")
    print("cls - Clears the GUI.")

def mainMenu1():
    header()
    while True:
        userinput = str(input(">>> "))
        if userinput == str("readall"):
            readallFunction()
        elif userinput == str("read"):
            readFunction()
        elif userinput == "add":
            addFunction()
        elif userinput == "salary":
            salaryFunction()
        elif userinput == "salary -a":
            avgSalaryFunction()
        elif userinput == "group":
            groupFunction()
        elif userinput == "query":
            queryFunction()
        elif userinput == "cls":
            os.system("cls")
            mainMenu1()
        elif userinput == "exit":
            quit()
        elif userinput == "help":
            helpFunction()

def readallFunction():
    dataset = open("dataset.txt","r")
    next(dataset)
    fdataset = dataset.read()
    print(fdataset)
    dataset.close()

def readFunction():
    dataset = open("dataset.txt","r")
    line = 0
    for lines in dataset:
        line = line + 1
    dataset.close()
    print("This dataset contains",line - 1,"data entries. ")

def addFunction():
    dataset = open('dataset.txt','a') # OPENS THE FILE IN APPEND MODE
    emp_no = int(input("Employee Number: "))
    for line in dataset:
        if emp_no in line:
            print("Please Enter a employee number which has not already been taken. ")
        else:
            pass

    emp_name = input("Employee Name: ")

    age = int(input("Employee Age: "))
    if age >= 18:
        pass
    else:
        print("Error. Employee must be 18 years old or older. ")
        time.sleep(5)
        os.system("cls")
        mainMenu1()

    position = input("Employee Position: ")
    if position == "Developer":
        pass
    elif position == "Tester":
        pass
    elif position == "DevOps":
        pass
    elif position == "Analyst":
        pass
    else:
        print("Error. Position has to be 'Developer','Tester','DevOps' or 'Analyst'")
        time.sleep(5)
        os.system("cls")
        addFunction()

    salary = int(input("Employee Salary: "))

    yrs_emp = int(input("Year's Employed: "))
    if yrs_emp >= 0:
        pass
    else:
        print("Error. Year's employed can not be negative. ")
        time.sleep(5)
        os.system("cls")
        mainMenu1()

    dataset.write("\n")
    dataset.write(str(emp_no) + ", " + str(emp_name) + ", " + str(age) + ", "+ str(position) + ", "+ str(salary)+ ", " + str(yrs_emp))
    print("\nEmployee Successfully added")
    time.sleep(3)
    dataset.close()
    os.system("cls")
    mainMenu1()

def salaryFunction():
    dataset = open("dataset.txt","r")
    next(dataset)
    totalsalary = 0
    for line in dataset:
        salary1 = line.split(',')
        salary = salary1[4]
        salary2 = int(salary)
        totalsalary += salary2
    print("The total salary bill for all employee's is",format(totalsalary, ".2f"))
    dataset.close()

def avgSalaryFunction():
    dataset = open("dataset.txt", "r")
    next(dataset)
    totalsalary = 0
    for line in dataset:
        salary1 = line.split(',')
        salary = salary1[4]
        salary2 = int(salary)
        totalsalary += salary2

    dataset = open("dataset.txt","r")
    line = 0
    for lines in dataset:
        line = line + 1
    dataset.close()
    print("The Average salary for each employee is $",format(totalsalary / line, ".2f"))

def groupFunction():
    dataset = open("dataset.txt","r")
    next(dataset)
    devopscount = int(0)
    testercount = int(0)
    devcount = int(0)
    analystcount = int(0)

    for line in dataset:
        job1 = line.split(',')
        job = job1[3]

        if "DevOps" in job:
            devopscount += 1
        else:
            pass

        if "Developer" in job:
            devcount += 1
        else:
            pass

        if "Tester" in job:
            testercount += 1
        else:
            pass

        if "Analyst" in job:
            analystcount += 1
        else:
            pass

    print("Currently employed are the following: ")
    print(devopscount, "DevOps")
    print(devcount, "Developers")
    print(testercount, "Testers")
    print(analystcount, "Analysts")
    dataset.close()

def queryFunction():
    dataset = open("dataset.txt","r")
    next(dataset)
    userinput = input("Salary Query. Please enter the salary threshold you would like to return: ")

    for line in dataset:
        salary3 = line.split(',')
        salary = salary3[4]
        if salary3 >= userinput:
            return line
        else:
            print("No Employee earns above set threshold. ")
            time.sleep(4)
            os.system("cls")
            mainMenu1()
    dataset.close()


#SECTION 3 - MAIN FUNCTION CALL
mainMenu1()