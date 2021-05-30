#Project 1: Basic School administration tool
import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "contact_number", "E-mail"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True

while(condition):
 student_info = input("Enter student information in the following format (Name Age contact_number E-mail_ID: ")


 # split
 student_info_list = student_info.split(" ")


 print("\nThe entered information is -\nName: {}\nAge: {}\nContact_number: {}\nE-mail ID: {}"
         .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

 choice_check = input("Is the entered information is correct? (YES/NO):")

 if choice_check == "YES":
    write_into_csv(student_info_list)

    condition_check = input("Enter (YES/NO) if you want to enter information for another student: ")
    if condition_check == "YES":
        condition = True
    elif condition_check == "NO":
        condition = False
 elif choice_check == "NO":
    print("\nPlease re-enter the values!")
