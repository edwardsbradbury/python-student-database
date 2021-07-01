students=[]

def main():
    '''Main menu function. Users can choose to add or remove a student record, add grades
    to a student's record, display a list of all students in the database (ordered by
    highest GPA to lowest), or exit.'''
    
    options=["A","G","L","R","X"]
# User input will be tested against the above 'options' for validity.
    while True:
        option=input('''
        What would you like to do:

        A) To enter a new student into the database, type A and hit return
        G) To add a student's grade to the database, type G and hit return
        L) For a list of all students in the database, type L and hit return
        R) To remove a student from the database, type R and hit return
        X) To exit, type X and hit return
        ''')
        option=(option.strip())

# Tests whether user input matches anything in previously specified list ('options' variable) of valid inputs.
# Input converted to uppercase. If user input is lowercase equivalent of something in the
# list of valid options, program will continue without prompting user to re-enter an option.
# If user input not valid, program prompts user to re-enter a valid input.
# User is repeatedly prompted for input until a valid 'option' is entered.
        if option.upper() not in options:
            print("Command not recognised.")
            continue
        if (option.upper())=="A":
            addNewStudent()
        elif (option.upper())=="X":
            print("Thank you, goodbye.")
            exit()
# Inputting G (add grade function), L (list all records function) or R (remove student record
# function) will only execute those functions if the database contains at least 1 record.
# Otherwise, message is displayed to user stating the database is empty.
        elif (len(students)==0):
            print("The database is empty.")
        elif (option.upper())=="G":
            addGrade()
        elif (option.upper())=="L":
            listDatabase()
        elif (option.upper())=="R":
            removeStudent()



def addNewStudent():
    '''Function to add new student records to the database (list in 'students' variable.
    Lots of input validation.
    All names are stored in the format "Lastname, Firstname" regardless of the format
    (e.g. capitalization or white space) the user inputs.'''

    first=input("Enter the student's first name:")
    while first.isalpha() is False:
# Checks the validity of the first name (forename) entered by user. If input contains anything
# other than letters, user is shown an error message and program returns to main menu.
        print("Error: the student's forename should not contain numbers, punctuation or spaces.")
        main()

    last=input("Enter the student's last name:")
    while last.isalpha() is False:
# Checks the validity of the last name (surname) entered by user. If input contains anything
# other than letters, user is shown an error message and program returns to main menu.
        print("Error: the student's surname should not contain numbers, punctuation or spaces.")
        main()
        
    newStudent=((last.strip().title())+", "+(first.strip().title()))
# Converts the first and last names input by user, into one object in format <Lastname, Firstname>
    if any(newStudent in i for i in students):
# Checks whether the database already contains a student with the name entered by user.
# If so, user is informed the student already has a record and program returns to main menu.
        print(first.title(),last.title(),"already exists in the database.")
        main()
    else:
# If the name entered by user does not have a record, a new sublist is created in the 'students' list.
# A student's sublist (or record) contains 4 elements, respectively: GPA, full name, credit hours, quality points.
# GPA value is first for ease of sorting the students by GPA score.
        students.append([0, newStudent, 0, 0])
        print(first.title(),last.title(),"has been added to the database.")
# Message displayed to user confirming that the student has been added to the database.
        main()



def studentIndex(student):
    '''Function to return the index of the sublist (or record) containing a particular student
    within the main database (list). Necessary for removing students and adding grades.'''

    for i in students:
        if i[1]==student:
            return students.index(i)



def removeStudent():
    '''Function to remove a student from the database. Asks the user which student to remove.
    If no student record exists in database with name input by user, message is displayed to user.'''
    
    first=input("Enter the student's first name:")
    last=input("Enter the student's last name:")
    student=((last.strip().title())+", "+(first.strip().title()))
    
    if any(student in i for i in students):
# Checks whether the main database contains a sublist containing the name entered by user.
        record=studentIndex(student)
# Retrieves the index of sublist containing the student name entered by user.
        del students[record] # Removes the sublist at the index retrieved on previous line.
        print(first.title(),last.title(),"has been removed from the database.")
# Message displayed to user confirming that the specified student was removed from database.
        main()
    else:
# If no sublists in database contain the name entered, message is displayed to user.
        print(first.strip().title()+" "+last.strip().title(),"was not in the database.")
        main()



def listDatabase():
    '''Function to display to user a list of all students in database, listed in order
    from student with highest GPA at top, to lowest GPA at bottom.'''

    students.sort(reverse=True)
