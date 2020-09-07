# CIS41A: Lab3 Classes and Lists: Nandhini Pandurangan
# This program creates two classes Student and Course to output a list of students sorted by their last names


# Student class contains 2 strings: the first and last name of the student
class Student:

    # constructor
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # defines how print() is used on Student objects
    def __str__(self):
        return self.first_name + " " + self.last_name

    # overloading the less than < operator to allow for comparison between student last names
    def __lt__(self, right):
        return self.last_name < right.last_name


# The Course class contains a list of students
class Course:

    # constructor
    def __init__(self):
        self.list_students = []

    # reader() reads the csv file
    def reader(self, csvfile):
        csv = open(csvfile)  # opening the file
        for line in csv:  # iterating through file contents
            rline = line.rstrip()  # strips away the new line carriage return character
            line_info = rline.split(",")  # line_info: list of the elements of the line after it is split by a comma

            st = Student(line_info[0], line_info[1])  # calls the Student constructor using the elements of line_info
            self.list_students.append(st)  # storing the student object in the list of students

        # sort_by_last_name() sorts the list of students using Python's built-in function sort()

    def sort_by_last_name(self):
        self.list_students.sort()

    # output_list() outputs the list of students in the course
    def output_list(self):
        print()
        print("---  List of students in this course:  ---")
        for i in range(0, len(self.list_students)):
            print(self.list_students[i])


# main() creates a Course object
def main():
    c = Course()
    c.reader("Students.txt")
    c.sort_by_last_name()
    c.output_list()


# calling main()
main()