# Sorts all sublists in database by their first element (the GPA score). reverse=True is
# necessary because Python would sort in ascending order by default, not descending order.
    for i in students:
        if i[0]==0:
# Checks whether each student has a GPA score (greater than 0). For those who do not have
# a score, output displayed to user will say "GPA: None".
            print(i[1],"- GPA: None")
        else:
# For those students who do have scores, output to user will be displayed as follows:
# <Lastname, Firstname> - GPA: <score>
# The GPA score is rounded to 2 decimal places for neatness.
            print(i[1],"- GPA:",round(i[0],2))
    main()



def addGrade():
    '''Function to add grades for a student with an existing record in the database.'''
    
    first=input("Enter the student's first name:")
    last=input("Enter the student's last name:")
    student=((last.strip().title())+", "+(first.strip().title()))
    grades=["A","B","C","D"]
# User input for the 'grade' variable below will be tested against above 'grades' list for validity.

    if any(student in i for i in students):
# Checks whether the main database contains a sublist containing the name entered by user.
        grade=input("Enter the grade for"+" "+first.title()+" "+last.title()+" "+"(as A,B,C or D):")

        while grade.upper() not in grades:
# Tests whether user input matches anything in previously specified list ('grades' variable) of valid inputs.
# Input converted to uppercase. If user input is lowercase equivalent of something in the
# list of valid options, program will continue without prompting user to re-enter an option.
# Otherwise, user is repeatedly prompted for input until a valid option is entered.
            print("Error: the grade should be A,B,C or D.")
            grade=input("Enter the grade for"+" "+first.title()+" "+last.title()+" "+"(as A,B,C or D):")

# The following if/elif statements convert the Grade letter input to a number, for use when Quality
# Points are calculated.
        if grade.upper()=="A":
            grade=float(4.0)
        elif grade.upper()=="B":
            grade=float(3.0)
        elif grade.upper()=="C":
            grade=float(2.0)
        elif grade.upper()=="D":
            grade=float(1.0)

# The following code block tests validity of user input for a student's Credit Hours.
        inputFloat=False # Sentinel value
        while inputFloat==False:
            hours=input("Enter the number of credit hours for"+" "+first.title()+" "+last.title()+":")
            try:
# Program will try to convert the user input for Credit Hours to a float.
                float(hours)
                if float(hours)<=0:
# If user input could successfully convert to float (Credit Hours can be either whole hours
# or only partial hours), checks whether value is greater than 0. If condition is False,
# user will be repeatedly prompted to input a number of Credit Hours greater than 0.
                    print("Error: the number of credit hours should be more than zero.")
                    continue
                if hours=="nan" or hours=="inf":
# Python can successfully convert 'nan' and 'inf' to floats, but we would be unable to
# calculate the Quality Points using these objects. User input is tested against these and
# if matches either 'nan' or 'inf', user is repeatedly prompted to re-enter Credit Hours
# until a usable value is input.
                    print("Error: the number of credit hours should be a numeric value.")
                    continue
            except ValueError:
# If the Credit Hours input by user could not be converted to float, it must have contained
# non-numeric data. We would be unable to use the data input for calculating Quality Points,
# so the user is repeatedly prompted to re-enter the Credit Hours until a usable value is input.
                print("Error: the number of credit hours should be a numeric value.")
                continue
            else:
# If this clause is executed, the Credit Hours user input must be either an integer or decimal,
# either of which can be used to calculate Quality Points. Input is converted to float and stored
# in a variable for use in calculating Quality Points.
                hours=float(hours)
            inputFloat=True # Updating sentinel value to break loop.
# Only executed when input validity is confirmed above. Necessary for program to proceed.
            
        record=studentIndex(student)
# Retrieves the index of the student (whose name user specified above) record within main database.
        points=grade*hours # Calculates value of Quality Points and saves in a variable.
        students[record][2]+=hours # Updates the Credit Hours value in the student's record (sublist).
        students[record][3]+=points # Updates the Quality Points value in student's record.
        gpa=(students[record][3]/students[record][2]) # Calculates the student's current GPA.
        students[record][0]=gpa # Update's the GPA value in the student's record.
        print(round(points,2),"quality points have been added to",first.title()+" "+last.title()+"'s record.")
# Message displayed to user confirming that Quality Points have been added to student's record.
        main()
    else:
# Warning message displayed to tell user that the student whose grade they want to add has no record in database.
        print(first.title(),last.title(),"is not in the database.")
        main()
                
main()
